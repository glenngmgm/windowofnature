"""Post-process every page: give each local <img> its real width/height (prevents layout shift),
lazy-load everything except the header logo, and preload the hero image.
Run after editing any page:  python3 finalize.py   (gen_pages.py calls it automatically)."""
import re,glob,os
from PIL import Image
_size={}
def dims(p):
    if p not in _size:
        try: _size[p]=Image.open(p).size
        except Exception: _size[p]=None
    return _size[p]
def fix_img(tag):
    m=re.search(r'src="([^"]+)"',tag)
    if not m or m.group(1).startswith('http'): return tag
    src=m.group(1); d=dims(src)
    tag=re.sub(r'\s(width|height|loading|decoding|fetchpriority)="[^"]*"','',tag)
    extra=''
    if d: extra+=f' width="{d[0]}" height="{d[1]}"'
    if 'logo' in src: extra+=' decoding="async"'
    else: extra+=' loading="lazy" decoding="async"'
    return tag[:-1].rstrip('/').rstrip()+extra+'>'
for f in glob.glob('*.html'):
    s=open(f).read(); o=s
    s=re.sub(r'<img\b[^>]*>',lambda m:fix_img(m.group(0)),s)
    # preload hero background (first url(...) in the page or the default home hero)
    m=re.search(r'\.hero \.ph\{\{?background-image:url\(([^)]+)\)',s)
    hero=m.group(1) if m else ('photos/hero-white.webp' if f=='index.html' else None)
    if hero and 'rel="preload" as="image"' not in s:
        s=s.replace('<link rel="stylesheet" href="site.css">',f'<link rel="preload" as="image" href="{hero}" fetchpriority="high">\n<link rel="stylesheet" href="site.css">',1)
    if s!=o: open(f,'w').write(s); print('finalized',f)
