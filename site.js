/* ===== EDIT ===== */
const CONFIG={whatsapp:'6281391779997',instagram:'https://www.instagram.com/wonfeed.official',tiktok:'https://www.tiktok.com/@wonfeed_'};
/* ================ */
const P='https://shopee.co.id/product/1250916592/';
const wa=m=>`https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(m)}`;
document.querySelectorAll('[data-wa]').forEach(a=>{a.href=wa(a.dataset.wa);a.target='_blank';a.rel='noopener'});
const ig=document.getElementById('f-ig'),tt=document.getElementById('f-tt');if(ig)ig.href=CONFIG.instagram;if(tt)tt.href=CONFIG.tiktok;
document.querySelectorAll('#mm a').forEach(a=>a.onclick=()=>document.getElementById('mm').classList.remove('open'));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.r').forEach(e=>io.observe(e));
const heroph=document.querySelector('.hero .ph');
if(heroph){(function tick(){const y=scrollY;if(y<1200)heroph.style.transform=`scale(1.06) translateY(${y*.18}px)`;requestAnimationFrame(tick)})();}
