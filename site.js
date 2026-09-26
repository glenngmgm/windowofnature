/* Progressive enhancement. Product pages, navigation and shop links work without JavaScript. */
const menuButton=document.querySelector('.menu-toggle');
const menu=document.querySelector('.mobile-menu');
function closeMenu(){if(!menuButton||!menu)return;menu.classList.remove('open');menuButton.setAttribute('aria-expanded','false');document.body.style.overflow='';}
menuButton?.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));menu.classList.toggle('open',open);document.body.style.overflow=open?'hidden':'';});
menu?.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeMenu();document.querySelectorAll('.collection-nav[open]').forEach(d=>d.open=false);menuButton?.focus();}});
document.addEventListener('click',e=>document.querySelectorAll('.collection-nav[open]').forEach(d=>{if(!d.contains(e.target))d.open=false;}));
window.matchMedia('(min-width:761px)').addEventListener('change',e=>{if(e.matches)closeMenu();});
if('IntersectionObserver' in window&&!window.matchMedia('(prefers-reduced-motion: reduce)').matches){document.documentElement.classList.add('js');const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target);}}),{threshold:.08});document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));}
const form=document.querySelector('#supply-enquiry');
form?.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;const data=new FormData(form);const message=`Hello Window of Nature, I would like to discuss alfalfa supply.\n\nName: ${data.get('name')}\nCompany / stable: ${data.get('company')}\nBusiness type: ${data.get('business')}\nDelivery city: ${data.get('city')}\nEstimated requirement: ${data.get('volume')}\nAdditional details: ${data.get('details')||'None'}`;const link=document.querySelector('#prepared-enquiry');link.href=`https://wa.me/6281391779997?text=${encodeURIComponent(message)}`;link.classList.remove('hidden');document.querySelector('.form-status').textContent='Your enquiry is ready. Open WhatsApp to review and send it.';link.focus();});
