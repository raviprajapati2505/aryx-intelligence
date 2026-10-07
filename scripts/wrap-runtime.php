<?php

$root = dirname(__DIR__);
$lib = $root.'/resources/js/lib';
$gl = $root.'/resources/js/gl';
foreach ([$lib, $gl] as $dir) {
    if (! is_dir($dir) && ! mkdir($dir, 0777, true) && ! is_dir($dir)) {
        fwrite(STDERR, "Cannot create {$dir}\n");
        exit(1);
    }
}

copy($root.'/final-template/site.css', $root.'/resources/css/site.css');

$site = file_get_contents($root.'/final-template/site.js');
$site = str_replace(<<<'OLD'
    if($('.hp', form) && $('.hp', form).value) return;
    st.hidden = false;
    st.textContent = 'This preview is not connected to a mailbox, so nothing was sent. On the live site this form posts to the configured endpoint and confirms delivery.';
  });
});
$$('form.news').forEach(f=>f.addEventListener('submit', e=>{ e.preventDefault(); const b = $('button', f); b.textContent = 'Preview only'; }));
OLD
, <<<'NEW'
    if($('.hp', form) && $('.hp', form).value) return;
    const payload = {
      name: ($('#fName', form)?.value || '').trim(),
      title: ($('#fTitle', form)?.value || '').trim(),
      organization: ($('#fOrg', form)?.value || '').trim(),
      email: ($('#fEmail', form)?.value || '').trim(),
      country: ($('#fCountry', form)?.value || '').trim(),
      area: $('#fArea', form)?.value || '',
      message: ($('#fMsg', form)?.value || '').trim(),
      consent: !!(consent && consent.checked),
    };
    st.hidden = false;
    st.textContent = 'Sending…';
    fetch('/api/inquiries', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(payload),
    }).then(async (res) => {
      const body = await res.json().catch(() => ({}));
      if (!res.ok) {
        const first = body.errors ? Object.values(body.errors)[0] : null;
        throw new Error((Array.isArray(first) ? first[0] : first) || body.message || 'The message could not be sent. Please try again.');
      }
      st.textContent = body.message || 'Received. Aryx will follow up on this conversation.';
      form.reset();
    }).catch((err) => {
      st.hidden = false;
      st.textContent = err.message || 'The message could not be sent. Please try again.';
    });
  });
});
$$('form.news').forEach(f=>listen(f, 'submit', e=>{
  e.preventDefault();
  const input = $('input[type=email]', f), b = $('button', f);
  const email = (input && input.value || '').trim();
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)){ b.textContent = 'Enter an email'; later(()=>{ b.textContent = 'Subscribe'; }, 1600); return; }
  b.textContent = 'Sending';
  fetch('/api/brief-subscriptions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
    body: JSON.stringify({ email }),
  }).then(async (res) => {
    const body = await res.json().catch(() => ({}));
    if(!res.ok) throw new Error(body.message || 'Try again');
    b.textContent = 'Subscribed';
    input.value = '';
  }).catch(() => { b.textContent = 'Try again'; later(()=>{ b.textContent = 'Subscribe'; }, 1600); });
}));
NEW
, $site, $count);
if ($count !== 1) {
    fwrite(STDERR, "Contact form block was not replaced ({$count})\n");
    exit(1);
}

$site = preg_replace('/new IntersectionObserver/', 'watch', $site, -1, $ioCount);
$site = preg_replace('/(?<!remove)addEventListener\(/', '___LISTEN___', $site);
$site = preg_replace('/(\w+)\.___LISTEN___/', 'listen($1, ', $site);
$site = str_replace('___LISTEN___', 'listen(window, ', $site);
$site = preg_replace('/(?<![\w.])setTimeout\(/', 'later(', $site);
$site = str_replace('requestAnimationFrame(', 'nextFrame(', $site);

$site = preg_replace('/\(function\(\)\{\s*\'use strict\';/', <<<'JS'
export function mountSite(){
'use strict';
const cleanups = [];
const observers = [];
const timers = new Set();
const rafs = new Set();
function listen(target, type, fn, opts){
  if(!target) return;
  target.addEventListener(type, fn, opts);
  cleanups.push(() => target.removeEventListener(type, fn, opts));
}
function later(fn, ms){
  const id = setTimeout(() => { timers.delete(id); fn(); }, ms);
  timers.add(id);
  return id;
}
function nextFrame(fn){
  const id = requestAnimationFrame((t) => { rafs.delete(id); fn(t); });
  rafs.add(id);
  return id;
}
function watch(cb, opts){
  const obs = new IntersectionObserver(cb, opts);
  observers.push(obs);
  return obs;
}
JS
, $site, 1, $wrapCount);

$site = preg_replace('/\}\)\\(\\);\s*$/', <<<'JS'
  return () => {
    cleanups.forEach((fn) => fn());
    observers.forEach((obs) => obs.disconnect());
    timers.forEach((id) => clearTimeout(id));
    rafs.forEach((id) => cancelAnimationFrame(id));
  };
}
JS
, $site, 1, $endCount);

if ($wrapCount !== 1 || $endCount !== 1) {
    fwrite(STDERR, "site.js wrap failed wrap={$wrapCount} end={$endCount} io={$ioCount}\n");
    exit(1);
}
if (str_contains($site, '___LISTEN___')) {
    fwrite(STDERR, "site.js still has a listener placeholder\n");
    exit(1);
}
file_put_contents($lib.'/site.js', $site);
echo "site.js listeners wrapped, intersection observers: {$ioCount}\n";

$stage = file_get_contents($root.'/final-template/gl.js');
$stage = str_replace(
    "if(window.ResizeObserver) new ResizeObserver(build).observe($('main'));",
    "if(window.ResizeObserver && $('main')){ const ro = new ResizeObserver(build); ro.observe($('main')); observers.push(ro); }",
    $stage,
    $resizeCount
);
$stage = str_replace('if(!ok){ document.documentElement.classList.add(\'no-gl\'); return; }', 'if(!ok){ document.documentElement.classList.add(\'no-gl\'); return () => {}; }', $stage, $okCount);
$stage = preg_replace('/new IntersectionObserver/', 'watch', $stage);
$stage = preg_replace('/(?<!remove)addEventListener\(/', '___LISTEN___', $stage);
$stage = preg_replace('/(\w+)\.___LISTEN___/', 'listen($1, ', $stage);
$stage = str_replace('___LISTEN___', 'listen(window, ', $stage);
$stage = str_replace('requestAnimationFrame(frame)', 'raf = requestAnimationFrame(frame)', $stage, $rafCount);

$stage = preg_replace('/\(function\(\)\{\s*\'use strict\';\s*const body = document\.body, mode = body\.dataset\.scene;\s*if\(!mode\) return;/', <<<'JS'
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
JS
, $stage, 1, $glWrap);

$stage = preg_replace('/\}\)\\(\\);\s*$/', <<<'JS'
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
JS
, $stage, 1, $glEnd);

if ($glWrap !== 1 || $glEnd !== 1 || $resizeCount !== 1 || $okCount !== 1 || $rafCount !== 2) {
    fwrite(STDERR, "gl.js wrap failed wrap={$glWrap} end={$glEnd} resize={$resizeCount} ok={$okCount} raf={$rafCount}\n");
    exit(1);
}
file_put_contents($gl.'/stage.js', $stage);
echo "stage.js wrapped\n";
