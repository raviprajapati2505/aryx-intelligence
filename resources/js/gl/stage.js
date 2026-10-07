/* Aryx Intelligence — shared WebGL stage: the Aryx Structure + one scene per page */
export function mountGl(){
'use strict';
const THREE = window.THREE;
const cleanups = [];
const observers = [];
let raf = 0;
function listen(target, type, fn, opts){
  if(!target) return;
  target.addEventListener(type, fn, opts);
  cleanups.push(() => target.removeEventListener(type, fn, opts));
}
function watch(cb, opts){
  const obs = new IntersectionObserver(cb, opts);
  observers.push(obs);
  return obs;
}
const body = document.body, mode = body.dataset.scene;
if(!mode || !THREE) return () => {};
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
const clamp = (v,a=0,b=1) => Math.min(b, Math.max(a, v));
const lerp = (a,b,t) => a + (b-a)*t;
const sm = t => t*t*(3-2*t);

let ok = false;
try{ const c = document.createElement('canvas'); ok = !!(window.THREE && (c.getContext('webgl2') || c.getContext('webgl'))); }catch(e){}
if(!ok){ document.documentElement.classList.add('no-gl'); return () => {}; }

const isSmall = () => innerWidth < 860;
const canvas = $('#gl');
const renderer = new THREE.WebGLRenderer({canvas, antialias:true, alpha:true, premultipliedAlpha:false, powerPreference:'high-performance'});
renderer.outputEncoding = THREE.sRGBEncoding;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.08;
renderer.setClearColor(0x000000, 0);
const scene = new THREE.Scene();
scene.fog = new THREE.Fog(0x061310, 11, 30);
const camera = new THREE.PerspectiveCamera(30, 1, .1, 100);

/* studio environment */
const pmrem = new THREE.PMREMGenerator(renderer);
const envScene = new THREE.Scene();
envScene.add(new THREE.Mesh(new THREE.BoxGeometry(30,30,30), new THREE.MeshBasicMaterial({color:new THREE.Color(0x03110d), side:THREE.BackSide})));
const soft = (w,h,c,p) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(w,h), new THREE.MeshBasicMaterial({color:c, side:THREE.DoubleSide})); m.position.set(...p); m.lookAt(0,0,0); envScene.add(m); };
soft(6,2.4,new THREE.Color(2.6,2.8,2.8),[-6,7,8]);
soft(2.5,12,new THREE.Color(.15,1.5,1.15),[12,0,-4]);
soft(8,1.2,new THREE.Color(.9,1.1,1.05),[0,-9,6]);
soft(1.6,1.6,new THREE.Color(2.2,2.4,2.4),[7,4,10]);
scene.environment = pmrem.fromScene(envScene, .03).texture;
scene.add(new THREE.AmbientLight(0x0f2a24, .6));
const key = new THREE.DirectionalLight(0xe8fff8, 1.1); key.position.set(-4,6,8); scene.add(key);
const rim = new THREE.DirectionalLight(0x3dd6b0, 1.6); rim.position.set(6,2,-6); scene.add(rim);

const root = new THREE.Group(), obj = new THREE.Group(), space = new THREE.Group();
root.add(space); root.add(obj); scene.add(root);

/* the Aryx mark — same four blades as aryx-logo.png, in y-up space */
const P = {
  leftUp:[[-1.65,-0.982],[-0.0724,0.9659],[-0.0724,0.3059]],
  leftLow:[[-1.5695,-1.0141],[-0.0724,0.0966],[-0.0885,-0.4185]],
  rightLow:[[0.0885,0.0966],[1.5856,-1.0141],[0.0885,-0.4024]],
  rightUp:[[0.0885,1.0141],[1.65,-0.982],[0.0724,0.338],[0.0724,0.66]]
};
const mat = new THREE.MeshPhysicalMaterial({color:0x003b33, metalness:.25, roughness:.32, clearcoat:.85, clearcoatRoughness:.12, envMapIntensity:.95});
const mat2 = mat.clone(); mat2.color.set(0x004a40);
const shardMat = new THREE.MeshPhysicalMaterial({color:0x005c50, metalness:.15, roughness:.22, clearcoat:1, emissive:new THREE.Color(0x3dd6b0), emissiveIntensity:.2, envMapIntensity:1.1});
const edgeMat = new THREE.LineBasicMaterial({color:0x3dd6b0, transparent:true, opacity:.2, blending:THREE.AdditiveBlending, depthWrite:false});
const pieces = [];
function makePiece(pts, m, depth, dir, zOff){
  const s = new THREE.Shape(); s.moveTo(pts[0][0],pts[0][1]); pts.slice(1).forEach(p=>s.lineTo(p[0],p[1])); s.closePath();
  const geo = new THREE.ExtrudeGeometry(s,{depth, bevelEnabled:true, bevelThickness:.05, bevelSize:.032, bevelSegments:4, curveSegments:1});
  geo.translate(0,0,-depth/2); geo.computeVertexNormals();
  const holder = new THREE.Group(); holder.add(new THREE.Mesh(geo, m)); holder.add(new THREE.LineSegments(new THREE.EdgesGeometry(geo, 25), edgeMat));
  holder.position.z = zOff; obj.add(holder);
  pieces.push({holder, dir:new THREE.Vector3(...dir), z:zOff});
}
makePiece(P.leftUp, mat, .36, [-1,.28,.3], 0);
makePiece(P.leftLow, mat, .36, [-.82,-.55,.28], 0);
makePiece(P.rightLow, mat2, .36, [.78,-.48,.32], 0);
makePiece(P.rightUp, shardMat, .32, [.72,.52,-.22], .04);
obj.position.y = 0;

