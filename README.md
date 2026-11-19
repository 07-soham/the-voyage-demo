# The Voyage: concept demo

A pitch demo website for **The Voyage | Cafe | Hostel | Co-work**, Koregaon Park, Pune. It is a concept demo prepared by Soham and is not the official website.

## Layout
- `BRIEF.md`: the researched facts with source links, and the placeholders.
- `NOTES.md`: photo picks, niche research, the two Stitch directions and the reasons for the pick, check results, and **the list of placeholders the owner must fill**.
- `images/raw/`: the business's own photos. `images/SOURCES.md` records where each one came from.
- `design/`: the Stitch design tokens and a screenshot of Direction B.
- `site/src/`: the page template, CSS, JS, `_headers`, `robots.txt` and the menu data.
- `site/img/`, `site/fonts/`: AVIF/WebP image sizes and the self-hosted fonts.
- `site/dist/`: the built site, ready to deploy.
- `screenshots/`: screenshots at 390 px and 1440 px.

## Build
Requires Python 3.
```
cd site
python build.py
```
This writes `site/dist/`.

## Deploy (Cloudflare Pages)
Set the build output directory to `site/dist`, or upload it directly:
```
npx wrangler pages deploy site/dist --project-name thevoyage-demo
```
`_headers` sets the CSP, nosniff, Referrer-Policy, Permissions-Policy, X-Frame-Options DENY and noindex.
