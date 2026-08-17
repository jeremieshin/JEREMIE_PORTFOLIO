from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

s = re.sub(r'<title>.*?</title>', '<title>JEREMIE Studio</title>', s, count=1, flags=re.S)
s = re.sub(r'\n?  /\* JEREMIE SAFE PATCH START \*/.*?/\* JEREMIE SAFE PATCH END \*/\n?', '\n', s, flags=re.S)
s = re.sub(r'\n?<script id="jeremie-safe-patch">.*?</script>\n?', '\n', s, flags=re.S)

css = r'''
  /* JEREMIE SAFE PATCH START */
  :root{
    --jeremie-accent:linear-gradient(135deg,#ff3d2b 0%,#e32b79 36%,#c12d98 66%,#9336d0 100%);
  }

  .filter-btn{
    font-size:clamp(40.5px,6.48vw,108px)!important;
    font-weight:800!important;
    line-height:.86!important;
    transition:opacity .2s ease!important;
  }
  .filter-btn.active,
  .filter-btn:hover,
  .filter-btn:focus-visible{
    color:transparent!important;
    background:var(--jeremie-accent)!important;
    -webkit-background-clip:text!important;
    background-clip:text!important;
    -webkit-text-fill-color:transparent!important;
  }

  .menu-overlay .menu-link:hover,
  .menu-overlay .menu-link:focus-visible,
  .menu-overlay .menu-link.active,
  .menu-overlay .menu-link[aria-current="page"],
  .menu-overlay .menu-nav a:hover,
  .menu-overlay .menu-nav a:focus-visible,
  .menu-overlay .menu-nav a.active,
  .menu-overlay .menu-nav a[aria-current="page"]{
    color:transparent!important;
    background:var(--jeremie-accent)!important;
    -webkit-background-clip:text!important;
    background-clip:text!important;
    -webkit-text-fill-color:transparent!important;
    text-decoration:none!important;
  }

  .burger{
    position:fixed!important;top:26px!important;right:40px!important;z-index:99999!important;
    width:42px!important;height:42px!important;border:1px solid currentColor!important;border-radius:0!important;
    background:transparent!important;display:flex!important;align-items:center!important;justify-content:center!important;
    flex-direction:column!important;gap:7px!important;padding:0!important;box-sizing:border-box!important;
    color:#555555!important;mix-blend-mode:normal!important;opacity:1!important;visibility:visible!important;pointer-events:auto!important;
  }
  .burger span{display:block!important;width:20px!important;height:2px!important;background:currentColor!important;margin:0!important;transform-origin:center!important;opacity:1!important;transition:transform .48s cubic-bezier(.16,.8,.24,1),opacity .25s ease!important;}
  .burger span:nth-child(n+3){display:none!important;}
  .burger.open span:nth-child(1){transform:translateY(4.5px) rotate(45deg)!important;}
  .burger.open span:nth-child(2){transform:translateY(-4.5px) rotate(-45deg)!important;}
  .burger.open{color:#333333!important;}
  body.inverted .burger.open{color:#f3f1ea!important;}
  .menu-close{display:none!important;}

  html.menu-open,body.menu-open{overflow:hidden!important;overscroll-behavior:none!important;}

  .menu-overlay.open hr,
  .menu-overlay.open [class*="footer"],
  .menu-overlay.open [class*="bottom"],
  .menu-overlay.open [class*="foot"],
  .menu-overlay.open [class*="meta"]{
    border-top:0!important;border-bottom:0!important;box-shadow:none!important;background-image:none!important;
  }
  .menu-overlay.open hr{display:none!important;}
  .menu-overlay.open [class*="footer"]::before,
  .menu-overlay.open [class*="footer"]::after,
  .menu-overlay.open [class*="bottom"]::before,
  .menu-overlay.open [class*="bottom"]::after,
  .menu-overlay.open [class*="foot"]::before,
  .menu-overlay.open [class*="foot"]::after,
  .menu-overlay.open [class*="meta"]::before,
  .menu-overlay.open [class*="meta"]::after{
    border:0!important;box-shadow:none!important;background:none!important;
  }
  .menu-overlay.open > :last-child{border-top:0!important;border-bottom:0!important;box-shadow:none!important;}

  .global-theme-toggle{position:fixed!important;right:40px!important;bottom:72px!important;z-index:390!important;color:#555555!important;}
  .global-theme-toggle .theme-label{display:none!important;}
  body.inverted .global-theme-toggle{color:#555555!important;}
  body.inverted .hero-title-img{filter:invert(1) hue-rotate(180deg) brightness(1.02) contrast(.96);}

  /* Work detail: a clean, solid fullscreen layer. No backdrop bleed or blur. */
  .work-detail-overlay{
    position:fixed!important;
    inset:0!important;
    z-index:100000!important;
    background:#151515!important;
    opacity:0;
    visibility:hidden;
    pointer-events:none;
    overflow-y:auto!important;
    overflow-x:hidden!important;
    overscroll-behavior:contain!important;
    -webkit-overflow-scrolling:touch;
    transition:opacity .35s cubic-bezier(.16,.8,.24,1),visibility .35s!important;
  }
  .work-detail-overlay.open{opacity:1!important;visibility:visible!important;pointer-events:auto!important;}
  .work-detail-stage{
    position:relative;
    min-height:100%;
    padding:76px 24px 96px!important;
    display:flex!important;
    justify-content:center!important;
    align-items:flex-start!important;
  }
  .work-detail-image{
    display:block!important;
    width:min(1180px,calc(100vw - 160px))!important;
    max-width:none!important;
    height:auto!important;
    object-fit:contain!important;
    image-rendering:auto!important;
    transform:translateY(18px)!important;
    opacity:0;
    box-shadow:0 30px 90px rgba(0,0,0,.34)!important;
    transition:transform .5s cubic-bezier(.16,.8,.24,1),opacity .3s ease!important;
  }
  .work-detail-overlay.open .work-detail-image{transform:translateY(0)!important;opacity:1!important;}

  .work-detail-close{
    position:fixed!important;
    top:26px!important;
    right:40px!important;
    z-index:100002!important;
    width:42px!important;
    height:42px!important;
    border:1px solid #f3f1ea!important;
    border-radius:0!important;
    background:#151515!important;
    color:#f3f1ea!important;
    cursor:pointer!important;
    padding:0!important;
    display:flex!important;
    align-items:center!important;
    justify-content:center!important;
  }
  .work-detail-close span{
    position:absolute!important;
    width:20px!important;
    height:1.5px!important;
    background:currentColor!important;
    display:block!important;
    transform-origin:center!important;
  }
  .work-detail-close span:first-child{transform:rotate(45deg)!important;}
  .work-detail-close span:last-child{transform:rotate(-45deg)!important;}
  .work-detail-close::before,.work-detail-close::after{content:none!important;display:none!important;}

  html.detail-open,body.detail-open{overflow:hidden!important;overscroll-behavior:none!important;}
  body.detail-open .burger,
  body.detail-open .global-theme-toggle{opacity:0!important;visibility:hidden!important;pointer-events:none!important;}

  @media(max-width:900px){
    .work-detail-image{width:calc(100vw - 56px)!important;}
  }
  @media(max-width:700px){
    .burger{top:20px!important;right:20px!important;}
    .global-theme-toggle{right:20px!important;bottom:56px!important}
    .filter-btn{font-size:clamp(36px,12vw,58px)!important;}
    .work-detail-stage{padding:72px 12px 48px!important;}
    .work-detail-image{width:calc(100vw - 24px)!important;}
    .work-detail-close{top:20px!important;right:20px!important;}
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
    const root = document.documentElement;
    const menu = document.querySelector('.menu-overlay');
    const oldBurger = document.querySelector('.burger');
    const menuClose = document.querySelector('.menu-close');

    const lockMenuScroll = () => {
      body.classList.add('menu-open');
      root.classList.add('menu-open');
    };
    const unlockMenuScroll = () => {
      body.classList.remove('menu-open');
      root.classList.remove('menu-open');
      body.style.position = '';
      body.style.top = '';
      body.style.left = '';
      body.style.right = '';
      body.style.width = '';
      body.style.overflow = '';
      root.style.overflow = '';
    };
    unlockMenuScroll();

    let burger = oldBurger;
    if (oldBurger && menu) {
      burger = oldBurger.cloneNode(true);
      burger.dataset.jeremieBound = '1';
      burger.innerHTML = '<span></span><span></span>';
      oldBurger.replaceWith(burger);
      document.body.appendChild(burger);

      const setMenu = (open) => {
        menu.classList.toggle('open', open);
        burger.classList.toggle('open', open);
        burger.setAttribute('aria-expanded', open ? 'true' : 'false');
        burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
        if (open) lockMenuScroll(); else unlockMenuScroll();
      };

      setMenu(false);
      burger.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        setMenu(!menu.classList.contains('open'));
      });
      document.querySelectorAll('.menu-link,.menu-nav a').forEach(link => {
        link.addEventListener('click', () => setMenu(false));
      });
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && menu.classList.contains('open')) setMenu(false);
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

    /* Rebuild the Work detail overlay once, so old duplicate handlers/buttons cannot remain. */
    document.querySelectorAll('#workDetailOverlay').forEach(el => el.remove());
    const overlay = document.createElement('div');
    overlay.id = 'workDetailOverlay';
    overlay.className = 'work-detail-overlay';
    overlay.setAttribute('aria-hidden','true');
    overlay.innerHTML = '<button class="work-detail-close" type="button" aria-label="Close project detail"><span></span><span></span></button><div class="work-detail-stage"><img class="work-detail-image" src="work_01_detail.png" alt="Grand 11st project detail" draggable="false"></div>';
    document.body.appendChild(overlay);

    const closeBtn = overlay.querySelector('.work-detail-close');
    const detailImage = overlay.querySelector('.work-detail-image');
    let detailScrollY = 0;

    const openDetail = () => {
      detailScrollY = window.scrollY || window.pageYOffset || 0;
      /* Never allow the menu lock to leak into the detail view. */
      if (menu) menu.classList.remove('open');
      if (burger) burger.classList.remove('open');
      unlockMenuScroll();
      overlay.scrollTop = 0;
      body.classList.add('detail-open');
      root.classList.add('detail-open');
      overlay.classList.add('open');
      overlay.setAttribute('aria-hidden','false');
    };

    const closeDetail = () => {
      overlay.classList.remove('open');
      overlay.setAttribute('aria-hidden','true');
      body.classList.remove('detail-open');
      root.classList.remove('detail-open');
      body.style.overflow = '';
      root.style.overflow = '';
      overlay.scrollTop = 0;
      requestAnimationFrame(() => window.scrollTo(0, detailScrollY));
    };

    const grid = document.querySelector('.grid');
    if (grid) {
      grid.addEventListener('click', e => {
        const tile = e.target.closest('.tile');
        if (!tile || tile !== grid.querySelector('.tile')) return;
        e.preventDefault();
        e.stopPropagation();
        openDetail();
      });
    }

    closeBtn.addEventListener('click', e => {
      e.preventDefault();
      e.stopPropagation();
      closeDetail();
    });
    overlay.addEventListener('click', e => {
      if (e.target === overlay) closeDetail();
    });
    if (detailImage) detailImage.addEventListener('click', e => e.stopPropagation());
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && overlay.classList.contains('open')) closeDetail();
    });
  });
})();
</script>
'''
if '</body>' not in s: raise SystemExit('body tag not found')
s = s.replace('</body>', js + '\n</body>', 1)
p.write_text(s, encoding='utf-8')