/* shared helpers */
const SIGNAL = new THREE.Color(0x3dd6b0);
const dot = (()=>{ const c=document.createElement('canvas'); c.width=c.height=64; const x=c.getContext('2d'); const gr=x.createRadialGradient(32,32,0,32,32,32); gr.addColorStop(0,'rgba(255,255,255,1)'); gr.addColorStop(.25,'rgba(255,255,255,.7)'); gr.addColorStop(1,'rgba(255,255,255,0)'); x.fillStyle=gr; x.fillRect(0,0,64,64); return new THREE.CanvasTexture(c); })();
const addMat = (color, opacity) => new THREE.MeshBasicMaterial({color, transparent:true, opacity, blending:THREE.AdditiveBlending, depthWrite:false});
function tubes(curves, parent, r=.011, glowR=.06, segs=200){
  return curves.map(cv=>{
    const core = new THREE.Mesh(new THREE.TubeGeometry(cv, segs, r, 6, false), addMat(SIGNAL,.9));
    const glow = new THREE.Mesh(new THREE.TubeGeometry(cv, segs, glowR, 8, false), addMat(SIGNAL,.08));
    parent.add(core); parent.add(glow);
    return {core, glow, n:core.geometry.index.count, ng:glow.geometry.index.count,
      set(rv, w){ core.geometry.setDrawRange(0, Math.floor(this.n*clamp(rv)/6)*6); glow.geometry.setDrawRange(0, Math.floor(this.ng*clamp(rv)/6)*6); core.material.opacity = Math.min(1,.75*w); glow.material.opacity = .07*w; }};
  });
}
const SAMP = 360;
const sampleTables = curves => curves.map(cv=>{ const a = new Float32Array(SAMP*3); for(let i=0;i<SAMP;i++){ const p=cv.getPointAt(i/(SAMP-1)); a[i*3]=p.x;a[i*3+1]=p.y;a[i*3+2]=p.z; } return a; });
function particles(N, tables, parent, spread=[26,15,12]){
  const K = Math.max(1, tables.length);
  const pos = new Float32Array(N*3), col = new Float32Array(N*3);
  const sc = new Float32Array(N*3), jit = new Float32Array(N*3), pk = new Uint8Array(N), pt = new Float32Array(N), sp = new Float32Array(N), off = new Float32Array(N);
  for(let i=0;i<N;i++){
    sc[i*3]=(Math.random()-.5)*spread[0]; sc[i*3+1]=(Math.random()-.5)*spread[1]; sc[i*3+2]=-9+Math.random()*spread[2];
    jit[i*3]=(Math.random()-.5)*.09; jit[i*3+1]=(Math.random()-.5)*.09; jit[i*3+2]=(Math.random()-.5)*.09;
    pk[i]=i%K; pt[i]=Math.random(); sp[i]=.025+Math.random()*.05; off[i]=Math.random();
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(pos,3)); geo.setAttribute('color', new THREE.BufferAttribute(col,3));
  parent.add(new THREE.Points(geo, new THREE.PointsMaterial({size:.075, map:dot, vertexColors:true, transparent:true, blending:THREE.AdditiveBlending, depthWrite:false})));
  return function(time, resolve, reveal, w, fade=1){
    for(let i=0;i<N;i++){
      const kk = pk[i], t = reduce? pt[i] : (pt[i] + time*sp[i]) % 1;
      const m = tables.length ? clamp(resolve*1.5 - off[i]*.5) : 0;
      const sx = sc[i*3] + (reduce?0:Math.sin(time*.3+i)*.25), sy = sc[i*3+1] + (reduce?0:Math.cos(time*.25+i)*.18), sz = sc[i*3+2];
      let tx=sx, ty=sy, tz=sz;
      if(tables.length){ const ii = Math.floor(t*(SAMP-1))*3, tb = tables[kk]; tx=tb[ii]+jit[i*3]; ty=tb[ii+1]+jit[i*3+1]; tz=tb[ii+2]+jit[i*3+2]; }
      pos[i*3]=sx+(tx-sx)*m; pos[i*3+1]=sy+(ty-sy)*m; pos[i*3+2]=sz+(tz-sz)*m;
      const rv = clamp(reveal*1.2 - kk*.04);
      const a = ((1-m)*.42 + m*(t <= rv+.02 ? 1:0)*.95*Math.min(1.6, w ? w[kk] : 1))*fade;
      col[i*3]=.24*a; col[i*3+1]=.84*a; col[i*3+2]=.69*a;
    }
    geo.attributes.position.needsUpdate = true; geo.attributes.color.needsUpdate = true;
  };
}
function pulses(tables, parent, per=2){
  const list = [];
  tables.forEach((tb,k)=>{ for(let j=0;j<per;j++){ const s = new THREE.Sprite(new THREE.SpriteMaterial({map:dot, color:SIGNAL, transparent:true, blending:THREE.AdditiveBlending, depthWrite:false})); s.scale.setScalar(.32); parent.add(s); list.push({s,k,o:j/per}); } });
  return function(time, reveal, w, fade=1){
    list.forEach(p=>{
      const rv = clamp(reveal*1.2 - p.k*.04), t = reduce? .7 : (time*.16 + p.o + p.k*.13) % 1;
      const ii = Math.floor(Math.min(t,rv)*(SAMP-1))*3, tb = tables[p.k];
      p.s.position.set(tb[ii],tb[ii+1],tb[ii+2]);
      p.s.material.opacity = rv > .98 ? Math.min(1,.8*(w?w[p.k]:1))*Math.sin(t*Math.PI)*fade : 0;
    });
  };
}
function triRings(parent, n=3){
  const sh = new THREE.Shape(); sh.moveTo(-0.008,0.998); sh.lineTo(-1.65,-1.014); sh.lineTo(1.65,-1.014); sh.closePath();
  const h = new THREE.Path(); h.moveTo(-0.008,0.82); h.lineTo(1.38,-0.84); h.lineTo(-1.38,-0.84); h.closePath(); sh.holes.push(h);
  const rs = [...Array(n)].map(()=>{ const m = new THREE.Mesh(new THREE.ShapeGeometry(sh), addMat(SIGNAL,0)); m.material.side = THREE.DoubleSide; m.position.z = -.3; parent.add(m); return m; });
  return function(time, amt, base=1){ rs.forEach((r,i)=>{ const f = reduce? .35 : ((time*.28 + i/n) % 1); r.scale.setScalar(base*(1 + f*1.6)); r.material.opacity = amt*(1-f)*.5; }); };
}
function sprite(parent, size=.2, color=SIGNAL){ const s = new THREE.Sprite(new THREE.SpriteMaterial({map:dot, color, transparent:true, blending:THREE.AdditiveBlending, depthWrite:false})); s.scale.setScalar(size); parent.add(s); return s; }
function legendSet(fn){ const items = $$('[data-legend] li'); items.forEach((li,i)=>li.classList.toggle('on', !!fn(i))); }

