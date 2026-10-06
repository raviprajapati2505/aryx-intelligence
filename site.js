/* Aryx Intelligence — shared UI behaviour */
(function(){
'use strict';
document.documentElement.classList.add('js');
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const hover = matchMedia('(hover:hover)').matches;
const $ = (s,r=document) => r.querySelector(s), $$ = (s,r=document) => [...r.querySelectorAll(s)];
const clamp = (v,a=0,b=1) => Math.min(b, Math.max(a, v));

/* headline word reveal */
$$('[data-split]').forEach(el=>{
  const words = el.textContent.trim().split(/\s+/);
  el.setAttribute('aria-label', el.textContent.trim());
  el.innerHTML = words.map((w,i)=>`<span class="w" aria-hidden="true"><i style="animation-delay:${120+i*70}ms">${w}</i></span>`).join(' ');
});

/* nav: mega menus + mobile */
function closeMegas(){ $$('[data-mega]').forEach(b=>{ b.setAttribute('aria-expanded','false'); $('#'+b.getAttribute('aria-controls')).classList.remove('open'); }); }
$$('[data-mega]').forEach(b=>b.addEventListener('click', e=>{ e.stopPropagation(); const open = b.getAttribute('aria-expanded')==='true'; closeMegas(); if(!open){ b.setAttribute('aria-expanded','true'); $('#'+b.getAttribute('aria-controls')).classList.add('open'); } }));
document.addEventListener('click', e=>{ if(!e.target.closest('.mega') && !e.target.closest('[data-mega]')) closeMegas(); });
const nav = $('#nav'), menuBtn = $('#menuBtn');
function setMenu(open){ nav.classList.toggle('menu-open', open); menuBtn.setAttribute('aria-expanded', open); menuBtn.textContent = open ? 'Close' : 'Menu'; }
menuBtn && menuBtn.addEventListener('click', ()=>setMenu(!nav.classList.contains('menu-open')));
document.addEventListener('keydown', e=>{ if(e.key==='Escape'){ closeMegas(); setMenu(false); } });

/* magnetic buttons */
if(!reduce && hover){
  $$('.btn').forEach(b=>{
    b.addEventListener('pointermove', e=>{ const r = b.getBoundingClientRect(); b.style.transform = `translate(${(e.clientX-r.left-r.width/2)/r.width*8}px,${(e.clientY-r.top-r.height/2)/r.height*6}px)`; });
    b.addEventListener('pointerleave', ()=>b.style.transform = '');
  });
}

/* reveals */
const io = new IntersectionObserver(es=>es.forEach(en=>{ if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); } }), {rootMargin:'0px 0px -8% 0px'});
$$('.rv, .test, .figbox, .cmp-row, .art').forEach(el=>{
  const p = el.parentElement; if(p && p.matches('.why-grid,.ins-grid,#capList,.outs,.related,.ind-cards,.tests,.rows')) el.style.transitionDelay = ([...p.children].indexOf(el)*70)+'ms';
  io.observe(el);
});

/* accordion rows (capabilities) */
$$('.cap-head').forEach(h=>h.addEventListener('click', ()=>{ const c = h.parentElement, open = !c.classList.contains('open'); c.classList.toggle('open', open); h.setAttribute('aria-expanded', open); }));

/* CTA pre-selection: contact.html#area-xxx or same-page form */
const AREAS = {'area-ai':'Enterprise AI','area-cyber':'Cybersecurity','area-risk':'Risk & Decision Intelligence','area-climate':'Climate Intelligence','area-digital':'Digital & Technology Transformation','area-other':'Other'};
const area = $('#fArea');
if(area && AREAS[location.hash.slice(1)]) area.value = AREAS[location.hash.slice(1)];

