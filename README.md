# DPGlance website

Marketing site, legal pages and Google Play helper files for **DPGlance**, a free Android app for viewing and saving
the public photos on a profile.

- Live site: https://soham-tejani.github.io/dpglance/
- Privacy policy: https://soham-tejani.github.io/dpglance/privacy/
- Terms: https://soham-tejani.github.io/dpglance/terms/
- Support and reports: https://soham-tejani.github.io/dpglance/support/

> DPGlance is an independent app and is not affiliated with, endorsed by, or sponsored by Snap Inc. Snapchat and the
> Ghost logo are trademarks of Snap Inc.

## Layout

```
docs/          the published site (GitHub Pages serves this folder)
play-store/    Google Play listing copy, Data safety answers, declarations, checklist, graphics
tools/         build.py (page generator), graphics.py (icons, social image, Play graphics)
.github/       issue forms used by the Support page
```

The site is plain static HTML and CSS. It makes no third-party requests: the font (Space Grotesk, SIL Open Font
License 1.1) and the small script are self-hosted, and there are no analytics or cookies.

## Edit and rebuild

Pages are generated so the header, footer, disclaimer and SEO tags stay identical everywhere. Edit
`tools/build.py` (content) or `docs/assets/css/style.css` (design), then:

```bash
python3 tools/build.py
python3 -m http.server 8000 --directory docs   # preview at http://localhost:8000/
```

Regenerate icons and the social/Play graphics (needs `fonttools`, `rsvg-convert` and ImageMagick):

```bash
python3 tools/graphics.py path/to/spacegrotesk.ttf
```

Do not edit the generated `docs/*.html` files by hand; the next build overwrites them.

## Deploy

GitHub Pages is configured to serve the `main` branch, `/docs` folder. Pushing to `main` publishes the site.

## Before the app goes live on Google Play

Read `play-store/CHECKLIST.md`. It lists the blockers still open in the app (no in-app privacy link, test AdMob IDs,
unsigned release build) and what to update on this site once the listing exists.
