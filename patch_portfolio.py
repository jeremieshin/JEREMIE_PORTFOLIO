from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

s = re.sub(r'<title>.*?</title>', '<title>JEREMIE Studio</title>', s, count=1, flags=re.S)
s = re.sub(r'\n?  /\* JEREMIE SAFE PATCH START \*/.*?/\* JEREMIE SAFE PATCH END \*/\n?', '\n', s, flags=re.S)
s = re.sub(r'\n?<script id="jeremie-safe-patch">.*?</script>\n?', '\n', s, flags=re.S)

css = r'''
  /* JEREMIE SAFE PATCH START */
  :root{--jeremie-accent:linear-gradient(90deg,#17a8e8 0%,#4778eb 50%,#8b39e7 100%);}

  .filter-btn{font-size:clamp(40.5px,6.48vw,108px)!important;font-weight:800!important;line-height:.86!important;}
  .filter-btn.active{color:transparent!important;background:var(--jeremie-accent)!important;-webkit-background-clip:text!important;background-clip:text!important;}

  /* Persistent menu button: fixed to viewport and always above menu overlay. */
  .burger{
    position:fixed!important;
    top:26px!important;
    right:40px!important;
    z-index:99999!important;
    width:42px!important;
    height:42px!important;
    border:1px solid currentColor!important;
    border-radius:0!important;
    background:transparent!important;
    display:flex!important;
    align-items:center!important;
    justify-content:center!important;
    flex-direction:column!important;
    gap:7px!important;
    padding:0!important;
    box-sizing:border-box!important;
    color:#555555!important;
    mix-blend-mode:normal!important;
    opacity:1!important;
    visibility:visible!important;
    pointer-events:auto!important;
  }
  .burger span{
    display:block!important;
    width:20px!important;
    height:2px!important;
    background:currentColor!important;
    margin:0!important;
    transform-origin:center!important;
    opacity:1!important;
    transition:transform .48s cubic-bezier(.16,.8,.24,1),opacity .25s ease!important;
  }
  .burger span:nth-child(n+3){display:none!important;}
  .burger.open span:nth-child(1){transform:translateY(4.5px) rotate(45deg)!important;}
  .burger.open span:nth-child(2){transform:translateY(-4.5px) rotate(-45deg)!important;}
  .burger.open{color:#333333!important;}
  body.inverted .burger.open{color:#f3f1ea!important;}

  /* Hide old close button: burger is the only menu/close control. */
  .menu-close{display:none!important;}

  /* Freeze the page underneath the menu overlay. */
  html.menu-open,body.menu-open{overscroll-behavior:none!important;}
  body.menu-open{overflow:hidden!important;touch-action:none!important;}

  .global-theme-toggle{position:fixed!important;right:40px!important;bottom:40px!important;z-index:390!important;color:#555555!important;}
  .global-theme-toggle .theme-label{display:none!important;}
  body.inverted .global-theme-toggle{color:#555555!important;}
  body.inverted .hero-title-img{filter:invert(1) hue-rotate(180deg) brightness(1.02) contrast(.96);}

  .work-detail-overlay{position:fixed;inset:0;z-index:520;background:rgba(18,18,18,.94);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);opacity:0;visibility:hidden;pointer-events:none;transition:opacity .45s cubic-bezier(.16,.8,.24,1),visibility .45s;overflow-y:auto;overscroll-behavior:contain;}
  .work-detail-overlay.open{opacity:1;visibility:visible;pointer-events:auto;}
  .work-detail-stage{min-height:100%;padding:92px 32px 72px;display:flex;justify-content:center;align-items:flex-start;}
  .work-detail-image{display:block;width:min(920px,82vw);height:auto;box-shadow:0 42px 120px rgba(0,0,0,.55);transform:translateY(34px) scale(.975);opacity:0;transition:transform .7s cubic-bezier(.16,.8,.24,1),opacity .45s ease;}
  .work-detail-overlay.open .work-detail-image{transform:translateY(0) scale(1);opacity:1;}
  .work-detail-close{position:fixed;top:26px;right:40px;z-index:2;width:42px;height:42px;border:1px solid #f3f1ea;border-radius:0;background:transparent;color:#f3f1ea;cursor:pointer;}
  .work-detail-close:before,.work-detail-close:after{content:'';position:absolute;left:10px;top:19px;width:20px;height:2px;background:currentColor;}
  .work-detail-close:before{transform:rotate(45deg)}.work-detail-close:after{transform:rotate(-45deg)}
  body.detail-open{overflow:hidden!important;}

  @media(max-width:700px){
    .burger{top:20px!important;right:20px!important;}
    .global-theme-toggle{right:20px!important;bottom:24px!important}
    .filter-btn{font-size:clamp(36px,12vw,58px)!important;}
    .work-detail-stage{padding:82px 14px 40px}.work-detail-image{width:94vw}.work-detail-close{top:20px;right:20px}
  }
  /* JEREMIE SAFE PATCH END */
'''
if '</style>' not in s: raise SystemExit('style tag not found')
s = s.replace('</style>', css + '\n</style>', 1)

