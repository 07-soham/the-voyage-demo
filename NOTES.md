# NOTES: The Voyage demo

## 1. Photos picked (from images/raw, all property-published)

The photo that sets the mood is **bk-442609951**: the upside-down boat set into a sea-blue painted ceiling above navy booths, with oars and nets on the walls. No other cafe or hostel in Pune has this, so the site is built around it.

Supporting photos: the facade with the ship's-wheel crest (bk-442609943), the rope-ladder dorm with blue floor glow (bk-442609757), the egg-chair dorm (bk-442609910), the private double with ombré curtains (bk-442609766), the courtyard with porthole rings and banana plants (bk-442609752), the oars-and-wheel lounge (bk-442609845), the astroturf terrace (bk-442609893), plates styled on fishing net (bk-442609917, bk-442609919), and courtyard events (bk-463770590, bk-469964752).
Converted to AVIF and WebP at 480/800/1280 px in `site/img/` (see `site/img-meta.json`).

## 2. What the best sites in this niche do (hostel + cafe + co-work)

1. **Price per night before anything else.** Zostel, The Hosteller and goSTOPS put "from ₹X/night" next to every room photo and in the hero, because backpackers sort by price first. → The hero and room list lead with "Dorm beds from ₹690".
2. **Room-type photos, then a date picker that goes straight to booking, plus a "book direct" reason.** The best independents (Moustache, Zostel) give each bed type its own photo, capacity, ensuite or shared bathroom, and price, and the date widget is reachable from every screen. → The boarding-pass widget sits in the first screen, a sticky "Book a bed" bar follows you on mobile, and the pass carries "Book direct and skip the app fees" (the property currently sells through Hostelworld, Booking.com, Goibibo and MMT).
3. **Show the social life, not just the beds.** Successful hostel-cafes (Social, Zostel, Backpacker Panda) sell events, the common room and the cafe menu as a reason to stay, and cafes link straight to Zomato for orders and tables. → An events section from real posters, a full menu with veg/non-veg markers and prices, and Zomato order/table links.

Also: WhatsApp-first contact (Indian travellers message before booking), a map plus walking times to landmarks (Osho Teerth Park, Aga Khan Palace), and house rules stated plainly (18+, local IDs not accepted, check-in 1 pm).

## 3. Design directions (Stitch)

Stitch project: "The Voyage Pune – homepage directions" (id 6958753537801989571, private, in Soham's Stitch account).

**Direction A: "Ship's Manifest".** A dark full-bleed hero of the real boat ceiling, then a **boarding-pass booking widget** (FROM your city → TO Koregaon Park, check-in/out, guests, berth, perforated stub with "Dorm beds from ₹690" and "Book direct and skip the app fees"). Room "tickets", a logbook-ruled menu, and ledger-style house rules. Stitch generated the design system for this direction ("Maritime Manifest": navy #1E3A6E, rope #C89B6A, sea-mural #2E7FA8, Space Mono + Work Sans, 0 radius, hard offset shadows, perforated ticket stubs). Exported to `design/tokens.json`.
_Stitch caveat:_ the A screens were generated (Stitch's agent confirms "SCREEN_4" and "SCREEN_13" exist in the project), but the MCP `list_screens` call returned nothing and the A generations timed out on the client side, so no A screenshot could be pulled through the API. Open the Stitch project in the browser to see them.

**Direction B: "Courtyard Daylight".** An airy, editorial page led by the courtyard and the cafe: "Breakfast at nine. A bed by one. Desk all day." Eat / Stay / Work split, big rating number, tabbed menu. Screenshot: `design/stitch-B-courtyard-daylight-mobile.jpg`.

### Pick: A, "Ship's Manifest"

1. **It's specific to this place.** The boat ceiling, oars, nets and rope-ladder bunks are what guests photograph and what Zomato tags ("Theme", "Interior", "Insta-worthy spots"). A boarding pass for a ship-themed hostel can't be moved to another business's site. B's courtyard-and-greenery look fits any Koregaon Park cafe.
2. **It converts better for the money-maker.** Hostel beds are the highest-value action. A puts the date picker and "from ₹690" in the first screen on mobile; B pushed booking below a lifestyle hero.
3. **B drifted off the brief.** Stitch filled B with AI stock photos instead of the real ones, invented a testimonial ("Aarav M."), invented prices (₹850 female dorm, ₹490 day pass, "100mb fiber") and added "Section 01/02" labels. All of these break the studio rules.

### Refinements made while building A
- The boarding pass is the one animated moment: it "prints" up out of a slot once on load (off under `prefers-reduced-motion`).
- Hard offset shadows only on actions and the pass, not on every card. Section layouts vary: full-bleed photo → ticket rail → split cafe with sticky photos → navy reviews band → co-work split → events grid.
- Rope tan and sea blue are too light for text on white, so text uses darker variants (`rope-ink`, `sea-ink`) to meet AA.
- Uppercase mono labels are limited to form fields and ledger keys, not stacked above every heading.
- Stitch's invented facts were dropped. Only BRIEF.md facts are used.

## 4. Checks (19 Nov 2026)

- Lighthouse mobile, served with the production `_headers` and gzip: **Performance 99, Accessibility 100, Best Practices 100, SEO 69**. LCP 2.1 s, CLS 0.036, TBT 0 ms.
  - SEO is 69 only because of the `noindex` meta, `X-Robots-Tag` and `robots.txt Disallow` that the demo rules require (Lighthouse's "page is blocked from indexing" audit). With those removed, as they will be at launch, SEO is **100**.
- No console errors and no broken images. No horizontal overflow at 390 px or 1440 px.
- Keyboard: every control can be reached and has a visible focus ring. The menu tabs work with arrow, Home and End keys, and Escape closes the demo dialog.
- Screenshots are in `screenshots/`.

## 5. Placeholders the owner must fill

Each of these shows on the site as a dashed "owner to add" tag, and BRIEF.md has the source details.

1. **WhatsApp number.** The site uses +91 99993 09921 (from Instagram) until the owner confirms it.
2. **Main phone number.** Three are listed publicly: 99993 09921, 75075 82162 and 85969 50267. Pick one for "Call".
3. **Email address.**
4. **Direct-booking prices or discount.** The site shows Hostelworld's "from" prices (₹690 / ₹750 / ₹780 / ₹2,520, plus 12% tax).
5. **Room-to-photo match.** Confirm which photo shows which dorm.
6. **Breakfast.** Is it included? Hostelworld contradicts itself.
7. **Parking.** Booking.com says none, but Google and Zomato mention valet.
8. **Co-work.** Day-pass and monthly-desk prices, hours, seat count and WiFi speed.
9. **Upcoming event dates.** The site shows past events only.
10. **Swiggy link.**
11. **Menu.** Veg and non-veg markers (desserts are unmarked) and dine-in prices. The site uses Zomato prices from Nov 2026.
12. **Pet policy.** The cafe is listed as pet-friendly, but the hostel policy is unknown.
13. **Real domain.** Update the canonical and OG URLs, which are now `thevoyage-demo.pages.dev`.
14. **At launch:** remove the demo banner, the `noindex` meta, `X-Robots-Tag` and the `robots.txt` Disallow, and connect the booking and table forms.
