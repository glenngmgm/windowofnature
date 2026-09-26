# WON — Window of Nature website

Official site for WON Feed (Glenn's pet food & feed mill, Bandung).
Live: https://windowofnature.co.id (GitHub Pages, repo `glenngmgm/windowofnature`, branch `main`, root).
Fallback URL while DNS propagates: https://glenngmgm.github.io/windowofnature/

## What it is
- Single static page: `index.html` (all CSS/JS inline). No build step.
- English only, premium/minimal tone, image-led. No prices on the site (Glenn's call).
- Every product links to its Shopee listing (`https://shopee.co.id/product/1250916592/<itemId>`).
- Design follows sarfatranch.com closely (floating pill nav, full-bleed photo hero with huge serif headline, stats band, product grid, hay photo band, tilted polaroid story, 4 pillars, animal trio, Shōri feature, white-rabbit photo band, Shopee banner rail, B2B accordion, trust band, footer) in a premium palette: deep navy #0A1F3D, ivory #F5F1E9, champagne gold #C9A961. Fonts: Instrument Serif (Sarfat's display face) + Jost, base 18px, big type throughout. Copy is English, elevated register, kept short.
- Logo: extracted from the Shopee shop banner (`img/logo-white.png`, `img/logo-navy.png`, `img/mark-*.png`).
- `photos/` — CC0 stock photos via the Openverse API + Wikimedia Commons (no attribution required). Hero is `hero-white.jpg` (arctic white rabbit, Commons CC0 'White rabbit on grass (Unsplash)'); `rabbit-white-close.jpg` (Commons CC0 'Dwarf rabbit 2014'), `rabbit-white-grass.jpg` (rawpixel), plus rabbit-dutch, rabbit-close, rabbits-hay, guinea-grass, guinea-pair, guinea-gray, rooster, chick, hay-bales, hay-band (crop), hen-freerange, hens-flock. Glenn rejected the brown lionhead hero; he wants white rabbits.

## Images
- `img/` — original Shopee listing photos (resized ≤1000px). `sec-*.jpg` are the secondary listing banners; six of them feed the gallery.
- `cut/` — background-removed product cutouts (PNG). Made locally with `rembg` (venv in the session scratchpad; models cached in `~/.u2net`). isnet-general-use for most; u2net for hay bales / white sacks (isnet eats pale objects); birefnet-general-lite is best but ~15 min/image on this Mac.
- `cut2/`, `cut3/` are gitignored scratch for cutout re-runs. `cut/cut-hay.png` is a copy of the 500 g bale cutout because every model drops the pale wrapped bale in the Premium Cut Hay photo.
- Shop logo/banner from Shopee CDN: `img/logo-square.jpg`, `img/logo-banner.jpg`.

## Editing
- Contact config at the bottom of `index.html`: `CONFIG.whatsapp` is still a placeholder `62XXXXXXXXXXX` — **fill in the real WA number**. Instagram/TikTok URLs are guesses (`wonfeed_`), confirm.
- Product rail: edit the `ITEMS` array (image basename in `cut/`, name, tag, Shopee itemId).
- Rabbit toggle copy: `RABBIT` object. Gallery: `GALLERY` array.

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
