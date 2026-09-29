# WON — Window of Nature website

Official site for WON Feed (Glenn's pet food & feed mill, Bandung).
Live: **https://windowofnature.co.id** (GitHub Pages, repo `glenngmgm/windowofnature`, branch `main`, root; `CNAME` file in repo). The old https://glenngmgm.github.io/windowofnature/ address 301-redirects to it.

## What it is
- Static multi-page site, no build step. Shared `site.css` + `site.js` (CONFIG with WhatsApp/Instagram/TikTok, WA links, reveal animations, hero parallax).
- Pages: `index.html` (home: **hero is the 60 s WON brand film** (`video/won-film-1080.mp4` for screens >900 px, `video/won-film-720.mp4` for phones, poster `video/poster*.webp`), framed 16:9, muted autoplay loop with Sound on/off + pause buttons, pauses when scrolled away, no autoplay for reduced-motion or Data Saver. 60 fps with motion blur (rendered 120 fps, blended); 1080p ≈13.5 MB, 720p ≈5.9 MB. Source project: ~/Claude/won-reel. It replaced the 'Welcome to our store' banner b8 at Glenn's request, stats band, four product-line tiles, story with polaroids + Hay/Feedmill tiles, pillars, B2B accordion, trust, footer), `rabbit.html` (Super & Premium), `shori.html`, `hay.html` ("Indonesia's largest importer of alfalfa"), `poultry.html`, `feedmill.html` (custom formulation, "first in Bandung"). Each product page is a full-screen hero + stats + an unboxed product showcase (large cutouts on the ivory with a ground shadow, class `.showcase .prod`) + ruled facts + CTA. (The "Seen on Shopee" banner gallery was removed at Glenn's request: too bleak.) Glenn wants products big and never boxed.
- The four product pages are generated from `gen_pages.py` (edit the PAGES dict there, then `python3 gen_pages.py`). `feedmill.html` and `index.html` are hand-written.
- English only, premium/minimal tone, image-led. No prices and no bundle/set products on the site (Glenn's call). Home links only to the four product lines + Feedmill.
- Poultry range is **starter and layer only (no grower feed)**; don't reintroduce grower copy even though some Shopee listing titles mention it.
- **Never claim preservative-free.** WON uses preservatives. No "preservative-free", "0% preservatives" or "no artificial colouring" anywhere (removed 26 Sep 2026; the Shopee shop description still says "tanpa bahan pengawet" — flag to Glenn if copying from Shopee).
- Every product links to its Shopee listing (`https://shopee.co.id/product/1250916592/<itemId>`).
- Design follows sarfatranch.com closely (floating pill nav, full-bleed photo hero with huge serif headline, stats band, product grid, hay photo band, tilted polaroid story, 4 pillars, animal trio, Shōri feature, white-rabbit photo band, Shopee banner rail, B2B accordion, trust band, footer) in a premium palette: deep navy #0A1F3D, ivory #F5F1E9, champagne gold #C9A961. Fonts: Instrument Serif (Sarfat's display face) + Jost, base 18px, big type throughout. Copy is English, elevated register, kept short.
- Logo: extracted from the Shopee shop banner (`img/logo-white.png`, `img/logo-navy.png`, `img/mark-*.png`).
- `photos/` — stock photos via the Openverse API + Wikimedia Commons. Hero is `hero-white.jpg` = Commons 'Blanc De Hotot.jpg' by The_only_true_editor, **CC BY-SA 4.0 — credit line is in the index/rabbit footers, keep it**. Glenn rejected the arctic hare ('rabbit or kangaroo?') and the brown lionhead. Everything else is CC0: `rabbit-white-close.jpg` (Commons CC0 'Dwarf rabbit 2014'), `rabbit-white-grass.jpg` (rawpixel), plus rabbit-dutch, rabbit-close, rabbits-hay, guinea-grass, guinea-pair, guinea-gray, rooster, chick, hay-bales, hay-band (crop), hen-freerange, hens-flock. Glenn rejected the brown lionhead hero; he wants white rabbits.

## Images
- `img/` — original Shopee listing photos (resized ≤1000px). `sec-*.jpg` are the secondary listing banners; six of them feed the gallery.
- `cut/` — background-removed product cutouts (PNG). Made locally with `rembg` (venv in the session scratchpad; models cached in `~/.u2net`). isnet-general-use for most; u2net for hay bales / white sacks (isnet eats pale objects); birefnet-general-lite is best but ~15 min/image on this Mac.
- `cut2/`, `cut3/` are gitignored scratch for cutout re-runs. `cut/cut-hay.png` is a copy of the 500 g bale cutout and `cut/bundle-pelet-hay.png` is composed from the Super bag + 500 g bale cutouts (PIL), because every model (isnet, u2net, birefnet, and their union) drops the pale wrapped bale in those two photos. `cut/hay-italia-11kg.png` is a colour mask (near-white, low-saturation pixels, largest component, holes filled) plus the model masks only inside the 11 KG badge and rabbit zones; the models alone tore the sack's bottom-left.
- Shopee banners are shown at their true proportions, never cropped (`.gal img` auto height; 2:1 banners get `.wide` and span two columns). Glenn complained when the family/Shop-now banner was cropped.
- `banners/b1..b8.jpg` — the Shopee **store decoration** banners (pulled via Glenn's logged-in Chrome; the API is signed). b2 = meadow logo poster (home), b1 = family (home B2B), b3 = hay promo (hay page), b4/b5 rabbit, b6 poultry, b7 benefits, b8 welcome lineup.
- Shop logo/banner from Shopee CDN: `img/logo-square.jpg`, `img/logo-banner.jpg`.

## Editing
- Contact config at the top of `site.js`: WhatsApp is **+62 813-9177-9997 (`6281391779997`)**, the confirmed WON line. **No email anywhere**; all contact is WhatsApp or Shopee. Instagram, TikTok and TikTok Shop are all `@wonfeed.official` (confirmed); links are hard-coded in HTML and set in `site.js` CONFIG. Trust bands offer Shopee, TikTok Shop and WhatsApp.
- Product cards per page live in `gen_pages.py`. Cutouts come from `cut/`; best results come from unioning rembg masks from isnet + u2net + birefnet (`masks/`, `compose.py` in the session scratchpad; recreate if lost: mask each model with `only_mask=True`, take the max, close small holes, crop to bbox).

## History note (26 Sep 2026)
Glenn tried a Codex redesign (commits 159d765, f2f11a4, c26b162: forest green/editorial, ten pages incl. pellets, why-alfalfa, wholesale, credits). He disliked it and asked for this design back. The commit after c26b162 restores this design and borrows only: the confirmed WhatsApp number, no-email rule, the horse/stable enquiry section on the Hay page (`photos/equestrian-pasture.jpg`, Zooey Li on Unsplash, credited under the photo), per-product colour backdrops (`tint`/`disc` in gen_pages.py), robots.txt and sitemap.xml. Codex's version stays in git history if anything else is wanted from it.


## Photo changes (26 Sep 2026)
- Glenn disliked `rabbits-hay` (brown rabbits with a bowl); it is no longer used anywhere. Replacements: `pellets-feeder` (small, realistic pellets: home Feedmill tile + feedmill hero), `hand-feeding` (feedmill 'What we tailor'). Glenn rejected big biomass-pellet photos as not looking like feed, `cattle-feed` (home Wholesale 'Farms'), `sheep-meadow`, `horses-hay`, `cattle-feed` (feedmill species strip). Credits for the CC BY-SA ones are in the index and feedmill footers. `tile-rabbit.webp` is a crop of rabbit-white-grass with the rabbit on the left so the Super/Premium bags don't cover it.
- Feedmill page names lambs, goats, cattle, horses etc. and lists species incl. crickets (WON's banner shows jangkrik feed).

## Performance & SEO setup (audit fixes, 26 Sep 2026)
- All site images are WebP (`cut/*.webp`, `photos/*.webp`, `banners/*.webp`), capped at 1000 px (cutouts) / 1800 px (photos). Originals (png/jpg) stay in the repo as sources. When adding an image, convert to WebP and reference the .webp.
- `finalize.py` adds **image version stamps** (`?v=<md5>` on every local image in HTML, including page <style> backgrounds, preloads and og:image), because Cloudflare tells browsers to cache images for 4 hours; a changed image gets a new address and shows immediately. It also adds version stamps to site.css/site.js links (`?v=<md5>`) so browsers never show stale styles after a deploy. It also stamps every `<img>` with width/height, lazy-loads all but the logo, and preloads the hero. `gen_pages.py` runs it automatically; run `python3 finalize.py` after hand-editing index.html or feedmill.html.
- Fonts are **self-hosted** in `fonts/` (Instrument Serif regular/italic + Epilogue variable, latin + latin-ext for 'ō'), declared at the top of site.css, with metric-matched fallbacks ('Instrument Serif Fallback' = Georgia at 76.5%, 'Epilogue Fallback' = Arial at 108.9%) so text doesn't jump when fonts load. The two regular latin files are preloaded on every page. No Google Fonts requests.
- Heroes have phone versions (`*-m.webp`, 900 px): product pages swap via a media query in each page's <style>, preloads carry media attributes, and the home banner uses srcset (`banners/b8-m.webp`). Hero parallax runs on scroll only.
- Share previews: `og/<page>.jpg` (1200x630). og:image/og:url, sitemap.xml and robots.txt use https://windowofnature.co.id/.
- Analytics: GA4 is ON with Measurement ID `G-B29T22FFXQ` (`CONFIG.ga4` in site.js). Outbound clicks to Shopee/TikTok/WhatsApp/Instagram are tracked as `outbound_click` with channel/label/page.
- Icons: img/favicon-32.png, img/apple-touch-icon.png, img/icon-192.png. robots.txt + sitemap.xml at root.


### Image speed (29 Sep 2026)
- Photos are sized to what they're actually displayed at (measured in Chrome at 390/1440/1920 px wide, allowing for 2x/3x screens). The species photos on the feedmill page were up to 4x too big (sheep 866KB -> 272KB). New photos: keep them no wider than about 2x their on-screen width, WebP quality ~74.
- `finalize.py` puts a ~250-byte blurred preview (inline data-URI background) on every `photos/` `<img>` and on inline `background-image:url(photos/...)` bands, so a picture area is never blank while loading. It also version-stamps image URLs inside site.css.
- Home film (site.js): the poster is picked in JS (phones never fetch the desktop poster). The film starts only after the page's images have loaded (or 3 s at most), and when scrolled away it pauses and drops an unfinished download so photos get the bandwidth. In a throttled 4G phone test, lower photos went from ~6.5 s each to under 1 s.
- Still possible (needs the Cloudflare account, which the domain seller holds): a Cache Rule "cache everything, Edge TTL 1 month" for images/video. It's safe because every asset URL is version-stamped. Right now GitHub's 10-min max-age makes Cloudflare re-check GitHub (US) for every image every 10 minutes.

## Cookie notice & privacy (UU PDP)
- Google Analytics loads ONLY after the visitor taps Accept on the cookie notice (site.js, "analytics with consent"). Choice stored in localStorage `won-consent` (granted/denied). Decline deletes any `_ga` cookies. Footer "Cookie settings" reopens the notice on every page. Outbound click events fire only when consent is granted.
- `privacy.html` explains what is collected, cookies, other services (GitHub Pages, Google Fonts, WhatsApp, Shopee/TikTok) and rights under UU No. 27/2022. Update its "Updated" date if anything changes.

## Claims (softened 26 Sep 2026, restore only with proof)
- Hay h1 was "Indonesia's largest alfalfa importer" → "Italian alfalfa, imported direct"; band "#1 importer in Indonesia" → "Direct from Italy".
- Feedmill "The first feedmill in Bandung…" → "A Bandung feedmill that formulates…"; band "1st in Bandung" → "Custom formulation".
- "Laboratory-tested" kept (it is on WON's own Shopee artwork). Review count updated to 7,000+ (Shopee showed 7RB).
- Home: the four quality pillars now live as a compact row inside the story section. Shōri page has a 7-day switching guide (from WON's own feeding banner). Nav includes Wholesale.

## Deploy
Push to `main` → GitHub Pages rebuilds in ~1 min. No CI.
Custom domain attached 28 Sep 2026. DNS is on **Cloudflare** (nameservers clay/gabriella.ns.cloudflare.com, managed by the domain seller) with the records **proxied** (orange cloud). Consequences:
- Cloudflare terminates HTTPS with its own certificate; GitHub cannot issue one behind the proxy, so **do not turn on "Enforce HTTPS" in GitHub Pages** (it would break or loop).
- http→https: every page has a tiny inline script (added by `finalize.py`) that upgrades http to https on windowofnature.co.id. The seller enabled Cloudflare **Always Use HTTPS** and SSL mode **Full** on 28 Sep 2026, so http now 301s to https at the edge; the inline script stays as a harmless fallback.
- www.windowofnature.co.id 301-redirects to the apex (GitHub does this).

### DNS records to set at the registrar for windowofnature.co.id
```
A     @    185.199.108.153
A     @    185.199.109.153
A     @    185.199.110.153
A     @    185.199.111.153
CNAME www  glenngmgm.github.io
```

## Data source
Product list scraped 26 Sep 2026 with Apify `zen-studio/shopee-product-scraper` (shopId 1250916592). Shopee's own search/decoration APIs are signed and login-walled; only `get_shop_detail`/`get_shop_base`/`get_categories` are open.
