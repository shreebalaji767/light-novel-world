function newNovel(){location.href='/'}
const chapters=[...document.querySelectorAll('.chapter')],toc=[...document.querySelectorAll('.toc')];
function showChapter(i){if(i<0||i>=chapters.length)return;chapters.forEach((x,n)=>x.classList.toggle('hidden',n!==i));toc.forEach((x,n)=>x.classList.toggle('active',n===i));document.querySelector('#reading').scrollIntoView({behavior:'smooth',block:'start'})}
let size=0;function font(d){const c=document.querySelectorAll('.copy');size=Math.max(-1,Math.min(2,size+d));c.forEach(x=>{x.style.fontSize=size===-1?'.95rem':size===1?'1.22rem':size===2?'1.4rem':'1.08rem'})}
document.addEventListener('keydown',e=>{const i=toc.findIndex(x=>x.classList.contains('active'));if(e.key==='ArrowRight')showChapter(i+1);if(e.key==='ArrowLeft')showChapter(i-1);if(e.key.toLowerCase()==='n')newNovel()});
