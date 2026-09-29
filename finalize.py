"""Post-process every page: give each local <img> its real width/height (prevents layout shift),
lazy-load everything except the header logo, and preload the hero image.
Run after editing any page:  python3 finalize.py   (gen_pages.py calls it automatically)."""
import re,glob,os,hashlib
from PIL import Image
_size={}
_hash={}
def _h(p):
    if p not in _hash: _hash[p]=hashlib.md5(open(p,'rb').read()).hexdigest()[:8] if os.path.exists(p) else None
    return _hash[p]
IMG_RE=re.compile(r'((?:cut|photos|banners|img|og|video)/[\w.-]+\.(?:webp|png|jpg|mp4))(\?v=\w+)?')
def stamp_images(s):
    return IMG_RE.sub(lambda m: m.group(1)+(f'?v={_h(m.group(1))}' if _h(m.group(1)) else ''), s)
def dims(p):
    if p not in _size:
        try: _size[p]=Image.open(p).size
        except Exception: _size[p]=None
    return _size[p]
import base64,io
from PIL import ImageFilter
_lq={}
def lqip(p):
    """~250-byte blurred preview of a photo, shown instantly while the real image downloads."""
    if p not in _lq:
        im=Image.open(p).convert('RGB'); im.thumbnail((24,24)); im=im.filter(ImageFilter.GaussianBlur(.6))
        b=io.BytesIO(); im.save(b,'WEBP',quality=45); _lq[p]='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
    return _lq[p]
LQ_RE=re.compile(r';?background:url\(data:image/webp;base64,[^)]*\) [^;"]*')
def add_lqip(tag,src):
    tag=LQ_RE.sub('',tag); tag=tag.replace(' style=""','')
    if not src.startswith('photos/') or not os.path.exists(src): return tag
    pos=re.search(r'object-position:([^;"]+)',tag); pos=pos.group(1).strip() if pos else 'center'
    bg=f'background:url({lqip(src)}) {pos}/cover no-repeat'
    if ' style="' in tag: return re.sub(r' style="([^"]*)"',lambda m:f' style="{m.group(1).rstrip(";")};{bg}"',tag,1)
    return tag[:-1].rstrip('/').rstrip()+f' style="{bg}">'
def fix_img(tag):
    m=re.search(r'src="([^"]+)"',tag)
    if not m or m.group(1).startswith('http'): return tag
    src=m.group(1).split('?')[0]; d=dims(src)
    tag=re.sub(r'\s(width|height|loading|decoding|fetchpriority)="[^"]*"','',tag)
    extra=''
    if d: extra+=f' width="{d[0]}" height="{d[1]}"'
    if 'data-eager' in tag: extra+=' fetchpriority="high" decoding="async"'
    elif 'logo' in src: extra+=' decoding="async"'
    else: extra+=' loading="lazy" decoding="async"'
    return add_lqip(tag[:-1].rstrip('/').rstrip()+extra+'>',src)
import hashlib
def asset_version(p): return hashlib.md5(open(p,'rb').read()).hexdigest()[:8]
_css=open('site.css').read(); _css2=IMG_RE.sub(lambda m: m.group(1)+(f'?v={_h(m.group(1))}' if _h(m.group(1)) else ''),_css)
if _css2!=_css: open('site.css','w').write(_css2); print('stamped site.css')
V={'site.css':asset_version('site.css'),'site.js':asset_version('site.js')}
HTTPS_UPGRADE='<script>if(location.protocol==="http:"&&/(^|\\.)windowofnature\\.co\\.id$/.test(location.hostname))location.replace("https://"+location.host+location.pathname+location.search+location.hash)</script>'
for f in glob.glob('*.html'):
    s=open(f).read(); o=s
    if 'location.protocol==="http:"' not in s:
        s=s.replace('<meta charset="UTF-8">','<meta charset="UTF-8">\n'+HTTPS_UPGRADE,1)
    s=re.sub(r'<img\b[^>]*>',lambda m:fix_img(m.group(0)),s)
    s=re.sub(r'style="background-image:url\((photos/[\w.-]+\.webp)(\?v=\w+)?\)(?:,url\(data:[^)]*\))?"',
             lambda m:f'style="background-image:url({m.group(1)}),url({lqip(m.group(1))})"',s)
    s=stamp_images(s)
    s=re.sub(r'href="site\.css(\?v=\w+)?"',f'href="site.css?v={V["site.css"]}"',s)
    s=re.sub(r'src="site\.js(\?v=\w+)?"',f'src="site.js?v={V["site.js"]}"',s)
    # preload hero background (first url(...) in the page or the default home hero)
    m=re.search(r'\.hero \.ph(?:,#trust \.ph)?\{\{?background-image:url\(([^)]+)\)',s)
    hero=m.group(1) if m else None
    if hero and 'rel="preload" as="image"' not in s:
        hero_path=hero.split('?')[0]; mob_path=hero_path.replace('.webp','-m.webp')
        hero=stamp_images(hero_path); mob=stamp_images(mob_path)
        tag=(f'<link rel="preload" as="image" href="{mob}" media="(max-width:700px)" fetchpriority="high">\n<link rel="preload" as="image" href="{hero}" media="(min-width:701px)" fetchpriority="high">' if os.path.exists(mob_path) else f'<link rel="preload" as="image" href="{hero}" fetchpriority="high">')
        s=re.sub(r'(<link rel="stylesheet" href="site\.css[^"]*">)',lambda m:tag+'\n'+m.group(1),s,count=1)
    if s!=o: open(f,'w').write(s); print('finalized',f)
