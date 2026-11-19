"""Build the static demo: src/ + img/ + fonts/ -> dist/.

Usage: python build.py
Expands {{IMG:name|alt|sizes|eager|lazy}}, {{ROOMS}}, {{MENU_*}}, {{SCHEMA}} and inline SVG icons.
"""
import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
SRC, DIST = ROOT / "src", ROOT / "dist"
META = json.loads((ROOT / "img-meta.json").read_text())

CREST = ('<svg class="crest" viewBox="0 0 40 40" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2">'
         '<circle cx="20" cy="20" r="11"/><circle cx="20" cy="20" r="3.2"/>'
         + "".join(f'<path d="M20 {y1}V{y2}" transform="rotate({a} 20 20)"/>' for a in range(0, 360, 45) for y1, y2 in [(2, 9)])
         + '<path d="M20 9v6M20 25v6M9 20h6M25 20h6" /></svg>')
SHIP = ('<svg viewBox="0 0 40 20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2">'
        '<path d="M2 13h30l-4 5H7z"/><path d="M15 13V2l9 9h-9"/><path d="M33 10l5 3-5 3"/></svg>')
WA = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3z"/></svg>')
PHONE = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/></svg>')
FAVICON = CREST.replace('class="crest" ', 'xmlns="http://www.w3.org/2000/svg" ').replace("currentColor", "#1E3A6E")

ROOMS = [
    ("dorm-rope-ladders", "Deluxe 8-bed mixed dorm", "Sleeps 8 · ensuite bathroom", 690, "per bed / night",
     "A dorm with navy wooden bunk frames, rope ladders to the upper berths and a blue glow along the floor"),
    ("dorm-egg-chair", "Standard 8-bed mixed dorm", "Sleeps 8", 750, "per bed / night",
     "A dorm with built-in white bunks and black ladders, blue floor lighting and a hanging wicker egg chair in the middle"),
    ("dorm-warm", "Deluxe 5-bed female dorm", "Women only · sleeps 5 · ensuite", 780, "per bed / night",
     "A warm-lit dorm with a raised bunk, a black ladder and a navy door"),
    ("private-double", "Superior double, private", "Sleeps 2 · private ensuite", 2520, "per room / night",
     "A private room with a low double bed, blue ombré curtains and two patterned armchairs"),
]


def picture(name, alt, sizes, mode):
    m = META[name]
    ws = m["sizes"]
    h = round(m["h"] * ws[-1] / m["w"])
    def ss(ext):
        return ", ".join(f"/img/{name}-{w}.{ext} {w}w" for w in ws)
    eager = mode == "eager"
    attrs = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<picture><source type="image/avif" srcset="{ss("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{ss("webp")}" sizes="{sizes}">'
            f'<img src="/img/{name}-{ws[min(1, len(ws)-1)]}.webp" alt="{html.escape(alt)}" width="{ws[-1]}" height="{h}" {attrs}></picture>')


def rooms():
    out = []
    for name, title, meta, price, unit, alt in ROOMS:
        out.append(
            f'<li class="ticket">{picture(name, alt, "(min-width: 860px) 22vw, 82vw", "lazy")}'
            f'<div class="ticket-body"><h3>{title}</h3><p class="ticket-meta">{meta}</p>'
            f'<div class="ticket-foot"><p class="price">₹{price:,}<small>{unit}</small></p>'
            f'<a class="btn btn-primary btn-sm" href="#book">Book this</a></div></div></li>')
    return "\n    ".join(out)


def menu():
    data = json.loads((SRC / "menu.json").read_text(encoding="utf-8"))
    labels = {"veg": "Veg", "nonveg": "Non-veg", "egg": "Contains egg", "tbc": "Diet marker not confirmed"}
    tabs, panels = [], []
    for i, c in enumerate(data):
        pid, tid = f"menu-p{i}", f"menu-t{i}"
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button role="tab" id="{tid}" aria-controls="{pid}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">{html.escape(c["cat"])}</button>')
        rows = "".join(
            f'<li><span class="mk {k}" role="img" aria-label="{labels[k]}"></span><span>{html.escape(n)}</span><span class="p">₹{p}</span></li>'
            for n, p, k in c["items"])
        panels.append(f'<div class="menu-panel" role="tabpanel" id="{pid}" aria-labelledby="{tid}" tabindex="0"{"" if i == 0 else " hidden"}><ul>{rows}</ul></div>')
    return "\n        ".join(tabs), "\n      ".join(panels), data


def schema(menu_data):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": ["Hostel", "CafeOrCoffeeShop"],
        "name": "The Voyage | Cafe | Hostel | Co-work",
        "description": "Nautical-themed cafe, hostel and co-working space in Koregaon Park, Pune.",
        "image": "/img/hero-boat-ceiling-1280.webp",
        "telephone": "+91-99993-09921",
        "priceRange": "₹690–₹2,520 per night; cafe ~₹1,800 for two",
        "servesCuisine": ["Continental", "Italian", "Healthy food", "Coffee"],
        "address": {"@type": "PostalAddress", "streetAddress": "A/2 Ashiyana Park, Lane 5, North Main Road, Koregaon Park",
                    "addressLocality": "Pune", "addressRegion": "Maharashtra", "postalCode": "411001", "addressCountry": "IN"},
        "geo": {"@type": "GeoCoordinates", "latitude": 18.5394686, "longitude": 73.8975966},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                       "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                       "opens": "09:00", "closes": "23:00"}],
        "checkinTime": "13:00", "checkoutTime": "11:00",
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": 4.4, "reviewCount": 1088, "bestRating": 5},
        "sameAs": ["https://www.instagram.com/thevoyage_pune/", "https://www.zomato.com/pune/the-voyage-koregaon-park"],
    }, ensure_ascii=False)


def build():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    page = (SRC / "index.html").read_text(encoding="utf-8")
    tabs, panels, data = menu()
    page = (page.replace("{{ROOMS}}", rooms()).replace("{{MENU_TABS}}", tabs).replace("{{MENU_PANELS}}", panels)
            .replace("{{SCHEMA}}", schema(data)).replace("{{CREST}}", CREST).replace("{{SHIP}}", SHIP)
            .replace("{{WA}}", WA).replace("{{PHONE}}", PHONE))
    page = re.sub(r"\{\{IMG:([^|]+)\|([^|]+)\|([^|]+)\|(eager|lazy)\}\}", lambda m: picture(*m.groups()), page)
    assert "{{" not in page, re.findall(r"\{\{[^}]*\}\}", page)
    (DIST / "index.html").write_text(page, encoding="utf-8")
    for f in ("styles.css", "app.js", "_headers", "robots.txt"):
        if (SRC / f).exists():
            shutil.copy(SRC / f, DIST / f)
    (DIST / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    shutil.copytree(ROOT / "img", DIST / "img")
    shutil.copytree(ROOT / "fonts", DIST / "fonts")
    print("built", DIST, len(page) // 1024, "KB html")


if __name__ == "__main__":
    build()
