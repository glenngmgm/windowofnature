# WON — Window of Nature website

Official site for WON Feed (Glenn's pet food & feed mill, Bandung).
Live: https://windowofnature.co.id (GitHub Pages, repo `glenngmgm/windowofnature`, branch `main`, root).
Fallback URL while DNS propagates: https://glenngmgm.github.io/windowofnature/

## What it is
- Static multi-page site, no build step. Shared `site.css` + `site.js` (CONFIG with WhatsApp/Instagram/TikTok, WA links, reveal animations, hero parallax).
- Pages: `index.html` (home: hero, stats band, four product-line tiles, story with polaroids + Hay/Feedmill tiles, pillars, B2B accordion, trust, footer), `rabbit.html` (Super & Premium), `shori.html`, `hay.html` ("Indonesia's largest importer of alfalfa"), `poultry.html`, `feedmill.html` (custom formulation, "first in Bandung"). Each product page is a full-screen hero + stats + an unboxed product showcase (large cutouts on the ivory with a ground shadow, class `.showcase .prod`) + ruled facts + Shopee banner gallery + CTA. Glenn wants products big and never boxed.
- The four product pages are generated from `gen_pages.py` (edit the PAGES dict there, then `python3 gen_pages.py`). `feedmill.html` and `index.html` are hand-written.
- English only, premium/minimal tone, image-led. No prices and no bundle/set products on the site (Glenn's call). Home links only to the four product lines + Feedmill.
- **Never claim preservative-free.** WON uses preservatives. No "preservative-free", "0% preservatives" or "no artificial colouring" anywhere (removed 26 Sep 2026; the Shopee shop description still says "tanpa bahan pengawet" — flag to Glenn if copying from Shopee).
- Every product links to its Shopee listing (`https://shopee.co.id/product/1250916592/<itemId>`).
- Design follows sarfatranch.com closely (floating pill nav, full-bleed photo hero with huge serif headline, stats band, product grid, hay photo band, tilted polaroid story, 4 pillars, animal trio, Shōri feature, white-rabbit photo band, Shopee banner rail, B2B accordion, trust band, footer) in a premium palette: deep navy #0A1F3D, ivory #F5F1E9, champagne gold #C9A961. Fonts: Instrument Serif (Sarfat's display face) + Jost, base 18px, big type throughout. Copy is English, elevated register, kept short.
- Logo: extracted from the Shopee shop banner (`img/logo-white.png`, `img/logo-navy.png`, `img/mark-*.png`).
- `photos/` — stock photos via the Openverse API + Wikimedia Commons. Hero is `hero-white.jpg` = Commons 'Blanc De Hotot.jpg' by The_only_true_editor, **CC BY-SA 4.0 — credit line is in the index/rabbit footers, keep it**. Glenn rejected the arctic hare ('rabbit or kangaroo?') and the brown lionhead. Everything else is CC0: `rabbit-white-close.jpg` (Commons CC0 'Dwarf rabbit 2014'), `rabbit-white-grass.jpg` (rawpixel), plus rabbit-dutch, rabbit-close, rabbits-hay, guinea-grass, guinea-pair, guinea-gray, rooster, chick, hay-bales, hay-band (crop), hen-freerange, hens-flock. Glenn rejected the brown lionhead hero; he wants white rabbits.

## Images
- `img/` — original Shopee listing photos (resized ≤1000px). `sec-*.jpg` are the secondary listing banners; six of them feed the gallery.
- `cut/` — background-removed product cutouts (PNG). Made locally with `rembg` (venv in the session scratchpad; models cached in `~/.u2net`). isnet-general-use for most; u2net for hay bales / white sacks (isnet eats pale objects); birefnet-general-lite is best but ~15 min/image on this Mac.
- `cut2/`, `cut3/` are gitignored scratch for cutout re-runs. `cut/cut-hay.png` is a copy of the 500 g bale cutout and `cut/bundle-pelet-hay.png` is composed from the Super bag + 500 g bale cutouts (PIL), because every model (isnet, u2net, birefnet, and their union) drops the pale wrapped bale in those two photos.
- `banners/b1..b8.jpg` — the Shopee **store decoration** banners (pulled via Glenn's logged-in Chrome; the API is signed). b2 = meadow logo poster (home), b1 = family (home B2B), b3 = hay promo (hay page), b4/b5 rabbit, b6 poultry, b7 benefits, b8 welcome lineup.
- Shop logo/banner from Shopee CDN: `img/logo-square.jpg`, `img/logo-banner.jpg`.

## Editing
- Contact config at the top of `site.js`: WhatsApp is `628112330890` (the number Glenn uses on JoynVision and Kru; he said he'd sent it, this was the only one found — confirm it is the WON line). Instagram is `wonfeed.official` (confirmed). TikTok URL is a guess.
- Product cards per page live in `gen_pages.py`. Cutouts come from `cut/`; best results come from unioning rembg masks from isnet + u2net + birefnet (`masks/`, `compose.py` in the session scratchpad; recreate if lost: mask each model with `only_mask=True`, take the max, close small holes, crop to bbox).

## Deploy
Push to `main` → GitHub Pages rebuilds in ~1 min. No CI.
Custom domain is NOT attached yet (DNS for windowofnature.co.id has no records as of 26 Sep 2026). Once the DNS records below exist, attach it with: `echo windowofnature.co.id > CNAME && git add CNAME && git commit -m "domain" && git push`, then enable Enforce HTTPS after the cert is issued.

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
