#!/usr/bin/env python3
"""Publish trainer assessment keys into a Drive limited-access folder and verify privacy."""

from __future__ import annotations

import configparser
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://www.googleapis.com/drive/v3"
REMOTE = "gdrive"


def private_name(name: str) -> bool:
    low = name.strip().lower()
    return (low.startswith("answer to") or low.startswith("answers to")
            or "assessor observation" in low or "observation checklist" in low
            or "assessor checklist" in low or "marking guide" in low)


def load_token(root: str) -> str:
    subprocess.run(["rclone", "lsf", f"{REMOTE}:", "--max-depth", "1",
                    "--drive-root-folder-id", root], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    parser = configparser.RawConfigParser()
    parser.read(Path.home() / ".config" / "rclone" / "rclone.conf")
    blob = parser.get(REMOTE, "token", fallback="")
    token = json.loads(blob).get("access_token") if blob else None
    if not token: raise RuntimeError("rclone gdrive token has no access_token")
    return token


def request(token: str, method: str, path: str, body: dict | None = None) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    for attempt in range(5):
        req = urllib.request.Request(f"{API}/{path}", data=data, method=method,
                                     headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=40) as response: payload = response.read()
            break
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:700]
            limited = exc.code in (403,429) and ("rateLimitExceeded" in detail or "RATE_LIMIT_EXCEEDED" in detail)
            if limited and attempt < 4:
                wait = min(16, 2 ** (attempt + 1))
                print(f"Drive API quota retry in {wait}s")
                time.sleep(wait)
                continue
            raise RuntimeError(f"Drive API {method} failed: HTTP {exc.code} {detail}") from exc
    return json.loads(payload) if payload else {}


def file_path(file_id: str, **params: str) -> str:
    query = urllib.parse.urlencode({"supportsAllDrives":"true", **params})
    return f"files/{file_id}?{query}"


def children(token: str, parent_id: str) -> list[dict]:
    query = urllib.parse.urlencode({
        "q": f"'{parent_id}' in parents and trashed=false",
        "fields": "files(id,name,mimeType,parents,inheritedPermissionsDisabled,capabilities)",
        "supportsAllDrives": "true", "includeItemsFromAllDrives": "true", "pageSize": "1000",
    })
    return request(token, "GET", f"files?{query}").get("files", [])


def folder(token: str, parent_id: str, name: str) -> dict:
    hit = next((f for f in children(token, parent_id)
                if f["mimeType"] == "application/vnd.google-apps.folder" and f["name"].strip().lower() == name.lower()), None)
    if hit: return hit
    return request(token, "POST", "files?supportsAllDrives=true&fields=id,name,mimeType,parents",
                   {"name":name, "mimeType":"application/vnd.google-apps.folder", "parents":[parent_id]})


def permissions(token: str, file_id: str) -> list[dict]:
    fields = "permissions(id,type,role,allowFileDiscovery,permissionDetails)"
    return request(token, "GET", f"files/{file_id}/permissions?supportsAllDrives=true&fields={urllib.parse.quote(fields, safe=',()')}").get("permissions", [])


def remove_anyone_permissions(token: str, file_id: str):
    for perm in permissions(token, file_id):
        if perm.get("type") == "anyone":
            request(token, "DELETE", f"files/{file_id}/permissions/{perm['id']}?supportsAllDrives=true&enforceExpansiveAccess=true")


def anonymous_file_accessible(file_id: str) -> bool:
    url = f"https://drive.usercontent.google.com/download?id={file_id}&export=download"
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            prefix = response.read(4); content_type = response.headers.get("Content-Type", "").lower()
        return prefix.startswith(b"PK") or "officedocument" in content_type
    except urllib.error.HTTPError:
        return False


def main() -> int:
    if len(sys.argv) != 2: raise SystemExit("usage: publish_private_assessments.py <course-root-folder-id>")
    root = sys.argv[1]
    local = sorted(p for p in (Path(__file__).resolve().parents[1] / "assessment").glob("*.docx") if private_name(p.name))
    if not local: raise RuntimeError("No trainer-only assessment documents found locally")
    token = load_token(root)
    trainer = folder(token, root, "Trainer Resources")
    keys = folder(token, trainer["id"], "Assessment Answer Keys")
    fields = urllib.parse.quote("id,name,inheritedPermissionsDisabled,capabilities(canDisableInheritedPermissions)", safe=",()")
    restricted = request(token, "PATCH", file_path(keys["id"], fields=fields), {"inheritedPermissionsDisabled": True})
    if not restricted.get("inheritedPermissionsDisabled"):
        raise RuntimeError("Drive did not confirm limited access on Assessment Answer Keys")

    # Move any old keys/checklists out of the learner Assessment tree, including archive/.
    assessment = next((f for f in children(token, root)
                       if f["mimeType"] == "application/vnd.google-apps.folder" and f["name"].strip().lower() == "assessment"), None)
    public_parents = []
    if assessment:
        public_parents.append(assessment)
        public_parents += [f for f in children(token, assessment["id"])
                           if f["mimeType"] == "application/vnd.google-apps.folder" and f["name"].strip().lower().startswith("archiv")]
    moved = 0
    for parent in public_parents:
        for item in children(token, parent["id"]):
            if item["mimeType"] != "application/vnd.google-apps.folder" and private_name(item["name"]):
                request(token, "PATCH", file_path(item["id"], addParents=keys["id"], removeParents=parent["id"], fields="id,name,parents"), {})
                remove_anyone_permissions(token, item["id"]); moved += 1

    target_path = "Trainer Resources/Assessment Answer Keys"
    for path in local:
        subprocess.run(["rclone", "copyto", str(path), f"{REMOTE}:{target_path}/{path.name}",
                        "--drive-root-folder-id", root], check=True)

    current = children(token, keys["id"])
    target_names = {p.name for p in local}
    targets = [f for f in current if f["name"] in target_names]
    if len({f["name"] for f in targets}) != len(target_names):
        raise RuntimeError("Not all current trainer assessment documents were found in restricted Drive folder")
    failures = []
    for item in targets:
        remove_anyone_permissions(token, item["id"])
        public = any(p.get("type") == "anyone" for p in permissions(token, item["id"]))
        anonymous = anonymous_file_accessible(item["id"])
        print(f"private key: {item['name']} | anyone_permissions={public} | anonymous_download={anonymous}")
        if public or anonymous: failures.append(item["name"])

    leaked = []
    for parent in public_parents:
        leaked += [f["name"] for f in children(token, parent["id"])
                   if f["mimeType"] != "application/vnd.google-apps.folder" and private_name(f["name"])]
    if leaked: failures.append("learner-tree leaks: " + ", ".join(leaked))
    if failures: raise RuntimeError("Privacy verification failed: " + "; ".join(failures))
    print(f"PASS private assessment gate: limited_access=true current_keys={len(targets)} legacy_moved={moved} learner_tree_leaks=0")
    return 0


if __name__ == "__main__": raise SystemExit(main())
