// The Voyage demo: menu tabs, demo dialog for disabled booking, click-to-load map.
(() => {
  const dlg = document.getElementById('demo-dialog');
  const body = document.getElementById('dd-body');
  const msgs = {
    booking: (f) => {
      const d = new FormData(f);
      const when = d.get('in') && d.get('out') ? ` for ${d.get('in')} to ${d.get('out')}` : '';
      return `On the live site, this checks real-time availability for the ${String(d.get('berth')).toLowerCase()}${when} and takes you to a secure checkout, with no app commission. Booking is switched off in this demo, so nothing was sent.`;
    },
    table: () => 'On the live site, you pick a date, time and party size and get an instant confirmation on WhatsApp. Table booking is switched off in this demo, so nothing was sent.'
  };
  const show = (text) => {
    body.textContent = text;
    if (typeof dlg.showModal === 'function') dlg.showModal(); else alert(text);
  };

  document.querySelectorAll('form[data-demo]').forEach((f) => {
    f.addEventListener('submit', (e) => { e.preventDefault(); show(msgs[f.dataset.demo](f)); });
  });
  document.querySelectorAll('button[data-demo]').forEach((b) => {
    b.addEventListener('click', () => show(msgs[b.dataset.demo]()));
  });

  // Dates: default to tomorrow / day after, never in the past
  const pad = (n) => String(n).padStart(2, '0');
  const iso = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  const today = new Date();
  const inp = document.querySelector('input[name=in]');
  const out = document.querySelector('input[name=out]');
  if (inp && out) {
    inp.min = iso(today);
    const t1 = new Date(today); t1.setDate(t1.getDate() + 1);
    out.min = iso(t1);
    inp.addEventListener('change', () => {
      if (!inp.value) return;
      const n = new Date(inp.value); n.setDate(n.getDate() + 1);
      out.min = iso(n);
      if (!out.value || out.value <= inp.value) out.value = iso(n);
    });
  }

  // Menu tabs (ARIA tabs pattern with arrow keys)
  const tabs = [...document.querySelectorAll('.menu-tabs [role=tab]')];
  const select = (t, focus) => {
    tabs.forEach((x) => {
      const on = x === t;
      x.setAttribute('aria-selected', on);
      x.tabIndex = on ? 0 : -1;
      document.getElementById(x.getAttribute('aria-controls')).hidden = !on;
    });
    if (focus) t.focus();
  };
  tabs.forEach((t, i) => {
    t.addEventListener('click', () => select(t));
    t.addEventListener('keydown', (e) => {
      const k = e.key;
      if (k === 'ArrowRight' || k === 'ArrowLeft' || k === 'Home' || k === 'End') {
        e.preventDefault();
        const j = k === 'Home' ? 0 : k === 'End' ? tabs.length - 1 : (i + (k === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
        select(tabs[j], true);
      }
    });
  });

  // Map loads only when asked (keeps the page fast and cookie-free)
  const map = document.querySelector('[data-map]');
  map?.querySelector('.map-load')?.addEventListener('click', () => {
    const f = document.createElement('iframe');
    f.title = 'Map showing The Voyage, Lane 5, North Main Road, Koregaon Park';
    f.src = 'https://maps.google.com/maps?q=18.5394686,73.8975966&z=16&output=embed';
    f.referrerPolicy = 'no-referrer-when-downgrade';
    map.replaceChildren(f);
  });
})();
