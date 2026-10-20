(() => {
  const root = document.documentElement;
  root.classList.remove('no-js');
  root.classList.add('js');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) root.classList.add('reduce');

  // Header background once the hero is scrolled past; mobile quote bar after the hero
  const header = document.querySelector('.site-header');
  const bar = document.querySelector('.quote-bar');
  const hero = document.querySelector('.hero');
  const onScroll = () => {
    header.classList.toggle('is-scrolled', window.scrollY > 24);
    if (bar && hero) bar.classList.toggle('is-on', window.scrollY > hero.offsetHeight * 0.7);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Hero: cycle the five sizes, ruler extends to each length
  const heroImgs = [...document.querySelectorAll('.hero-trailers img')];
  const heroSize = document.querySelector('.hero-readout .size');
  const heroFill = document.querySelector('.ruler-mini span');
  let heroIndex = 0;
  const showHero = (i) => {
    const prev = heroImgs[heroIndex];
    const next = heroImgs[i];
    if (prev !== next) {
      prev.classList.remove('is-active');
      prev.classList.add('is-leaving');
      setTimeout(() => prev.classList.remove('is-leaving'), 900);
    }
    next.classList.add('is-active');
    heroSize.textContent = next.dataset.label;
    heroFill.style.transform = `scaleX(${Number(next.dataset.len) / 20})`;
    heroIndex = i;
  };
  if (heroImgs.length) {
    showHero(0);
    if (!reduce) {
      let timer = setInterval(() => showHero((heroIndex + 1) % heroImgs.length), 3400);
      document.addEventListener('visibilitychange', () => {
        clearInterval(timer);
        if (!document.hidden) timer = setInterval(() => showHero((heroIndex + 1) % heroImgs.length), 3400);
      });
    }
  }

  // Size selector: accessible tabs
  const tabs = [...document.querySelectorAll('.size-tabs [role="tab"]')];
  const panels = tabs.map((t) => document.getElementById(t.getAttribute('aria-controls')));
  const select = (i, focus) => {
    tabs.forEach((t, j) => {
      const on = i === j;
      t.setAttribute('aria-selected', on);
      t.tabIndex = on ? 0 : -1;
      panels[j].hidden = !on;
      panels[j].classList.remove('is-entering');
    });
    if (!reduce) { void panels[i].offsetWidth; panels[i].classList.add('is-entering'); }
    if (focus) tabs[i].focus();
  };
  tabs.forEach((t, i) => {
    t.addEventListener('click', () => select(i));
    t.addEventListener('keydown', (e) => {
      const k = e.key;
      if (k === 'ArrowRight' || k === 'ArrowLeft' || k === 'Home' || k === 'End') {
        e.preventDefault();
        const n = k === 'Home' ? 0 : k === 'End' ? tabs.length - 1 : (i + (k === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
        select(n, true);
      }
    });
  });
  if (tabs.length) {
    tabs.forEach((t, j) => { panels[j].hidden = j !== 0; t.tabIndex = j === 0 ? 0 : -1; });
  }
  // "Custom" tab inside the selector jumps to the custom section
  document.querySelectorAll('[data-jump]').forEach((b) => b.addEventListener('click', () => {
    document.querySelector(b.dataset.jump).scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
  }));

  // About statement: words light up as it scrolls through the viewport
  const statement = document.querySelector('.statement');
  if (statement && !reduce) {
    const words = [];
    const wrap = (node) => {
      [...node.childNodes].forEach((n) => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            const s = document.createElement('span');
            s.className = 'w';
            s.textContent = part;
            words.push(s);
            frag.appendChild(s);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1) wrap(n);
      });
    };
    wrap(statement);
    const light = () => {
      const r = statement.getBoundingClientRect();
      const vh = window.innerHeight;
      const p = Math.min(1, Math.max(0, (vh * 0.85 - r.top) / (r.height + vh * 0.35)));
      const lit = Math.round(p * words.length);
      words.forEach((w, i) => w.classList.toggle('on', i < lit));
    };
    window.addEventListener('scroll', light, { passive: true });
    light();
  }

  // Recent work rail buttons
  const rail = document.querySelector('.work-rail');
  document.querySelectorAll('[data-rail]').forEach((b) => b.addEventListener('click', () => {
    const step = rail.firstElementChild.getBoundingClientRect().width + 12;
    rail.scrollBy({ left: Number(b.dataset.rail) * step, behavior: reduce ? 'auto' : 'smooth' });
  }));

  // Contact form: validate, then hand the request to WhatsApp (static preview has no backend)
  const form = document.querySelector('.form');
  if (form) {
    const msg = form.dataset;
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let first = null;
      form.querySelectorAll('[required]').forEach((el) => {
        const ok = el.type === 'checkbox' ? el.checked : el.value.trim() !== '' && el.checkValidity();
        el.setAttribute('aria-invalid', ok ? 'false' : 'true');
        const err = document.getElementById(el.id + '-err');
        if (err) err.textContent = ok ? '' : (el.type === 'email' && el.value ? msg.errEmail : msg.errRequired);
        if (!ok && !first) first = el;
      });
      const status = form.querySelector('.form-status');
      if (first) { first.focus(); status.textContent = msg.errSummary; return; }
      const v = (n) => form.elements[n].value.trim();
      const text = `${msg.waIntro}\n${msg.lName}: ${v('first')} ${v('last')}\n${msg.lPhone}: ${v('phone')}\n${msg.lEmail}: ${v('email')}\n${msg.lCity}: ${v('city')}`;
      status.textContent = msg.ok;
      window.open('https://wa.me/18632669575?text=' + encodeURIComponent(text), '_blank', 'noopener');
    });
    form.querySelectorAll('input').forEach((el) => el.addEventListener('input', () => {
      if (el.getAttribute('aria-invalid') === 'true') {
        el.setAttribute('aria-invalid', 'false');
        const err = document.getElementById(el.id + '-err');
        if (err) err.textContent = '';
      }
    }));
  }
})();
