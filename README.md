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

## Deploy (demo): GitHub Pages
`.github/workflows/pages.yml` publishes `site/dist` on every push to `main`.
Live at https://07-soham.github.io/the-voyage-demo/

One-time setup:
1. GitHub Pages needs the repo to be **public**, or a GitHub Pro account for a private repo. Change it under Settings -> General -> Danger Zone -> Change visibility.
2. Go to Settings -> Pages -> Build and deployment -> Source: **GitHub Actions**.
3. Re-run the "Deploy to GitHub Pages" workflow from the Actions tab, or push any commit.

To update: edit `site/src`, run `python build.py` in `site/`, then commit and push.

Note: GitHub Pages ignores `_headers`, so the demo has no CSP or X-Frame headers. The `noindex` meta still keeps it out of search results.

## Deploy (after the client signs): Cloudflare Pages
Connect this repo in Cloudflare -> Workers & Pages -> Create -> Pages -> Connect to Git. Use framework preset None, leave the build command empty, and set the output directory to `site/dist`. `_headers` then applies (CSP, nosniff, Referrer-Policy, Permissions-Policy, X-Frame-Options DENY).
Paths are relative, so the same build works on both hosts. At launch, update the canonical, `og:image` and schema `image` URLs (in `site/src/index.html` and `site/build.py`) to the client's domain.