/* default sculpture state */
const BASE = {x:2.15,y:0,s:.84,objS:1,rotY:-.62,rotX:.1,camZ:9.6,explode:0,shard:.4,edge:.2,spin:1};
const mix = (a,b,t) => { const o = {}; for(const k in a){ o[k] = Array.isArray(a[k]) ? a[k].map((v,j)=>lerp(v,b[k][j],t)) : lerp(a[k], b[k] ?? a[k], t); } return o; };

/* scroll progress helpers for inner pages */
const heroEl = $('[data-hero]'), closeEl = $('[data-closing]');
function progress(){
  const vh = innerHeight;
  const hp = heroEl ? clamp(scrollY / Math.max(1, heroEl.offsetHeight*.85)) : 0;
  let cp = 0; if(closeEl){ const r = closeEl.getBoundingClientRect(); cp = clamp((vh - r.top)/(vh*.85)); }
  return {hp, cp};
}
function innerTarget(heroA, heroB, closing){
  const {hp, cp} = progress();
  const h = mix(Object.assign({},BASE,heroA), Object.assign({},BASE,heroB), sm(hp));
  return cp > 0 ? mix(h, Object.assign({},BASE,closing), sm(cp)) : h;
}
const CLOSE = {x:2.15,rotY:0,rotX:.04,camZ:9.4,explode:0,shard:.95,edge:.2,spin:.4};

/* hover link from HTML: elements with data-path highlight path i */
let hoverPath = -1;
listen(document, 'pointerover', e=>{ const el = e.target.closest('[data-path]'); hoverPath = el ? +el.dataset.path : (body.dataset.path ? +body.dataset.path : -1); });
listen(document, 'focusin', e=>{ const el = e.target.closest('[data-path]'); if(el) hoverPath = +el.dataset.path; });
if(body.dataset.path) hoverPath = +body.dataset.path;

/* ================= scenes ================= */
const SCENES = {};

