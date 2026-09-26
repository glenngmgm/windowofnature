/* ===== EDIT ===== */
const CONFIG={
  whatsapp:'6281391779997',
  instagram:'https://www.instagram.com/wonfeed.official',
  tiktok:'https://www.tiktok.com/@wonfeed.official',
  ga4:'' // paste a Google Analytics 4 Measurement ID here (looks like G-XXXXXXX) to switch tracking on
};
/* ================ */
const P='https://shopee.co.id/product/1250916592/';
const wa=m=>`https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(m)}`;
document.querySelectorAll('[data-wa]').forEach(a=>{a.href=wa(a.dataset.wa);a.target='_blank';a.rel='noopener'});
const ig=document.getElementById('f-ig'),tt=document.getElementById('f-tt');if(ig)ig.href=CONFIG.instagram;if(tt)tt.href=CONFIG.tiktok;
document.querySelectorAll('#mm a').forEach(a=>a.onclick=()=>document.getElementById('mm').classList.remove('open'));

/* reveal on scroll */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.r').forEach(e=>io.observe(e));

/* hero parallax: only recalculates while scrolling, and not for reduced-motion users */
const heroph=document.querySelector('.hero .ph');
if(heroph&&!matchMedia('(prefers-reduced-motion: reduce)').matches){
  let ticking=false;
  addEventListener('scroll',()=>{
    if(ticking)return;ticking=true;
    requestAnimationFrame(()=>{const y=scrollY;if(y<1200)heroph.style.transform=`scale(1.06) translateY(${y*.18}px)`;ticking=false;});
  },{passive:true});
}

/* analytics: loads only when CONFIG.ga4 is set; records clicks to Shopee, TikTok, WhatsApp and Instagram */
window.dataLayer=window.dataLayer||[];
function track(name,params){window.dataLayer.push({event:name,...params});if(window.gtag)gtag('event',name,params);}
if(CONFIG.ga4){
  const s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+CONFIG.ga4;document.head.appendChild(s);
  window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config',CONFIG.ga4);
}
document.addEventListener('click',e=>{
  const a=e.target.closest('a[href]');if(!a)return;const h=a.href;
  const ch=/shopee\./.test(h)?'shopee':/tiktok\.com/.test(h)?'tiktok':/wa\.me/.test(h)?'whatsapp':/instagram\.com/.test(h)?'instagram':null;
  if(ch)track('outbound_click',{channel:ch,label:(a.textContent||'').trim().slice(0,60),page:location.pathname});
});
