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
    if 'data-eager' in tag: extra+=' fetchpriority="high" decoding="async"'
    elif 'logo' in src: extra+=' decoding="async"'
    else: extra+=' loading="lazy" decoding="async"'
    return tag[:-1].rstrip('/').rstrip()+extra+'>'
import hashlib
def asset_version(p): return hashlib.md5(open(p,'rb').read()).hexdigest()[:8]
V={'site.css':asset_version('site.css'),'site.js':asset_version('site.js')}
HTTPS_UPGRADE='<script>if(location.protocol==="http:"&&/(^|\\.)windowofnature\\.co\\.id$/.test(location.hostname))location.replace("https://"+location.host+location.pathname+location.search+location.hash)</script>'
for f in glob.glob('*.html'):
    s=open(f).read(); o=s
    if 'location.protocol==="http:"' not in s:
        s=s.replace('<meta charset="UTF-8">','<meta charset="UTF-8">\n'+HTTPS_UPGRADE,1)
    s=re.sub(r'<img\b[^>]*>',lambda m:fix_img(m.group(0)),s)
    s=re.sub(r'href="site\.css(\?v=\w+)?"',f'href="site.css?v={V["site.css"]}"',s)
    s=re.sub(r'src="site\.js(\?v=\w+)?"',f'src="site.js?v={V["site.js"]}"',s)
    # preload hero background (first url(...) in the page or the default home hero)
    m=re.search(r'\.hero \.ph(?:,#trust \.ph)?\{\{?background-image:url\(([^)]+)\)',s)
    hero=m.group(1) if m else None
    if hero and 'rel="preload" as="image"' not in s:
        mob=hero.replace('.webp','-m.webp')
        tag=(f'<link rel="preload" as="image" href="{mob}" media="(max-width:700px)" fetchpriority="high">\n<link rel="preload" as="image" href="{hero}" media="(min-width:701px)" fetchpriority="high">' if os.path.exists(mob) else f'<link rel="preload" as="image" href="{hero}" fetchpriority="high">')
        s=re.sub(r'(<link rel="stylesheet" href="site\.css[^"]*">)',lambda m:tag+'\n'+m.group(1),s,count=1)
    if s!=o: open(f,'w').write(s); print('finalized',f)
