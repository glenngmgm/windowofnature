# Generates one full-screen page per product line from a shared template.
import json
WA='<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 12 12 0 0 0 4.6 4c1.7.7 2.3.8 3.1.7a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.2-.2-.2-.4-.3z"/></svg>'
NAV='<a href="rabbit.html">Rabbit</a><a href="shori.html">Shōri</a><a href="hay.html">Alfalfa Hay</a><a href="poultry.html">Poultry</a><a href="feedmill.html">The Feedmill</a>'
PAGES={
 'rabbit':dict(title='Rabbit Feed — WON',hero='photos/hero-white.jpg',pos='center 38%',eyebrow='For rabbits · Super & Premium',
   h1='Super <i>&</i> Premium',lead='Two alfalfa pellets from one mill. Super for every day. Premium, finished with olive oil, for growth and coat.',
   band=[('2','formulas'),('Alfalfa','Australian'),('0%','preservatives'),('1–20 kg','pack sizes')],
   sec='Choose your <i>pellet</i>',
   cards=[('super-1kg','Everyday · 1 kg','Super Rabbit Feed','Australian alfalfa and black seed. The daily pellet, our best seller.','27251151691'),
          ('premium-1kg','Growth & coat · 1 kg','Premium Rabbit Feed','The same alfalfa base, finished with olive oil for growth and a glossy coat.','26728134263'),
          ('super-20kg','Mill sack · 20 kg','Super Rabbit Feed','For farms and breeders, straight from the mill.','28867359695'),
          ('bundle-premium-super','Set · 1 kg + 1 kg','Super + Premium','Both formulas in one set.','44458452013')],
   facts=[('20%+','protein','Alfalfa-led nutrition for steady growth and condition.'),('Black seed','habbatussauda','Traditional immune support in every batch of Super.'),('Olive oil','in Premium','Cold-pressed, for coat shine and skin health.')],
   gal=[('../banners/b4','27251151691'),('../banners/b5','27251151691'),('../banners/b1','27251151691')],
   cta='Ready for your <i>rabbit</i>',ctap='Order today on Shopee, or write to us for farm quantities.',ctaid='27251151691',credit='Hero photograph: "Blanc De Hotot" by The_only_true_editor, Wikimedia Commons, CC BY-SA 4.0.'),
 'shori':dict(title='Shōri — WON',hero='photos/guinea-grass.jpg',pos='30% center',eyebrow='Rabbits & guinea pigs · 勝利',
   h1='Shōri, for<br><i>two companions</i>',lead="Indonesia's first dual-nutrition formula. Japanese-inspired, milled in Bandung, with the vitamin C guinea pigs cannot make themselves.",
   band=[('18%','crude protein'),('14.5%','crude fibre'),('+C','vitamin'),('2550','kcal / kg')],
   sec='The Shōri <i>range</i>',
   cards=[('shori-vitc','Daily blend · 1 kg','Shōri Daily Blend','Corn, wheat, rice bran, soybean, alfalfa and copra, with omega and vitamin C.','51350921733'),
          ('shori-hay','Set · blend + hay','Shōri + Alfalfa Hay','The daily blend with Italian hay. Complete for guinea pigs.','47754016253'),
          ('bundle-starter-pack','Set · starter','Starter Set','Shōri, pellets, hay pellets and Italian hay for a new owner.','53464985222')],
   facts=[('Vitamin C','for guinea pigs','Guinea pigs cannot synthesise it. Shōri carries it in every pellet.'),('Omega','for coat & heart','Balanced fatty acids for skin, coat and condition.'),('One bag','two animals','Rabbit and guinea pig households feed from a single blend.')],
   gal=[('sec-r','51350921733'),('sec-k','51350921733'),('sec-p','51350921733')],
   cta='Discover <i>Shōri</i>',ctap='Available on Shopee in 1 kg, or in sets with Italian hay.',ctaid='51350921733',credit=''),
 'hay':dict(title='Alfalfa Hay — WON',hero='photos/hay-bales.jpg',pos='center 55%',eyebrow='Alfalfa hay · imported from Italy',
   h1="Indonesia's largest <i>alfalfa</i> importer",lead='Sun-cured in Emilia-Romagna, above 20% protein, non-GMO. Shipped by the container and fresh with every harvest.',
   band=[('#1','importer in Indonesia'),('20%+','crude protein'),('Italy','Emilia-Romagna'),('Fresh','every harvest')],
   sec='From a pouch to a <i>bale</i>',
   cards=[('hay-italia-500g','Hay · 500 g','Alfalfa Hay Italia','The pouch, for one or two companions.','29611529965'),
          ('hay-italia-500g','Hay · 1 kg','Alfalfa Hay Italia','The family bag. Our best seller.','29611524857'),
          ('hay-italia-11kg','Hay · 11 kg','Alfalfa Hay Italia','The full bale, for many cages or livestock.','24586140324'),
          ('pellet-hay','Hay · pellets','Hay Green Pellets','Pure alfalfa, pressed. Nothing else.','44151924570')],
   facts=[('20%','protein and above','Legume hay, richer than grass hay, for growth, milk and recovery.'),('Fibre','for teeth and gut','Long, sun-cured stems keep rabbit and guinea pig digestion moving.'),('Non-GMO','dehydrated at source','Cut and dried in Italy, sealed for the journey, opened fresh in Bandung.')],
   gal=[('../banners/b3','24586140324'),('sec-c','29611524857'),('sec-d','29611529965')],
   cta='Hay by the <i>tonne</i>',ctap='Bales, pallets and full containers for farms, pet shops and distributors across Indonesia.',ctaid='29611524857',credit=''),
 'poultry':dict(title='Poultry Feed — WON',hero='photos/hen-freerange.jpg',pos='center 40%',eyebrow='For poultry · starter, grower, layer',
   h1='Super <i>Chicken</i> Feed',lead='Three formulas for every stage of the flock, pressed fresh at the mill. Rapid growth on less feed, and eggs you can count on.',
   band=[('22%','starter protein'),('17%','grower protein'),('Ω','omega layer'),('1–25 kg','pack sizes')],
   sec='Every <i>stage</i> of the flock',
   cards=[('ayam-starter','Starter · days 0–21','Super Chicken Feed Starter','22% protein for the first three weeks. Rapid growth, less feed.','43403176817'),
          ('ayam-starter-25kg','Starter · 25 kg','Chicken Starter 25 kg','The mill sack for farms. 20% protein.','56408384874'),
          ('ayam-petelur-25kg','Layer · 25 kg','Omega Layer','Omega-enriched layer formula for consistent, quality eggs.','26379151810')],
   facts=[('22%','starter protein','Lab-tested formula for the fastest, healthiest start.'),('Omega','in every layer bag','Richer yolks and steadier laying.'),('Fresh','per batch','Pressed at our mill in Bandung, never warehoused for months.')],
   gal=[('../banners/b6','43403176817'),('sec-h','43403176817'),('sec-i','43403176817')],
   cta='Feed the <i>flock</i>',ctap='Order on Shopee, or write to us for farm quantities and scheduled delivery.',ctaid='43403176817',credit=''),
}
TPL='''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{leadplain}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{leadplain}">
<meta property="og:image" content="https://windowofnature.co.id/{hero}">
<link rel="icon" href="img/mark-navy.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Epilogue:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
<style>.hero .ph{{background-image:url({hero});background-position:{pos}}}</style>
</head>
<body>
<header>
  <div class="pill">
    <a class="logo" href="./"><img src="img/logo-white.png" alt="WON Window of Nature"></a>
    <div class="links">{nav}</div>
    <div class="nav-cta">
      <a class="btn white" href="https://shopee.co.id/wonfeed_" target="_blank" rel="noopener">Shop</a>
      <a class="btn fill" href="#" data-wa="Hello WON, I would like to place an order.">Order now</a>
      <button class="burger" aria-label="menu" onclick="document.getElementById('mm').classList.toggle('open')"><span></span><span></span></button>
    </div>
  </div>
  <div class="mmenu" id="mm">{nav}<a href="https://shopee.co.id/wonfeed_" target="_blank" rel="noopener">Shop on Shopee</a></div>
</header>

<section class="hero">
  <div class="ph"></div>
  <div class="wrap">
    <span class="eyebrow r in" style="color:var(--gold-2)">{eyebrow}</span>
    <h1 class="d lg r in d1" style="margin-top:20px;max-width:12ch">{h1}</h1>
    <p class="r in d2">{lead}</p>
    <div class="cta r in d3">
      <a class="btn fill" href="https://shopee.co.id/product/1250916592/{ctaid}" target="_blank" rel="noopener">Shop now</a>
      <a class="btn white" href="./#b2b">Wholesale</a>
    </div>
  </div>
  <div class="scroll">scroll</div>
</section>

<div class="band"><div class="wrap">{band}</div></div>

<section>
  <div class="wrap">
    <div class="head center"><span class="eyebrow r">The range</span><h2 class="d lg r d1">{sec}</h2></div>
    <div class="range n{ncards}">{cards}</div>
  </div>
</section>

<section style="background:var(--ivory-2)">
  <div class="wrap">
    <div class="facts">{facts}</div>
  </div>
</section>

<section style="background:var(--navy);color:var(--ivory)">
  <div class="wrap">
    <div class="center"><span class="eyebrow r" style="color:var(--gold-2)">From the catalogue</span><h2 class="d lg r d1" style="margin-top:20px">Seen on <i>Shopee</i></h2></div>
    <div class="gal r d2">{gal}</div>
  </div>
</section>

<section id="trust">
  <div class="ph"></div>
  <div class="wrap">
    <div class="stars r">★★★★★</div>
    <h2 class="d lg r d1">{cta}</h2>
    <p class="r d2">{ctap}</p>
    <div class="acts r d3">
      <a class="btn fill" href="https://shopee.co.id/product/1250916592/{ctaid}" target="_blank" rel="noopener">Order now</a>
      <a class="btn white" href="#" data-wa="Hello WON, I have a question about {name}.">Speak with us</a>
    </div>
  </div>
</section>

<footer><div class="wrap">
  <div class="foot">
    <div><a class="logo" href="./"><img src="img/logo-white.png" alt="WON"></a><p>Window of Nature. A feed mill in Bandung, West Java, crafting small-batch, preservative-free nutrition for rabbits, guinea pigs, poultry and livestock.</p></div>
    <div><h4>Explore</h4>{navfoot}</div>
    <div><h4>Shop</h4><a href="https://shopee.co.id/wonfeed_" target="_blank" rel="noopener">Shopee</a><a href="#" id="f-tt" target="_blank" rel="noopener">TikTok Shop</a><a href="#" data-wa="Hello WON, I would like to place an order.">WhatsApp</a></div>
    <div><h4>Contact</h4><a href="#" id="f-ig" target="_blank" rel="noopener">Instagram</a><a href="mailto:hello@windowofnature.co.id">hello@windowofnature.co.id</a><a href="#">Bandung, West Java</a></div>
  </div>
  <div class="copy"><span>© 2026 WON · Window of Nature</span><span>Milled with care in Bandung</span></div>
  {credit}
</div></footer>
<a class="wa-float" href="#" data-wa="Hello WON, I have a question." aria-label="WhatsApp">{wa}</a>
<script src="site.js"></script>
</body>
</html>
'''
import re
for slug,p in PAGES.items():
    band=''.join(f'<div><b>{b}</b><span>{s}</span></div>' for b,s in p['band'])
    cards=''.join(f'<a class="card r" href="https://shopee.co.id/product/1250916592/{i}" target="_blank" rel="noopener"><div class="ph"><img src="cut/{img}.png" alt="{n}" loading="lazy"></div><div class="k">{k}</div><h3>{n}</h3><p>{d}</p><div class="go">View on Shopee <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M8 7h9v9"/></svg></div></a>' for img,k,n,d,i in p['cards'])
    facts=''.join(f'<div class="fact r"><b>{b}</b><span>{s}</span><p>{d}</p></div>' for b,s,d in p['facts'])
    gal=''.join(f'<a href="https://shopee.co.id/product/1250916592/{i}" target="_blank" rel="noopener"><img src="{g.replace("../","") if g.startswith("../") else "img/"+g}.jpg" alt="WON on Shopee" loading="lazy"></a>' for g,i in p['gal'])
    html=TPL.format(title=p['title'],leadplain=re.sub('<[^>]+>','',p['lead']),hero=p['hero'],pos=p['pos'],nav=NAV,navfoot=NAV.replace('<a ','<a class="fl" '),eyebrow=p['eyebrow'],h1=p['h1'],lead=p['lead'],ctaid=p['ctaid'],band=band,sec=p['sec'],ncards=len(p['cards']),cards=cards,facts=facts,gal=gal,cta=p['cta'],ctap=p['ctap'],name=p['title'].split(' — ')[0],credit=(f'<div class="credits">{p["credit"]}</div>' if p['credit'] else ''),wa=WA)
    open(f'{slug}.html','w').write(html); print('wrote',slug)