/* ---------- home ---------- */
SCENES.home = function(){
  const starts = [[-4,9,-9],[-5,-9,-7],[7,8,-8],[9,-5,-4],[2,-9,-5]];
  const ends = [[-.55,.25,.15],[-.6,-.75,.2],[.35,.55,.1],[.65,-.6,.15],[0,-1.05,.25]];
  const curves = starts.map((s,i)=>{ const e = ends[i]; const m1 = [s[0]*.45+(i%2?.8:-.6), s[1]*.45, s[2]*.5+1]; const m2 = [e[0]*2.4, e[1]*1.8+(i%2?-.4:.5), 1.6];
    return new THREE.CatmullRomCurve3([new THREE.Vector3(...s),new THREE.Vector3(...m1),new THREE.Vector3(...m2),new THREE.Vector3(...e)], false, 'centripetal'); });
  const paths = tubes(curves, space, .011, .06, 220), tables = sampleTables(curves);
  const parts = particles(isSmall()?700:1500, tables, space), pul = pulses(tables, space), rings = triRings(space);
  const actC = [[-.95,0],[0,.05],[.95,0]].map(([x,z])=>new THREE.CatmullRomCurve3([new THREE.Vector3(x*.82,-1.62,z),new THREE.Vector3(x*1.1,-2.6,.3),new THREE.Vector3(x*2.2,-4.2,.2),new THREE.Vector3(x*3.6,-7,-.5)]));
  const acts = tubes(actC, space, .012, .04, 120);
  const D = o => Object.assign({}, BASE, {reveal:.2,resolve:0,w:[.6,.6,.6,.6,.6],action:0,pulse:0}, o);
  const S = {
    hero:D({}), frag:D({x:2.0,rotY:-1.0,rotX:.18,camZ:7.6,explode:1,reveal:.32,shard:.1,edge:.6,spin:0}),
    c0:D({x:2.0,rotY:-.8,camZ:8.4,explode:.75,reveal:.45,resolve:.35,shard:.2,edge:.45,spin:0}),
    c1:D({x:2.0,rotY:-.55,camZ:8.6,explode:.35,reveal:.8,resolve:.75,shard:.55,edge:.3,w:[.85,.85,.85,.85,.85],spin:0}),
    c2:D({x:2.0,rotY:-.38,camZ:8.8,explode:0,reveal:1,resolve:1,shard:.9,edge:.22,w:[1,1,1,1,1],spin:0}),
    vc:[ D({x:2.2,rotY:-.85,camZ:9.4,explode:.55,reveal:.06,shard:.05,edge:.4,w:[.5,.5,.5,.5,.5],spin:0}),
         D({x:2.2,rotY:-.65,camZ:9.0,explode:.35,reveal:.9,resolve:1,shard:.15,edge:.3,w:[.9,.9,.9,.9,.9],spin:0}),
         D({x:2.2,rotY:-.45,camZ:8.2,explode:.12,reveal:1,resolve:1,shard:1.15,edge:.25,w:[.8,.8,.8,.8,.8],spin:0}),
         D({x:2.2,rotY:-.3,camZ:8.0,reveal:1,resolve:1,shard:1.4,w:[.18,.18,1.9,.18,.18],spin:0}),
         D({x:2.2,y:.5,rotY:-.2,rotX:.24,camZ:9.6,reveal:1,resolve:.7,shard:.9,w:[.55,.55,.55,.55,.55],action:1,spin:0}),
         D({x:2.2,rotY:0,rotX:.06,camZ:9.2,reveal:1,resolve:.85,shard:1,w:[.7,.7,.7,.7,.7],action:.35,pulse:1,spin:0}) ],
    closing:D(Object.assign({},CLOSE,{reveal:1,resolve:.6,pulse:.55}))
  };
  let keys = [];
  function build(){
    const vh = innerHeight, top = el => el.getBoundingClientRect().top + scrollY;
    const frag=$('#about'), conn=$('#conn'), chain=$('#chain'), closing=$('#closing'); if(!frag) return;
    const c0 = top(conn), c1 = c0 + conn.offsetHeight - vh, v0 = top(chain), v1 = v0 + chain.offsetHeight - vh;
    keys = [{y:0,s:S.hero},{y:top(frag)-vh*.45,s:S.frag},{y:c0-vh*.1,s:S.c0},{y:c0+(c1-c0)*.5,s:S.c1},{y:c1,s:S.c2},
      ...S.vc.map((s,i)=>({y:v0+(v1-v0)*i/5,s})),{y:v1+vh*.6,s:S.vc[5]},{y:top(closing)-vh*.7,s:S.closing}].sort((a,b)=>a.y-b.y);
  }
  build(); listen(window, 'load',build); listen(window, 'resize',build);
  if(window.ResizeObserver && $('main')){ const ro = new ResizeObserver(build); ro.observe($('main')); observers.push(ro); }
  return {
    target(){ const y = scrollY; if(!keys.length || y <= keys[0].y) return S.hero;
      for(let i=0;i<keys.length-1;i++){ const a=keys[i], b=keys[i+1]; if(y < b.y) return mix(a.s, b.s, sm(clamp((y-a.y)/(b.y-a.y||1)))); }
      return keys[keys.length-1].s; },
    update(time, st){
      const w = st.w.map((v,i)=> hoverPath<0 ? v : (i===hoverPath ? 2.2 : v*.25));
      paths.forEach((p,i)=>p.set(st.reveal*1.2 - i*.04, w[i]));
      parts(time, st.resolve, st.reveal, w); pul(time, st.reveal, w);
      acts.forEach((a,i)=>a.set(st.action*1.3 - i*.1, 1)); rings(time, st.pulse);
    }
  };
};

/* ---------- Enterprise AI: decision lattice ---------- */
SCENES.ai = function(){
  const nodes = [], cols = 7, rows = 5;
  for(let r=0;r<rows;r++) for(let c=0;c<cols;c++){ nodes.push(new THREE.Vector3(-2.9 + c*1.05 + (Math.random()-.5)*.25, -2.1 + r*1.05 + (Math.random()-.5)*.2, -2.2 + Math.sin(c*.9+r)*.45)); }
  const seg = [];
  nodes.forEach((n,i)=>{ const c=i%cols, r=Math.floor(i/cols); if(c<cols-1) seg.push(n, nodes[i+1]); if(r<rows-1) seg.push(n, nodes[i+cols]); if(c<cols-1 && r<rows-1 && (i%3===0)) seg.push(n, nodes[i+cols+1]); });
  const lg = new THREE.BufferGeometry().setFromPoints(seg);
  const lines = new THREE.LineSegments(lg, new THREE.LineBasicMaterial({color:SIGNAL, transparent:true, opacity:.1, blending:THREE.AdditiveBlending, depthWrite:false}));
  space.add(lines);
  const sp = nodes.map(n=>{ const s = sprite(space,.14); s.position.copy(n); s.material.opacity=.25; return s; });
  const dec = [8, 16, 23, 31];
  const curves = dec.map((ni,k)=>{ const e = nodes[ni], s = new THREE.Vector3([-.5,.4,-.3,.5][k],[.4,-.3,.6,-.8][k],.2); const m = s.clone().lerp(e,.5); m.z += 1.1; return new THREE.QuadraticBezierCurve3(s, m, e); });
  const tb = tubes(curves, space, .012, .055, 90);
  let active = -1;
  return {
    target(){ return innerTarget({rotY:-.55}, {rotY:-.2,explode:.25,camZ:9}, CLOSE); },
    update(time, st, f){
      const P = 2.6, k = reduce ? 0 : Math.floor(time/P) % 4, ph = reduce ? 1 : (time % P)/P;
      if(k !== active){ active = k; legendSet(i=>i===k); }
      tb.forEach((t,i)=>t.set(i===k ? clamp(ph*2.2) : 0, (i===k ? 1.3 : .4)*f));
      sp.forEach((s,i)=>{ const di = dec.indexOf(i); let o = .2 + .08*Math.sin(time*1.4+i); let sc = .14;
        if(di>=0){ o = di===k ? (ph>.45 ? 1 : .35) : .45; sc = di===k && ph>.45 ? .42 + Math.sin(time*6)*.03 : .22; }
        s.material.opacity = o*f; s.scale.setScalar(sc); });
      lines.material.opacity = .1*f;
      shardMat.emissiveIntensity = (ph>.45 ? 1 : .4)*st.shard;
    }
  };
};