/* forms (honest preview behaviour) */
$$('form[data-contact]').forEach(form=>{
  form.addEventListener('submit', e=>{
    e.preventDefault();
    let ok = true, first = null;
    const st = $('[data-status]', form);
    $$('[required]', form).forEach(el=>{
      if(el.type==='checkbox') return;
      const wrap = el.closest('.f'), err = wrap && $('.err', wrap);
      const v = el.value.trim();
      let msg = '';
      if(!v) msg = 'This field is required.';
      else if(el.type==='email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) msg = 'Enter a business email, for example name@company.com.';
      else if(el.tagName==='TEXTAREA' && v.length < 10) msg = 'Describe the decision or challenge in a sentence or two.';
      if(msg){ ok=false; first = first||el; wrap.setAttribute('data-invalid',''); err.textContent = msg; el.setAttribute('aria-invalid','true'); }
      else { wrap && wrap.removeAttribute('data-invalid'); if(err) err.textContent=''; el.removeAttribute('aria-invalid'); }
    });
    const consent = $('input[type=checkbox][required]', form);
    st.hidden = true;
    if(ok && consent && !consent.checked){ ok=false; first=consent; st.hidden=false; st.textContent='Tick the privacy consent box to continue.'; }
    if(!ok){ first.focus(); return; }
    if($('.hp', form) && $('.hp', form).value) return;
    st.hidden = false;
    st.textContent = 'This preview is not connected to a mailbox, so nothing was sent. On the live site this form posts to the configured endpoint and confirms delivery.';
  });
});
$$('form.news').forEach(f=>f.addEventListener('submit', e=>{ e.preventDefault(); const b = $('button', f); b.textContent = 'Preview only'; }));

/* copy buttons */
$$('[data-copy]').forEach(b=>b.addEventListener('click', ()=>{ const t = b.dataset.copy; const done = ()=>{ b.textContent='Copied'; setTimeout(()=>b.textContent='Copy',1600); };
  if(navigator.clipboard) navigator.clipboard.writeText(t).then(done).catch(()=>{}); }));

/* ================= homepage ================= */
const disc = $('#disc');
if(disc){
  const note = $('#discNote'), notes = JSON.parse(disc.dataset.notes);
  $$('button', disc).forEach(b=>{
    const on = ()=>{ $$('button',disc).forEach(x=>x.classList.toggle('on', x===b)); note.textContent = notes[+b.dataset.path]; };
    b.addEventListener('pointerenter', on); b.addEventListener('focus', on); b.addEventListener('click', on);
    b.addEventListener('pointerleave', ()=>b.classList.remove('on'));
  });
}
const conn = $('#conn'), chain = $('#chain');
if(conn && chain){
  const lines = $$('#connLines p'), btns = $$('#stages button'), sds = $$('.sd'), fill = $('#railFill');
  let cur = -1;
  const update = ()=>{
    const vh = innerHeight, cr = conn.getBoundingClientRect(), cp = clamp(-cr.top/(conn.offsetHeight-vh));
    lines.forEach((l,i)=>l.classList.toggle('on', cp >= i*.33-.02 && cr.top < vh*.5));
    const r = chain.getBoundingClientRect(), p = clamp(-r.top/(chain.offsetHeight-vh)), st = Math.min(5, Math.round(p*5));
    fill.style.height = (p*100)+'%';
    if(st !== cur){ cur = st; btns.forEach((b,i)=> i===st ? b.setAttribute('aria-current','step') : b.removeAttribute('aria-current')); sds.forEach((d,i)=>d.classList.toggle('on', i===st)); }
  };
  addEventListener('scroll', update, {passive:true}); addEventListener('resize', update); update();
  const go = i => { const top = chain.getBoundingClientRect().top + scrollY; scrollTo({top: top + (chain.offsetHeight-innerHeight)*i/5 + 2, behavior: reduce?'auto':'smooth'}); };
  btns.forEach((b,i)=>{ b.addEventListener('click', ()=>go(i)); b.addEventListener('keydown', e=>{ const n = (e.key==='ArrowRight'||e.key==='ArrowDown') ? Math.min(5,i+1) : (e.key==='ArrowLeft'||e.key==='ArrowUp') ? Math.max(0,i-1) : -1; if(n>=0){ e.preventDefault(); btns[n].focus(); go(n); } }); });
}
/* industry tabs (homepage) */
const indList = $('#indList');
if(indList){
  const tabs = $$('[role=tab]', indList), panels = $$('[data-indpanel]');
  const show = (i, focus) => { tabs.forEach((t,j)=>{ t.setAttribute('aria-selected', j===i); t.tabIndex = j===i ? 0 : -1; }); panels.forEach((p,j)=>{ p.hidden = j!==i; if(j===i){ p.classList.remove('swap'); void p.offsetWidth; p.classList.add('swap'); } }); if(focus) tabs[i].focus(); };
  tabs.forEach((t,i)=>{ t.addEventListener('click', ()=>show(i)); t.addEventListener('mouseenter', ()=>{ if(hover && t.getAttribute('aria-selected')!=='true') show(i); }); });
  indList.addEventListener('keydown', e=>{ const i = tabs.findIndex(t=>t.getAttribute('aria-selected')==='true'); if(e.key==='ArrowDown'){ e.preventDefault(); show((i+1)%tabs.length, true); } if(e.key==='ArrowUp'){ e.preventDefault(); show((i+tabs.length-1)%tabs.length, true); } });
}

/* ================= stepper (process lists) ================= */
$$('[data-stepper]').forEach(sp=>{
  const btns = $$('.step-nav button', sp), panels = $$('[data-step]', sp), dur = 5200;
  let i = 0, timer = null, inView = false, paused = reduce;
  sp.style.setProperty('--dur', dur+'ms'); sp.style.setProperty('--n', btns.length);
  if(paused) sp.classList.add('paused');
  const show = (n, user) => {
    i = n; btns.forEach((b,j)=>{ b.setAttribute('aria-selected', j===n); b.tabIndex = j===n?0:-1; }); panels.forEach((p,j)=>p.hidden = j!==n);
    if(user){ paused = true; sp.classList.add('paused'); }
    clearTimeout(timer); if(!paused && inView){ const b = btns[n]; b.style.animation='none'; void b.offsetWidth; b.style.animation=''; timer = setTimeout(()=>show((i+1)%btns.length), dur); }
  };
  btns.forEach((b,n)=>{ b.addEventListener('click', ()=>show(n,true)); b.addEventListener('keydown', e=>{ const m = e.key==='ArrowRight' ? (n+1)%btns.length : e.key==='ArrowLeft' ? (n+btns.length-1)%btns.length : -1; if(m>=0){ e.preventDefault(); show(m,true); btns[m].focus(); } }); });
  new IntersectionObserver(es=>{ inView = es[0].isIntersecting; if(inView) show(i); else clearTimeout(timer); }, {threshold:.35}).observe(sp);
  show(0);
});

/* ================= AI: use-case prioritizer ================= */
const prio = $('[data-prio]');
if(prio){
  const grid = $('.grid2', prio), out = $('.prio-out', prio), chips = $$('.chip', prio), qs = $$('.q', grid);
  const Q = [['Quick win','High value and feasible now: fund it first.'],['Strategic bet','High value but harder to deliver: build foundations, then commit.'],['Easy but low value','Feasible but small: automate only if it frees real capacity.'],['Park it','Low value and hard: revisit when data or platforms mature.']];
  let selected = null, ghost = null, drag = null;
  const quadrant = (x,y) => (y < .5 ? (x >= .5 ? 0 : 1) : (x >= .5 ? 2 : 3));
  const place = (chip, x, y) => {
    x = clamp(x,.04,.96); y = clamp(y,.06,.94);
    let pin = $(`.pin[data-for="${chip.dataset.id}"]`, grid);
    if(!pin){ pin = document.createElement('button'); pin.type='button'; pin.className='pin'; pin.dataset.for = chip.dataset.id; pin.textContent = chip.textContent.trim(); grid.appendChild(pin); bindPin(pin, chip); }
    pin.style.left = (x*100)+'%'; pin.style.top = (y*100)+'%';
    chip.classList.add('placed');
    const q = quadrant(x,y); qs.forEach((el,j)=>el.classList.toggle('on', j===q));
    pin.setAttribute('aria-label', `${chip.textContent.trim()}: ${Q[q][0]}. Value ${Math.round((1-y)*10)} of 10, feasibility ${Math.round(x*10)} of 10.`);
    out.innerHTML = `<b>${chip.textContent.trim()}</b> lands in <b>${Q[q][0]}</b>. ${Q[q][1]}`;
  };
  const rel = e => { const r = grid.getBoundingClientRect(); return [(e.clientX-r.left)/r.width, (e.clientY-r.top)/r.height, e.clientX>=r.left && e.clientX<=r.right && e.clientY>=r.top && e.clientY<=r.bottom]; };
  function startDrag(e, chip){ drag = chip; ghost = document.createElement('div'); ghost.className='ghost'; ghost.textContent = chip.textContent.trim(); document.body.appendChild(ghost); moveGhost(e); }
  function moveGhost(e){ if(ghost){ ghost.style.left = e.clientX+'px'; ghost.style.top = e.clientY+'px'; } }
  addEventListener('pointermove', e=>{ if(drag) moveGhost(e); });
  addEventListener('pointerup', e=>{ if(!drag) return; const [x,y,inside] = rel(e); if(inside) place(drag, x, y); ghost.remove(); ghost=null; drag=null; });
  chips.forEach(c=>{
    c.addEventListener('pointerdown', e=>{ e.preventDefault(); startDrag(e, c); });
    c.addEventListener('click', ()=>{ selected = c; chips.forEach(x=>x.setAttribute('aria-pressed', x===c)); out.textContent = `Selected ${c.textContent.trim()}. Click the grid to place it, or use arrow keys after placing.`; });
    c.addEventListener('keydown', e=>{ if(e.key==='Enter' || e.key===' '){ e.preventDefault(); place(c, .5, .5); const p = $(`.pin[data-for="${c.dataset.id}"]`, grid); p && p.focus(); } });
  });
  grid.addEventListener('click', e=>{ if(e.target.closest('.pin') || !selected) return; const [x,y] = rel(e); place(selected, x, y); });
  function bindPin(pin, chip){
    pin.addEventListener('pointerdown', e=>{ e.preventDefault(); pin.setPointerCapture(e.pointerId); const mv = ev=>{ const [x,y] = rel(ev); place(chip, x, y); }; const up = ()=>{ pin.removeEventListener('pointermove', mv); pin.removeEventListener('pointerup', up); }; pin.addEventListener('pointermove', mv); pin.addEventListener('pointerup', up); });
    pin.addEventListener('keydown', e=>{ const d = {ArrowLeft:[-.05,0],ArrowRight:[.05,0],ArrowUp:[0,-.05],ArrowDown:[0,.05]}[e.key]; if(!d) return; e.preventDefault(); const x = parseFloat(pin.style.left)/100 + d[0], y = parseFloat(pin.style.top)/100 + d[1]; place(chip, x, y); });
  }
  // sample placements so the tool opens in a working state
  [[0,.8,.22],[3,.3,.3],[5,.75,.75]].forEach(([i,x,y])=>chips[i] && place(chips[i],x,y));
  out.innerHTML = 'Three example use cases are already placed. Drag the others onto the grid, or move the ones that are there.';
}

/* ================= Cyber: self-assessment ================= */
const assess = $('[data-assess]');
if(assess){
  const arc = $('.g-val', assess), lvl = $('.lvl', assess), txt = $('.g-txt', assess), ndl = $('.g-ndl', assess);
  const LV = [['1 · Initial','Security is mostly reactive. Start with ownership, asset visibility and a tested incident plan.'],['2 · Developing','Basics exist but are not connected to business priorities. Map controls to the services they protect.'],['3 · Defined','A program is in place. The next step is reporting exposure in business terms the board can weigh.'],['4 · Managed','Risk-led and measured. Focus on third parties, AI systems and recovery testing under realistic scenarios.'],['5 · Resilient','Security is managed as a business-risk discipline. Keep testing, and keep the board close to the decisions.']];
  const calc = ()=>{
    const vals = $$('input:checked', assess).map(i=>+i.value), n = $$('fieldset', assess).length;
    const score = vals.length ? vals.reduce((a,b)=>a+b,0)/(n*3) : 0;
    const L = Math.min(4, Math.floor(score*5 - 1e-9));
    const len = 251.3; arc.style.strokeDashoffset = len*(1-score);
    ndl.style.transform = `rotate(${-90 + score*180}deg)`;
    if(vals.length < n){ lvl.textContent = `${vals.length} of ${n} answered`; txt.textContent = 'Answer all five questions to see an indicative maturity level.'; }
    else { lvl.textContent = LV[Math.max(0,L)][0]; txt.textContent = LV[Math.max(0,L)][1]; }
  };
  assess.addEventListener('change', calc); calc();
}

/* ================= Risk: scenario explorer ================= */
const scen = $('[data-scen]');
if(scen){
  const EV = JSON.parse(scen.dataset.events);
  const btns = $$('.ev', scen), out = $('.scen-out', scen);
  let sel = [0,1];
  const MECH = ['Shared assets','Shared suppliers','Shared processes','Shared triggers'];
  const render = ()=>{
    btns.forEach((b,i)=>b.setAttribute('aria-pressed', sel.includes(i)));
    if(sel.length < 2){ out.innerHTML = '<p class="tool-note">Choose a second event to see how the two combine.</p>'; return; }
    const [a,b] = sel.map(i=>EV[i]);
    const svc = a.svc.filter(s=>b.svc.includes(s)), mech = MECH.map((m,i)=> a.mech.includes(i) && b.mech.includes(i));
    const hit = svc.length ? svc : [a.svc[0], b.svc[0]];
    out.innerHTML = `<div class="swapin"><p class="tag">Illustrative scenario</p><h3 style="margin-top:14px">${a.name} + ${b.name}</h3>
      <div class="blk"><span>What connects them</span><div class="mech">${MECH.map((m,i)=>`<i class="${mech[i]?'on':''}">${m}</i>`).join('')}</div></div>
      <div class="blk"><span>Services exposed together</span><p>${hit.join(', ')}</p></div>
      <div class="blk"><span>Combined picture</span><p>${a.name} ${a.verb}. In the same window, ${b.name.toLowerCase()} ${b.verb}. ${svc.length ? `Both land on ${svc.join(' and ').toLowerCase()}, so the impact compounds instead of adding up.` : 'They hit different services, but recovery competes for the same people and budget.'}</p></div>
      <div class="blk"><span>Decision leadership would need</span><p>${svc.length ? `Which of ${hit[0].toLowerCase()} must keep running, for how long it can be down, and who can authorise fallback.` : 'How to sequence recovery, and who decides when two incident teams need the same resources.'}</p></div></div>`;
  };
  btns.forEach((b,i)=>b.addEventListener('click', ()=>{ if(sel.includes(i)) sel = sel.filter(x=>x!==i); else { sel.push(i); if(sel.length>2) sel.shift(); } render(); }));
  render();
}

/* ================= Climate: pathway toggle ================= */
const clim = $('[data-climate]');
if(clim){
  const D = JSON.parse(clim.dataset.paths), tabs = $$('[role=tab]', clim), bars = $$('.bar', clim), desc = $('.path-desc', clim);
  const show = i => { tabs.forEach((t,j)=>{ t.setAttribute('aria-selected', j===i); t.tabIndex = j===i?0:-1; });
    D[i].v.forEach(([ph,tr],j)=>{ const b = bars[j]; $('.ph1',b).style.width = ph+'%'; $('.tr1',b).style.width = tr+'%'; $('.val',b).textContent = ph+tr; $('.trk',b).setAttribute('aria-label', `Physical ${ph}, transition ${tr}, total ${ph+tr} on an illustrative 0 to 100 index`); });
    desc.textContent = D[i].d; };
  tabs.forEach((t,i)=>{ t.addEventListener('click', ()=>show(i)); t.addEventListener('keydown', e=>{ const m = e.key==='ArrowRight' ? (i+1)%tabs.length : e.key==='ArrowLeft' ? (i+tabs.length-1)%tabs.length : -1; if(m>=0){ e.preventDefault(); show(m); tabs[m].focus(); } }); });
  show(0);
}

/* ================= Digital: before/after ================= */
$$('[data-ba]').forEach(ba=>{
  const r = $('input', ba); const set = ()=>ba.style.setProperty('--cut', r.value+'%');
  r.addEventListener('input', set); set();
  if(!reduce){ let t0 = null; const io2 = new IntersectionObserver(es=>{ if(es[0].isIntersecting && t0===null){ t0 = performance.now(); const anim = now=>{ const k = clamp((now-t0)/1800); r.value = 85 - 50*(1-Math.pow(1-k,3)); set(); if(k<1) requestAnimationFrame(anim); }; requestAnimationFrame(anim); } }, {threshold:.5}); io2.observe(ba); }
});

/* ================= Insights: filters ================= */
const filt = $('[data-filters]');
if(filt){
  const cards = $$('[data-cat]'), empty = $('[data-empty]');
  $$('button', filt).forEach(b=>b.addEventListener('click', ()=>{
    $$('button', filt).forEach(x=>x.setAttribute('aria-pressed', x===b));
    const c = b.dataset.f; let n = 0;
    cards.forEach(card=>{ const show = c==='all' || card.dataset.cat.split(' ').includes(c); card.hidden = !show; if(show){ n++; card.classList.remove('in'); void card.offsetWidth; card.classList.add('in'); } });
    empty.hidden = n>0;
  }));
}

/* ================= Article: progress + TOC ================= */
const art = $('.article');
if(art){
  const bar = $('.progress'), links = $$('.toc a'), heads = links.map(a=>$(a.getAttribute('href')));
  const up = ()=>{ const r = art.getBoundingClientRect(); bar.style.width = (clamp(-r.top/(r.height-innerHeight*.6))*100)+'%';
    let k = 0; heads.forEach((h,i)=>{ if(h && h.getBoundingClientRect().top < innerHeight*.3) k = i; }); links.forEach((a,i)=>a.classList.toggle('on', i===k)); };
  addEventListener('scroll', up, {passive:true}); up();
}
})();
