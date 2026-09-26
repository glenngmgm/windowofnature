/* ===== EDIT ===== */
const CONFIG={
  whatsapp:'6281391779997',
  instagram:'https://www.instagram.com/wonfeed.official',
  tiktok:'https://www.tiktok.com/@wonfeed.official',
  ga4:'G-B29T22FFXQ' // Google Analytics 4 Measurement ID
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

/* ===== analytics with consent (UU PDP) =====
   Google Analytics loads ONLY after the visitor taps "Accept".
   The choice is stored in this browser; "Cookie settings" in the footer reopens the notice. */
window.dataLayer=window.dataLayer||[];
const CONSENT_KEY='won-consent';
function getConsent(){try{return localStorage.getItem(CONSENT_KEY)}catch(e){return null}}
function setConsent(v){try{localStorage.setItem(CONSENT_KEY,v)}catch(e){}}
function clearGACookies(){
  const host=location.hostname,parts=host.split('.');
  document.cookie.split(';').map(c=>c.split('=')[0].trim()).filter(n=>/^_ga/.test(n)).forEach(n=>{
    for(let i=0;i<parts.length;i++){const dom=parts.slice(i).join('.');document.cookie=`${n}=; Max-Age=0; path=/; domain=${dom}`;}
    document.cookie=`${n}=; Max-Age=0; path=/`;
  });
}
let gaLoaded=false;
function loadGA(){
  if(gaLoaded||!CONFIG.ga4)return;gaLoaded=true;
  window.gtag=function(){dataLayer.push(arguments)};
  gtag('consent','default',{analytics_storage:'granted',ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied'});
  gtag('js',new Date());gtag('config',CONFIG.ga4,{anonymize_ip:true});
  const s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+CONFIG.ga4;document.head.appendChild(s);
}
function track(name,params){if(gaLoaded&&window.gtag)gtag('event',name,params);}
document.addEventListener('click',e=>{
  const a=e.target.closest('a[href]');if(!a)return;const h=a.href;
  const ch=/shopee\./.test(h)?'shopee':/tiktok\.com/.test(h)?'tiktok':/wa\.me/.test(h)?'whatsapp':/instagram\.com/.test(h)?'instagram':null;
  if(ch)track('outbound_click',{channel:ch,label:(a.textContent||'').trim().slice(0,60),page:location.pathname});
});

function showNotice(){
  if(document.getElementById('cc'))return;
  const d=document.createElement('div');d.id='cc';d.setAttribute('role','dialog');d.setAttribute('aria-live','polite');d.setAttribute('aria-label','Cookie notice');
  d.innerHTML='<p>We use analytics cookies to understand how visitors use this site, so we can improve it. No advertising. <a href="privacy.html">Privacy</a></p><div class="cc-acts"><button type="button" class="btn cc-no">Decline</button><button type="button" class="btn fill cc-yes">Accept</button></div>';
  document.body.appendChild(d);document.body.classList.add('cc-open');
  requestAnimationFrame(()=>d.classList.add('show'));
  const close=v=>{setConsent(v);if(v==='denied')clearGACookies();d.classList.remove('show');document.body.classList.remove('cc-open');setTimeout(()=>d.remove(),400);if(v==='granted')loadGA();};
  d.querySelector('.cc-yes').onclick=()=>close('granted');
  d.querySelector('.cc-no').onclick=()=>close('denied');
}
document.querySelectorAll('[data-cookie-settings]').forEach(b=>b.addEventListener('click',e=>{e.preventDefault();if(getConsent()==='granted'&&gaLoaded){setConsent('');clearGACookies();location.reload();return;}showNotice();}));
const choice=getConsent();
if(choice==='granted')loadGA();
else if(choice!=='denied')setTimeout(showNotice,1200);