/* ---------- Cybersecurity: threat path intercepted by controls ---------- */
SCENES.cyber = function(){
  const cv = new THREE.CatmullRomCurve3([new THREE.Vector3(-2.6,4.2,-4),new THREE.Vector3(-2.4,2.2,-1.6),new THREE.Vector3(-1.5,.5,.3),new THREE.Vector3(-.4,-.2,.3)]);
  const track = new THREE.Mesh(new THREE.TubeGeometry(cv,160,.008,6,false), addMat(new THREE.Color(0x87968F),.4)); space.add(track);
  const planes = [.42,.6,.78].map(t=>{
    const p = cv.getPointAt(t), tan = cv.getTangentAt(t);
    const g = new THREE.Group(); g.position.copy(p); g.lookAt(p.clone().add(tan));
    const shape = new THREE.Shape(); shape.moveTo(-.7,-.55); shape.lineTo(.55,-.55); shape.lineTo(.7,-.4); shape.lineTo(.7,.55); shape.lineTo(-.7,.55); shape.closePath();
    const geo = new THREE.ShapeGeometry(shape);
    const fill = new THREE.Mesh(geo, addMat(SIGNAL,.05)); fill.material.side = THREE.DoubleSide;
    const edge = new THREE.LineLoop(new THREE.BufferGeometry().setFromPoints(shape.getPoints()), new THREE.LineBasicMaterial({color:SIGNAL, transparent:true, opacity:.5, blending:THREE.AdditiveBlending}));
    g.add(fill); g.add(edge); space.add(g); return {t, fill, edge, flash:0};
  });
  const threats = [...Array(5)].map((_,i)=>({s:sprite(space,.3,new THREE.Color(0xE6EEEA)), t:-i*.22, stop:planes[i%3].t, v:.18+Math.random()*.08}));
  let lastFlash = 0;
  return {
    target(){ return innerTarget({rotY:-.5}, {rotY:-.2,camZ:9}, CLOSE); },
    update(time, st, f, dt){
      threats.forEach(th=>{
        if(!reduce) th.t += dt*th.v;
        if(th.t >= th.stop){ const pl = planes.find(p=>p.t===th.stop); pl.flash = 1; lastFlash = time; th.t = -Math.random()*.4; th.stop = planes[Math.floor(Math.random()*3)].t; }
        const tt = clamp(th.t); const p = cv.getPointAt(tt); th.s.position.copy(p); th.s.material.opacity = th.t < 0 ? 0 : .9*f;
      });
      planes.forEach(p=>{ p.flash *= Math.pow(.04, dt); p.fill.material.opacity = (.05 + p.flash*.3)*f; p.edge.material.opacity = (.4 + p.flash*.6)*f; });
      track.material.opacity = .35*f;
      legendSet(i => i===0 || (i===1 && time - lastFlash < .5) || i===2);
      shardMat.emissiveIntensity = st.shard*(.8 + .2*Math.sin(time*2));
    }
  };
};

/* ---------- Risk: isolated nodes link into a network; one critical path ---------- */
SCENES.risk = function(){
  const N = 24, nodes = [];
  for(let i=0;i<N;i++) nodes.push(new THREE.Vector3(-3.2 + Math.random()*6, -2.6 + Math.random()*5.2, -3.4 + Math.random()*2.6));
  nodes.push(new THREE.Vector3(0,0,.1));
  const edges = [];
  nodes.forEach((a,i)=>{ if(i===N) return; const d = nodes.map((b,j)=>[j, a.distanceTo(b)]).filter(x=>x[0]!==i && x[0]!==N).sort((x,y)=>x[1]-y[1]).slice(0,2);
    d.forEach(([j])=>{ if(!edges.some(e=>(e[0]===j&&e[1]===i))) edges.push([i,j]); }); });
  edges.sort(()=>Math.random()-.5);
  const pts = []; edges.forEach(([a,b])=>{ pts.push(nodes[a], nodes[b]); });
  const lg = new THREE.BufferGeometry().setFromPoints(pts);
  const net = new THREE.LineSegments(lg, new THREE.LineBasicMaterial({color:SIGNAL, transparent:true, opacity:.28, blending:THREE.AdditiveBlending, depthWrite:false}));
  space.add(net);
  const crit = nodes.slice(0,N).map((n,i)=>[i,n]).sort((a,b)=>a[1].x-b[1].x);
  const chainIdx = [crit[0][0]]; let cur = nodes[crit[0][0]];
  for(let s=0;s<3;s++){ const next = nodes.slice(0,N).map((n,i)=>[i,n]).filter(([i,n])=>!chainIdx.includes(i) && n.x > cur.x + .6).sort((a,b)=>a[1].distanceTo(cur)-b[1].distanceTo(cur))[0]; if(!next) break; chainIdx.push(next[0]); cur = next[1]; }
  const chainPts = chainIdx.map(i=>nodes[i]).concat([nodes[N]]);
  const cc = new THREE.CatmullRomCurve3(chainPts, false, 'centripetal');
  const critT = tubes([cc], space, .016, .07, 160)[0];
  const sp = nodes.slice(0,N).map((n,i)=>{ const s = sprite(space,.2); s.position.copy(n); return s; });
  return {
    target(){ return innerTarget({rotY:-.55,explode:.3}, {rotY:-.25,explode:0,camZ:9}, CLOSE); },
    update(time, st, f){
      const {hp} = progress();
      const rev = clamp(.12 + hp*1.3 + (reduce ? .6 : Math.min(time/7, .45)));
      lg.setDrawRange(0, Math.floor(edges.length*rev)*2);
      const cr = clamp(rev*1.6 - .6);
      critT.set(cr, 1.6*f); net.material.opacity = .26*f;
      sp.forEach((s,i)=>{ const onC = chainIdx.includes(i); s.material.opacity = (onC && cr>0 ? .95 : .35 + .1*Math.sin(time+i))*f; s.scale.setScalar(onC && cr>0 ? .34 : .2); });
      legendSet(i => i===0 || (i===1 && rev>.5) || (i===2 && cr>.5));
      shardMat.emissiveIntensity = st.shard*(.4 + cr*.8);
    }
  };
};

