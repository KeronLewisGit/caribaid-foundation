// Caribaid Foundation preview: menu, scroll reveals, the wall of 50 blocks, the video and the giving picker.
(() => {
  const WA = '17584860990';
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  $$('[data-year]').forEach((e) => { e.textContent = new Date().getFullYear(); });

  // Menu
  const btn = $('.menu-btn'), nav = $('#nav');
  if (btn) {
    btn.addEventListener('click', () => { const open = nav.classList.toggle('open'); btn.setAttribute('aria-expanded', open); });
    nav.addEventListener('click', (e) => { if (e.target.closest('a')) { nav.classList.remove('open'); btn.setAttribute('aria-expanded', false); } });
  }
  const top = $('.top');
  const onScroll = () => top && top.classList.toggle('stuck', scrollY > 40);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Reveal on scroll; siblings stagger
  const io = new IntersectionObserver((entries) => entries.forEach((en) => {
    if (!en.isIntersecting) return;
    const sibs = $$(':scope > [data-r]', en.target.parentElement);
    en.target.style.setProperty('--d', Math.max(0, sibs.indexOf(en.target)) * 90 + 'ms');
    en.target.classList.add('in'); io.unobserve(en.target);
  }), { threshold: 0.14, rootMargin: '0px 0px -6% 0px' });
  $$('[data-r]').forEach((el) => io.observe(el));

  // Things that switch on once when they come into view
  const once = new IntersectionObserver((entries) => entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('on'); once.unobserve(en.target); } }), { threshold: 0.35 });
  $$('[data-wall], [data-path]').forEach((el) => once.observe(el));

  // Interview: the YouTube player loads only when asked for
  $$('[data-yt]').forEach((b) => b.addEventListener('click', () => {
    const f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + b.dataset.yt + '?autoplay=1&rel=0';
    f.allow = 'autoplay; encrypted-media; picture-in-picture'; f.allowFullscreen = true; f.title = 'The Dolor Factor: This Foundation Cares, part 1';
    b.replaceChildren(f);
  }, { once: true }));

  // Giving picker
  const TIPS = {
    clothes: ['Clothes', 'Clean, wearable clothes and shoes for babies and children. Sort by size if you can; it saves our volunteers hours.'],
    supplies: ['School supplies', 'Exercise books, pencils, crayons, school bags and lunch kits. New or gently used.'],
    food: ['Food', 'Rice, flour, tinned fish, milk, cereal and fresh produce for the feeding programme.'],
    building: ['Building materials', 'Blocks, cement, steel, lumber and roofing for the daycare, or a tradesperson’s time.'],
    money: ['Money', 'Sponsor a child’s daycare place or contribute to the building fund. We will send you the details and a receipt.'],
    time: ['My time', 'Cooks, mentors, special-aid teachers and fundraisers. Tell us what you are good at and when you are free.'],
  };
  const picker = $('[data-picker]');
  if (picker) {
    const advice = $('.advice', picker), form = $('.send', picker), prev = $('[data-preview]', picker), err = $('.send-err', picker), mail = $('[data-mail]', picker);
    const chosen = () => $$('.chip[aria-pressed=true]', picker).map((c) => c.dataset.k);
    const message = () => {
      const k = chosen(); if (!k.length) return '';
      const f = new FormData(form), name = (f.get('name') || '').trim(), note = (f.get('note') || '').trim();
      return 'Hello Earl, ' + (name ? 'my name is ' + name + '. ' : '') + 'I would like to give: ' + k.map((x) => TIPS[x][0].toLowerCase()).join(', ') + '. I am ' + (f.get('where') === 'Overseas' ? 'overseas' : 'in Saint Lucia') + '.' + (note ? '\n' + note : '');
    };
    const render = () => {
      const k = chosen();
      advice.innerHTML = k.length ? k.map((x) => '<div class="tip"><h3>' + TIPS[x][0] + '</h3><p>' + TIPS[x][1] + '</p></div>').join('') : '<p class="advice-empty">Pick something above to see what helps most.</p>';
      const m = message(); prev.textContent = m;
      mail.href = 'mailto:earl@caribaidfoundation.com?subject=' + encodeURIComponent('I would like to give') + '&body=' + encodeURIComponent(m);
      if (k.length) err.hidden = true;
    };
    const pick = (k, on = true) => { const c = $('.chip[data-k="' + k + '"]', picker); if (c) { c.setAttribute('aria-pressed', on); render(); } };
    $$('.chip', picker).forEach((c) => c.addEventListener('click', () => { c.setAttribute('aria-pressed', c.getAttribute('aria-pressed') !== 'true'); render(); }));
    form.addEventListener('input', render);
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      if (!chosen().length || !form.name.value.trim()) { err.hidden = false; return; }
      window.open('https://wa.me/' + WA + '?text=' + encodeURIComponent(message()), '_blank', 'noopener');
    });
    // A link elsewhere can arrive with something already picked
    try { const k = sessionStorage.getItem('caribaid-pick'); if (k) { pick(k); sessionStorage.removeItem('caribaid-pick'); } } catch (e) { /* storage may be unavailable */ }
    $$('[data-pick]').forEach((a) => a.addEventListener('click', () => pick(a.dataset.pick)));
    render();
  } else {
    $$('[data-pick]').forEach((a) => a.addEventListener('click', () => { try { sessionStorage.setItem('caribaid-pick', a.dataset.pick); } catch (e) { /* ignore */ } }));
  }
})();