js = r'''
<script id="jeremie-safe-patch">
(() => {
  const ready = (fn) => document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', fn) : fn();
  ready(() => {
    document.title = 'JEREMIE Studio';
    const body = document.body;
    const menu = document.querySelector('.menu-overlay');
    const oldBurger = document.querySelector('.burger');
    const menuClose = document.querySelector('.menu-close');
    let lockedScrollY = 0;

    const lockMenuScroll = () => {
      lockedScrollY = window.scrollY || window.pageYOffset || 0;
      body.classList.add('menu-open');
      document.documentElement.classList.add('menu-open');
      body.style.position = 'fixed';
      body.style.top = `-${lockedScrollY}px`;
      body.style.left = '0';
      body.style.right = '0';
      body.style.width = '100%';
    };
    const unlockMenuScroll = () => {
      body.classList.remove('menu-open');
      document.documentElement.classList.remove('menu-open');
      body.style.position = '';
      body.style.top = '';
      body.style.left = '';
      body.style.right = '';
      body.style.width = '';
      window.scrollTo(0, lockedScrollY);
    };

    let burger = oldBurger;
    if (oldBurger && menu) {
      /* Clone to remove legacy handlers, then move to BODY so no parent stacking context can hide it. */
      burger = oldBurger.cloneNode(true);
      burger.dataset.jeremieBound = '1';
      burger.innerHTML = '<span></span><span></span>';
      oldBurger.replaceWith(burger);
      document.body.appendChild(burger);

      const setMenu = (open) => {
        const wasOpen = menu.classList.contains('open');
        menu.classList.toggle('open', open);
        burger.classList.toggle('open', open);
        burger.setAttribute('aria-expanded', open ? 'true' : 'false');
        burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
        if (open && !wasOpen) lockMenuScroll();
        if (!open && wasOpen) unlockMenuScroll();
      };

      setMenu(menu.classList.contains('open'));
      burger.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        setMenu(!menu.classList.contains('open'));
      });
      document.querySelectorAll('.menu-link,.menu-nav a').forEach(link => {
        link.addEventListener('click', () => setMenu(false));
      });
    }
    if (menuClose) menuClose.setAttribute('aria-hidden','true');

    const themeButtons = [...document.querySelectorAll('.theme-toggle')];
    let theme = document.getElementById('themeToggle') || themeButtons[0];
    document.querySelectorAll('.global-theme-toggle').forEach(el => { if (el !== theme) el.remove(); });
    themeButtons.forEach(el => { if (el !== theme) el.remove(); });
    if (theme) {
      theme.classList.add('global-theme-toggle');
      document.body.appendChild(theme);
    }

    let overlay = document.getElementById('workDetailOverlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = 'workDetailOverlay';
      overlay.className = 'work-detail-overlay';
      overlay.setAttribute('aria-hidden','true');
      overlay.innerHTML = '<button class="work-detail-close" aria-label="Close project detail"></button><div class="work-detail-stage"><img class="work-detail-image" src="work_01_detail.png" alt="Grand 11st project detail"></div>';
      document.body.appendChild(overlay);
    }
    const close = () => { overlay.classList.remove('open'); overlay.setAttribute('aria-hidden','true'); body.classList.remove('detail-open'); };
    const open = () => { overlay.classList.add('open'); overlay.setAttribute('aria-hidden','false'); body.classList.add('detail-open'); overlay.scrollTop=0; };
    const grid = document.querySelector('.grid');
    if (grid) grid.addEventListener('click', e => { const tile=e.target.closest('.tile'); if(tile && tile===grid.querySelector('.tile')) open(); });
    const closeBtn=overlay.querySelector('.work-detail-close'); if(closeBtn) closeBtn.addEventListener('click',close);
    overlay.addEventListener('click',e=>{if(e.target===overlay)close()});
    document.addEventListener('keydown',e=>{if(e.key==='Escape'&&overlay.classList.contains('open'))close()});
  });
})();
</script>
'''
if '</body>' not in s: raise SystemExit('body tag not found')
s = s.replace('</body>', js + '\n</body>', 1)
p.write_text(s, encoding='utf-8')