/* ---------- Climate: data layers collapse into one exposure view ---------- */
SCENES.climate = function(){
  const layers = [0xF6F8F7, 0x2FBF9A, 0x3DD6B0].map((c,li)=>{
    const W=48, H=24, n=W*H, pos=new Float32Array(n*3), base=[];
    for(let y=0;y<H;y++) for(let x=0;x<W;x++){ base.push([(x/(W-1)-.5)*7, (y/(H-1)-.5)*3.4]); }
    const geo = new THREE.BufferGeometry(); geo.setAttribute('position', new THREE.BufferAttribute(pos,3));
    const m = new THREE.Points(geo, new THREE.PointsMaterial({color:c, size:.055, map:dot, transparent:true, opacity:.8, blending:THREE.AdditiveBlending, depthWrite:false}));
    const grp = new THREE.Group(); grp.add(m); grp.rotation.x = -1.12; grp.position.set(-.6, 0, -2.2); space.add(grp);
    return {grp, geo, pos, base, li, mat:m.material};
  });
  return {
    target(){ return innerTarget({rotY:-.5,x:2.3}, {rotY:-.2,x:2.3,camZ:9.2}, CLOSE); },
    update(time, st, f){
      const {hp} = progress(); const col = sm(clamp(hp*1.7));
      layers.forEach(L=>{
        const off = [1.35,0,-1.35][L.li]*(1-col);
        L.grp.position.y = off;
        for(let i=0;i<L.base.length;i++){ const [x,y] = L.base[i];
          const a = [Math.sin(x*.9+time*.4)*.25+Math.cos(y*1.6)*.15, Math.sin(x*1.6-time*.3+y)*.18, Math.cos(x*.6+y*1.2+time*.5)*.22][L.li];
          const u = (Math.sin(x*.8+time*.35)+Math.cos(y*1.1-time*.2))*.16;
          L.pos[i*3]=x; L.pos[i*3+1]=y; L.pos[i*3+2]=lerp(a,u,col); }
        L.geo.attributes.position.needsUpdate = true;
        L.mat.opacity = (col>.6 ? (L.li===2 ? .95 : .15) : .75)*f;
      });
      legendSet(i => col>.6 ? i===3 : i<3);
      shardMat.emissiveIntensity = st.shard*(.4 + col*.8);
    }
  };
};

/* ---------- Digital: tangled architecture planes settle into a clean stack ---------- */
SCENES.digital = function(){
  const slabs = [...Array(5)].map((_,i)=>{
    const geo = new THREE.BoxGeometry(3.6,.05,2.1);
    const m = new THREE.Mesh(geo, new THREE.MeshPhysicalMaterial({color:0x00594F, transparent:true, opacity:.32, roughness:.3, metalness:.1, envMapIntensity:.8, depthWrite:false}));
    const e = new THREE.LineSegments(new THREE.EdgesGeometry(geo), new THREE.LineBasicMaterial({color:SIGNAL, transparent:true, opacity:.6, blending:THREE.AdditiveBlending}));
    const gr = new THREE.Group(); gr.add(m); gr.add(e); space.add(gr);
    return {gr, e, y:-1.7 + i*.85, rx:(Math.random()-.5)*.9, ry:(Math.random()-.5)*1.2, rz:(Math.random()-.5)*.5, dx:(Math.random()-.5)*1.8, dz:(Math.random()-.5)*1.2};
  });
  const conn = new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints([...Array(4)].flatMap((_,i)=>[[-1.5,-.8],[1.5,-.8],[-1.5,.8],[1.5,.8]].flatMap(([x,z])=>[new THREE.Vector3(x,-1.7+i*.85,z),new THREE.Vector3(x,-1.7+(i+1)*.85,z)]))), new THREE.LineBasicMaterial({color:SIGNAL, transparent:true, opacity:0, blending:THREE.AdditiveBlending}));
  const stack = new THREE.Group(); slabs.forEach(s=>stack.add(s.gr)); stack.add(conn); stack.position.set(.2,0,-3); stack.scale.setScalar(.9); stack.rotation.set(.28,-.5,0); space.add(stack);
  return {
    target(){ return innerTarget({rotY:-.5,x:2.3}, {rotY:-.2,x:2.3,camZ:9.2}, CLOSE); },
    update(time, st, f){
      const {hp} = progress();
      const s = sm(clamp(hp*1.6 + (reduce ? 1 : (Math.sin(time*.45)*.5+.5)*.5)));
      slabs.forEach(b=>{ const k = 1-s; b.gr.position.set(b.dx*k, b.y, b.dz*k); b.gr.rotation.set(b.rx*k, b.ry*k, b.rz*k); b.e.material.opacity = (.35 + s*.45)*f; });
      conn.material.opacity = clamp(s*1.6-.8)*.7*f;
      legendSet(i => s>.75 ? i===1 : i===0);
      shardMat.emissiveIntensity = st.shard*(.4 + s*.7);
    }
  };
};

