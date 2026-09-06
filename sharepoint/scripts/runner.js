async (page) => {
  const fs = (await import('node:fs')).default;
  const dir = '/Users/alfredang/Documents/Supporting Document/Tertiary Infotech/Tertiary WSQ Projects/TGS-2024051421-Generative AI for Interviewing/courseware/sharepoint/scripts/chunks/';
  const sites = ['FutureTech-Careers','HarbourBank-Talent','MediCare-Recruitment','GreenLogix-Hiring','BrightPath-Careers'];
  const results = [];
  for (const a of sites) {
    const DATA = JSON.parse(fs.readFileSync(dir + a + '.json', 'utf8'));
    const r = await page.evaluate(async ({DATA, a}) => {
      const site = 'https://tertiaryinfotech.sharepoint.com/sites/' + a;
      const dj = await (await fetch(site+'/_api/contextinfo',{method:'POST',headers:{'Accept':'application/json;odata=nometadata'}})).json();
      const digest = dj.FormDigestValue;
      let ok = 0; const fail = [];
      for (const [lib, files] of Object.entries(DATA)) {
        for (const f of files) {
          const bin = Uint8Array.from(atob(f.b64), c => c.charCodeAt(0));
          const url = site + "/_api/web/GetFolderByServerRelativeUrl('/sites/" + a + "/" + lib + "')/Files/add(url='" + encodeURIComponent(f.name) + "',overwrite=true)";
          const rr = await fetch(url, {method:'POST', headers:{'Accept':'application/json;odata=nometadata','X-RequestDigest':digest}, body: bin});
          if (rr.status < 300) ok++; else fail.push({n:f.name, s:rr.status, m:(await rr.text()).slice(0,100)});
        }
      }
      return {ok, fail};
    }, {DATA, a});
    results.push({site: a, uploaded: r.ok, failed: r.fail.length, errors: r.fail.slice(0,2)});
  }
  return JSON.stringify(results, null, 1);
}