/* ---------- About & Contact: Doha → GCC cartographic field ---------- */
function mapScene(zoomFrom, zoomTo, contact){
  return function(){
    const C = [['Doha',25.29,51.53],['Riyadh',24.71,46.68],['Dubai',25.20,55.27],['Abu Dhabi',24.45,54.38],['Kuwait City',29.38,47.98],['Muscat',23.59,58.41],['Manama',26.23,50.59],['Jeddah',21.49,39.19]];
    const S = .34, xy = (lat,lon) => new THREE.Vector3((lon-51.53)*S, (lat-25.29)*S, 0);
    const map = new THREE.Group(); space.add(map);
    const grat = [];
    for(let lon=34; lon<=64; lon+=2){ grat.push(xy(14,lon), xy(34,lon)); }
    for(let lat=14; lat<=34; lat+=2){ grat.push(xy(lat,34), xy(lat,64)); }
    const gl = new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints(grat), new THREE.LineBasicMaterial({color:SIGNAL, transparent:true, opacity:.12, blending:THREE.AdditiveBlending, depthWrite:false}));
    map.add(gl);
    const pts = C.map(([n,la,lo],i)=>{ const s = sprite(map, i===0 ? .5 : .24); s.position.copy(xy(la,lo)); return s; });
    const arcs = C.slice(1).map(([n,la,lo])=>{ const e = xy(la,lo), s = xy(25.29,51.53); const m = s.clone().lerp(e,.5); m.z = .4 + s.distanceTo(e)*.25; return new THREE.QuadraticBezierCurve3(s,m,e); });
    const at = tubes(arcs, map, .01, .045, 80);
    const rings = triRings(map, 3);
    map.rotation.x = -.62;
    return {
      target(){ return innerTarget(contact ? {x:.75,y:-2.3,objS:.26,rotY:-.4,camZ:9.6} : {x:1.9,rotY:-.4}, contact ? {x:1.9,objS:.26,rotY:-.1,camZ:10} : {x:1.9,rotY:-.1,camZ:10}, contact ? Object.assign({},CLOSE,{objS:.26}) : CLOSE); },
      update(time, st, f){
        const {hp} = progress(); const z = lerp(zoomFrom, zoomTo, sm(hp));
        map.scale.setScalar(z); map.position.y = -.25;
        const P = 1.4, k = reduce ? -1 : Math.floor(time/P) % arcs.length, ph = (time % P)/P;
        at.forEach((a,i)=>a.set(reduce ? 1 : (i===k ? clamp(ph*1.6) : (i<k ? 1 : (time > P*arcs.length ? 1 : 0))), (i===k ? .95 : .45)*f));
        pts.forEach((s,i)=>{ s.material.opacity = (i===0 ? .95 : .55 + (i===k+1 && ph>.6 ? .4 : 0))*f; s.scale.setScalar((i===0 ? .34 : .2)/z*1.3); });
        gl.material.opacity = .13*f;
        rings(time, contact ? .7*f : .45*f, .16/z);
        shardMat.emissiveIntensity = 1;
      }
    };
  };
}
SCENES.about = mapScene(2.2, 1.05, false);
SCENES.contact = mapScene(1.8, 1.6, true);

/* ---------- Industries: nine sector paths converge on the structure ---------- */
SCENES.industries = function(){
  const curves = [...Array(9)].map((_,i)=>{ const a = (110 + i*17.5)*Math.PI/180; const s = new THREE.Vector3(Math.cos(a)*8, Math.sin(a)*5.2, -5 + (i%3)*1.4); const e = new THREE.Vector3(Math.cos(a)*.55, Math.sin(a)*.6 - .2, .2);
    const m1 = s.clone().multiplyScalar(.55); m1.z = 0; const m2 = e.clone().multiplyScalar(2.6); m2.z = 1.4;
    return new THREE.CatmullRomCurve3([s,m1,m2,e], false, 'centripetal'); });
  const paths = tubes(curves, space, .01, .05, 180), tables = sampleTables(curves);
  const parts = particles(isSmall()?500:1000, tables, space), pul = pulses(tables, space, 1);
  return {
    target(){ return innerTarget({rotY:-.5}, {rotY:-.2,camZ:9}, CLOSE); },
    update(time, st, f){
      const {hp} = progress(); const rv = clamp(.55 + hp + (reduce?1:Math.min(time/4,.45)));
      const w = [...Array(9)].map((_,i)=> hoverPath<0 ? .75 : (i===hoverPath ? 2.3 : .2));
      paths.forEach((p,i)=>p.set(rv*1.2 - i*.03, w[i]*f));
      parts(time, 1, rv, w, f); pul(time, rv, w, f);
      shardMat.emissiveIntensity = st.shard*(hoverPath<0 ? .7 : 1.3);
    }
  };
};

/* ---------- Insights: calm signal field ---------- */
SCENES.insights = function(){
  const parts = particles(isSmall()?500:1100, [], space, [24,14,12]);
  const rings = triRings(space, 2);
  return {
    target(){ return innerTarget({rotY:-.5}, {rotY:-.15,camZ:9.2}, CLOSE); },
    update(time, st, f){ parts(time, 0, 0, null, f); rings(time, .35*f); shardMat.emissiveIntensity = st.shard*(.8+.2*Math.sin(time*1.5)); }
  };
};

/* ================= run ================= */
const S = (SCENES[mode] || SCENES.insights)();
const cur = JSON.parse(JSON.stringify(S.target()));

let mx=0, my=0, userRot=0, userVel=0, dragging=false, lastX=0;
listen(window, 'pointermove', e=>{ mx = e.clientX/innerWidth*2-1; my = e.clientY/innerHeight*2-1; }, {passive:true});
$$('[data-drag]').forEach(z=>{
  listen(z, 'pointerdown', e=>{ dragging=true; lastX=e.clientX; z.setPointerCapture(e.pointerId); });
  listen(z, 'pointermove', e=>{ if(!dragging) return; const dx=e.clientX-lastX; lastX=e.clientX; userVel=dx*.006; userRot+=userVel; });
  const end = ()=>{ dragging=false; }; listen(z, 'pointerup',end); listen(z, 'pointercancel',end);
});

const visSet = new Set();
const vio = watch(es=>es.forEach(en=>en.isIntersecting ? visSet.add(en.target) : visSet.delete(en.target)));
$$('.gl-through').forEach(el=>vio.observe(el));
let tabHidden = document.hidden, last = performance.now(), time = 0;
listen(document, 'visibilitychange', ()=>{ tabHidden = document.hidden; last = performance.now(); });

function resize(){
  renderer.setPixelRatio(Math.min(devicePixelRatio, isSmall()?1.5:2));
  renderer.setSize(innerWidth, innerHeight, false);
  camera.aspect = innerWidth/innerHeight; camera.updateProjectionMatrix();
}
listen(window, 'resize', resize); resize();

function frame(now){
  raf = requestAnimationFrame(frame);
  const dt = Math.min(.05, (now-last)/1000); last = now;
  if(tabHidden || visSet.size===0) return;
  time += reduce ? 0 : dt;
  const T = S.target(), k = reduce ? 1 : 1 - Math.exp(-dt*3.2);
  for(const key in T){ if(Array.isArray(T[key])) cur[key] = (cur[key]||T[key]).map((v,j)=>lerp(v,T[key][j],k)); else cur[key] = lerp(cur[key] ?? T[key], T[key], k); }
  const small = isSmall(), aspect = innerWidth/innerHeight;
  const xs = small ? 0 : Math.min(1, aspect/1.6)*(aspect>1.9?1.15:1);
  root.position.set(cur.x*xs, cur.y + (small ? 1.75 : 0), 0);
  root.scale.setScalar(cur.s*(small ? .58 : 1));
  obj.scale.setScalar(cur.objS ?? 1);
  camera.position.set(0, .15, cur.camZ + (small ? 1.2 : 0)); camera.lookAt(0, small ? .35 : 0, 0);
  if(!dragging){ userVel *= .92; userRot += userVel; userRot *= .985; }
  const idle = reduce ? 0 : Math.sin(time*.35)*.06*(cur.spin ?? 1);
  obj.rotation.y = lerp(obj.rotation.y, cur.rotY + userRot + idle + (reduce?0:mx*.22), reduce?1:.08);
  obj.rotation.x = lerp(obj.rotation.x, cur.rotX + (reduce?0:my*.1), reduce?1:.08);
  space.rotation.y = lerp(space.rotation.y, reduce?0:mx*.06, .05);
  space.rotation.x = lerp(space.rotation.x, reduce?0:my*.03, .05);
  const breathe = reduce ? 0 : Math.sin(time*.8)*.015;
  pieces.forEach((p,i)=>{ const e = cur.explode; p.holder.position.set(p.dir.x*e*.62, p.dir.y*e*.62, p.z + p.dir.z*e*.9 + breathe*(i===3?2:0)); p.holder.rotation.z = p.dir.x*e*.07; p.holder.rotation.y = p.dir.z*e*.12; });
  edgeMat.opacity = Math.min(.9, cur.edge);
  shardMat.emissiveIntensity = cur.shard*(reduce ? 1 : .85 + Math.sin(time*2.2)*.15);
  const {cp} = progress(); const f = mode==='home' ? 1 : 1 - cp*.75;
  S.update(time, cur, f, dt);
  renderer.render(scene, camera);
}
raf = requestAnimationFrame(frame);
  return () => {
    cancelAnimationFrame(raf);
    cleanups.forEach((fn) => fn());
    observers.forEach((obs) => obs.disconnect());
    try {
      scene.traverse((obj) => {
        if (obj.geometry) obj.geometry.dispose();
        const mats = obj.material ? [].concat(obj.material) : [];
        mats.forEach((material) => {
          if (material.map) material.map.dispose();
          material.dispose();
        });
      });
      if (scene.environment && scene.environment.dispose) scene.environment.dispose();
      pmrem.dispose();
      renderer.dispose();
      renderer.forceContextLoss();
    } catch (e) {}
  };
}