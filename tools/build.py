#!/usr/bin/env python3
"""Generates the static Peekly site into ../docs. Run: python3 tools/build.py"""
import json
import pathlib
from html import escape

OUT = pathlib.Path(__file__).resolve().parent.parent / "docs"
SITE = "https://soham-tejani.github.io/peekly"
REPO = "https://github.com/soham-tejani/peekly"
ISSUES = REPO + "/issues/new/choose"
ISSUE_HELP = REPO + "/issues/new?template=support.yml"
ISSUE_REPORT = REPO + "/issues/new?template=report-content.yml"
ISSUE_PRIVACY = REPO + "/issues/new?template=privacy-request.yml"
UPDATED = "2026-11-08"
UPDATED_H = "8 November 2026"
OG = SITE + "/assets/img/og-image.png"

DISCLAIMER = (
    "Peekly is an independent app and is not affiliated with, endorsed by, or sponsored by Snap Inc. "
    "Snapchat, Snap and the Ghost logo are trademarks of Snap Inc., used here only to describe what the app "
    "works with. Google Play and Android are trademarks of Google LLC."
)

ICONS = {
    "link": '<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/>',
    "image": '<rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="9" cy="9" r="1.8"/><path d="m21 15-5-5L5 21"/>',
    "play": '<rect x="3" y="4" width="18" height="16" rx="3"/><path d="m10 9 5 3-5 3z"/>',
    "download": '<path d="M12 4v11"/><path d="m7 11 5 5 5-5"/><path d="M5 20h14"/>',
    "shield": '<path d="M12 3 4.5 6v5.5c0 4.5 3.2 8 7.5 9.5 4.3-1.5 7.5-5 7.5-9.5V6z"/><path d="m9 12 2.2 2.2L15.5 10"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
}


def icon(name):
    return f'<span class="ico" aria-hidden="true"><svg viewBox="0 0 24 24">{ICONS[name]}</svg></span>'


FAQ = [
    ("What is Peekly?",
     "Peekly is a free Android app that shows the public photos on a profile (the profile picture, cover image and "
     "highlights) at full size from a link you copy, and lets you save them to your gallery."),
    ("Does it work with private accounts?",
     "No. Peekly only shows what a profile publishes publicly. A personal account without a public profile photo "
     "shows a “no public photo” message. Peekly never asks you to sign in and never shows anything that "
     "is not already public."),
    ("Do I need an account?",
     "No. Peekly has no accounts, no sign-in and no developer server."),
    ("Why do I watch an ad?",
     "Peekly is free. Unlocking a profile’s photo and cover, or a highlight, takes one short rewarded ad from "
     "Google AdMob. You always choose to start it, and nothing pops up unexpectedly. If an ad can’t load after a "
     "couple of tries, Peekly lets you continue."),
    ("What does Peekly do with my clipboard?",
     "Each time you open the app, it checks on your device whether the text you most recently copied is a Snapchat "
     "profile link. Nothing from your clipboard is stored or sent anywhere, except the username in that link, which "
     "is looked up on snapchat.com. Details are in the Privacy Policy."),
    ("Where are my saved files?",
     "Photos are saved to Pictures/Peekly/username and videos to Movies/Peekly/username on your phone, using "
     "Android’s standard media storage, so Peekly needs no storage permission."),
    ("Is Peekly affiliated with Snapchat?",
     "No. Peekly is an independent app and is not affiliated with, endorsed by, or sponsored by Snap Inc. Snapchat "
     "and the Ghost logo are trademarks of Snap Inc."),
    ("Which Android versions are supported?",
     "Android 10 (API level 29) and later."),
    ("Who owns the pictures I see in Peekly?",
     "Their creators. Save images for personal use only, and don’t repost them without the creator’s permission."),
    ("How do I report misuse or ask for removal?",
     "Open a support request on the Support page. Peekly only reads what a profile already publishes on Snapchat, so "
     "the quickest way to stop a profile appearing is to change that profile’s visibility in Snapchat. We also "
     "review every request."),
]


def head(title, desc, path, root, jsonld=None, noindex=False):
    canon = SITE + "/" + path
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large"
    ld = ""
    if jsonld:
        ld = "\n".join(
            '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False, separators=(",", ":")) + "</script>"
            for j in jsonld
        )
    t, d = escape(title, quote=True), escape(desc, quote=True)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0c0c0d">
<meta name="color-scheme" content="dark">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Peekly">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{OG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Peekly app icon, an amber eye with a coral iris, on a dark glass background">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{OG}">
<meta name="twitter:image:alt" content="Peekly app icon, an amber eye with a coral iris, on a dark glass background">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{root}favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="{root}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="preload" href="{root}assets/fonts/space-grotesk.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/css/style.css">
{ld}
</head>"""


def header(root, current=""):
    home = root or "./"

    def a(label, href, key):
        cur = ' aria-current="page"' if key and key == current else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'

    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<div class="aurora" aria-hidden="true"><i></i><i></i><i></i></div>
<header class="site-header">
<div class="wrap">
<nav class="nav glass" aria-label="Main">
<a class="brand" href="{home}"><img src="{root}assets/img/logo.svg" width="34" height="34" alt="">Peekly</a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
<ul id="menu">
{a("Features", home + "#features", "")}
{a("How it works", home + "#how", "")}
{a("FAQ", home + "#faq", "")}
{a("Privacy", root + "privacy/", "privacy")}
{a("Support", root + "support/", "support")}
</ul>
</nav>
</div>
</header>
"""


def footer(root):
    home = root or "./"
    return f"""<footer>
<div class="wrap foot">
<div>
<a class="brand" href="{home}"><img src="{root}assets/img/logo.svg" width="34" height="34" alt="">Peekly</a>
<p class="meta" style="margin-top:12px">Peek at any public profile. A free Android app for viewing and saving public profile photos, covers and highlights.</p>
</div>
<div>
<h2>Explore</h2>
<ul>
<li><a href="{home}#features">Features</a></li>
<li><a href="{home}#how">How it works</a></li>
<li><a href="{home}#faq">FAQ</a></li>
</ul>
</div>
<div>
<h2>Legal and help</h2>
<ul>
<li><a href="{root}privacy/">Privacy Policy</a></li>
<li><a href="{root}terms/">Terms of Use</a></li>
<li><a href="{root}support/">Support and reports</a></li>
<li><a href="{REPO}" rel="noopener">Site source on GitHub</a></li>
</ul>
</div>
<p class="legal">{DISCLAIMER} &copy; 2026 Peekly.</p>
</div>
</footer>
<script src="{root}assets/js/main.js" defer></script>
</body>
</html>
"""


def write(rel, content):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def crumbs(root, label):
    return f'<p class="crumbs"><a href="{root or "./"}">Home</a> / {label}</p>'


def breadcrumb_ld(label, path):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Peekly", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": label, "item": SITE + "/" + path},
        ],
    }


# ---------------------------------------------------------------- home
def home():
    root = ""
    title = "Peekly: view public profile photos, covers and highlights"
    desc = ("Peekly is a free Android app. Copy a public profile link to view the profile photo, cover and "
            "highlights at full size and save them. No account needed.")
    ld = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": "Peekly", "url": SITE + "/",
         "description": desc, "inLanguage": "en"},
        {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Peekly",
         "description": desc, "url": SITE + "/", "image": SITE + "/assets/img/og-image.png",
         "applicationCategory": "UtilitiesApplication", "operatingSystem": "ANDROID",
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "featureList": ["Detects a copied public profile link", "Full-size profile photo and cover",
                         "Highlights and Spotlight viewer", "Save to your gallery without extra permissions",
                         "No account and no developer server"],
         "isAccessibleForFree": True},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
    ]
    faq_html = "\n".join(
        f'<details class="glass"><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in FAQ
    )
    # The FAQ entries mention pages by name; link them for people (JSON-LD keeps plain text).
    faq_html = faq_html.replace("Privacy Policy.", '<a href="privacy/">Privacy Policy</a>.', 1)
    faq_html = faq_html.replace("Support page.", '<a href="support/">Support page</a>.', 1)

    body = f"""
<main id="main">
<div class="wrap hero">
<div>
<p class="eyebrow">Profile viewer for Android</p>
<h1>Peek at any <span class="grad">public profile.</span></h1>
<p class="lead" style="margin-top:20px">Copy a public profile link, open Peekly, and see the profile photo, cover and highlights at full size. Save what you like to your gallery. No account, no sign-in.</p>
<div class="cta">
<a class="btn primary" href="#how">See how it works</a>
<span class="soon"><span class="dot" aria-hidden="true"></span>Coming soon to Google Play</span>
</div>
<ul class="chips" aria-label="Highlights">
<li>Free</li><li>No account</li><li>Android 10+</li><li>Rewarded ads only, never surprise ones</li>
</ul>
</div>
<div class="reveal">
<div class="phone" role="img" aria-label="Illustration of the Peekly profile screen: a round profile picture, a Watch a short ad to view and save button, a locked cover image and a row of highlights.">
<div class="screen">
<span class="orb o1"></span><span class="orb o2"></span>
<div class="bar"><b>&larr;</b>@username</div>
<div class="dp"><span></span></div>
<div class="name">Sample Creator</div>
<div class="handle">@username</div>
<div class="watch">Watch a short ad to view &amp; save</div>
<div class="hint">One ad unlocks this profile&rsquo;s photo and cover.</div>
<div class="cover"><svg viewBox="0 0 24 24" fill="none" stroke="#f4f4f5" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg></div>
<div class="hl"><i></i><i></i><i></i><i></i></div>
</div>
</div>
<p class="caption">Illustration of the app. Not a real profile.</p>
</div>
</div>

<section id="features" aria-labelledby="f-h">
<div class="wrap">
<div class="head reveal"><p class="eyebrow">Features</p><h2 id="f-h">Everything a profile viewer needs, nothing it doesn&rsquo;t.</h2></div>
<div class="grid">
<article class="card glass reveal">{icon("link")}<h3>Finds your link</h3><p>Copy a public profile link and open Peekly. It spots the link for you, or you can paste a link or username yourself.</p></article>
<article class="card glass reveal">{icon("image")}<h3>Full-size photos and covers</h3><p>See the profile picture and cover image at the largest size the profile offers, with pinch-to-zoom.</p></article>
<article class="card glass reveal">{icon("play")}<h3>Highlights and Spotlight</h3><p>Browse a profile&rsquo;s public highlights and Spotlight rows and open each one in a full-screen viewer.</p></article>
<article class="card glass reveal">{icon("download")}<h3>Save to your gallery</h3><p>Save photos and videos to Pictures/Peekly using Android&rsquo;s media storage. No storage permission needed.</p></article>
<article class="card glass reveal">{icon("shield")}<h3>Private by design</h3><p>No account, no analytics of ours and no developer server. Your recent profiles stay on your phone.</p></article>
<article class="card glass reveal">{icon("clock")}<h3>Fair, rewarded ads</h3><p>One short ad that you choose to watch unlocks a profile. Nothing pops up out of the blue.</p></article>
</div>
</div>
</section>

<section id="how" aria-labelledby="h-h">
<div class="wrap">
<div class="head reveal"><p class="eyebrow">How it works</p><h2 id="h-h">Three taps from link to photo.</h2></div>
<ol class="steps">
<li class="glass reveal"><h3>Copy a link</h3><p>Copy a public profile link from Snapchat, a browser or a message.</p></li>
<li class="glass reveal"><h3>Open Peekly</h3><p>Peekly detects the link and loads the public profile. Or paste it yourself.</p></li>
<li class="glass reveal"><h3>View and save</h3><p>Watch one short rewarded ad to unlock, then view full-size and save to your gallery.</p></li>
</ol>
</div>
</section>

<section aria-labelledby="r-h">
<div class="wrap split">
<div class="panel glass reveal">
<p class="eyebrow">Responsible use</p>
<h2 id="r-h" style="font-size:1.6rem">Public content, creator&rsquo;s rights.</h2>
<ul>
<li>Peekly only shows what a profile publishes publicly.</li>
<li>Pictures belong to their creators. Save them for personal use and don&rsquo;t repost without permission.</li>
<li>Don&rsquo;t use Peekly to harass, stalk or impersonate anyone.</li>
</ul>
<p style="margin-top:16px"><a href="terms/">Read the Terms of Use</a></p>
</div>
<div class="panel glass reveal">
<p class="eyebrow">Your privacy</p>
<h2 style="font-size:1.6rem">What leaves your phone, in plain words.</h2>
<ul>
<li>Your clipboard is checked on your device when you open the app. It is never stored or sent anywhere.</li>
<li>Only the username in a link you copied is looked up on snapchat.com.</li>
<li>Ads come from Google AdMob, with Google&rsquo;s consent form where the law requires it.</li>
</ul>
<p style="margin-top:16px"><a href="privacy/">Read the Privacy Policy</a></p>
</div>
</div>
</section>

<section id="faq" aria-labelledby="q-h">
<div class="wrap">
<div class="head reveal"><p class="eyebrow">FAQ</p><h2 id="q-h">Questions, answered.</h2></div>
<div class="faq">
{faq_html}
</div>
</div>
</section>
</main>
"""
    write("index.html", head(title, desc, "", root, ld) + header(root) + body + footer(root))


# ---------------------------------------------------------------- privacy
def privacy():
    root = "../"
    title = "Privacy Policy | Peekly"
    desc = ("How Peekly handles your data: clipboard checks happen on your device, no accounts or developer "
            "server, and ads come from Google AdMob with consent where required.")
    body = f"""
<main id="main" class="page">
<div class="wrap">
<article class="prose glass">
{crumbs(root, "Privacy Policy")}
<h1>Privacy Policy</h1>
<p class="meta">Effective and last updated: {UPDATED_H}</p>

<div class="note"><p><strong>In short.</strong> Peekly has no accounts and no developer server, and we do not run analytics or crash reporting of our own. Your clipboard is checked on your device and never stored or sent anywhere. The only things that leave your phone are the lookup of a profile on snapchat.com and the ad requests handled by Google AdMob.</p></div>

<h2>1. Who we are</h2>
<p>Peekly is a free Android app published by an independent developer (GitHub: <a href="https://github.com/soham-tejani" rel="noopener">soham-tejani</a>). In this policy, &ldquo;we&rdquo; and &ldquo;us&rdquo; mean the Peekly developer. To contact us, see <a href="{root}support/">Support</a>.</p>
<p>Peekly is an independent app. It is not affiliated with, endorsed by, or sponsored by Snap Inc.</p>

<h2>2. What Peekly does with information</h2>
<div class="tbl"><table>
<thead><tr><th scope="col">Information</th><th scope="col">What happens</th><th scope="col">Leaves your device?</th></tr></thead>
<tbody>
<tr><td><strong>Clipboard text</strong></td><td>When you open Peekly, it checks whether the text you most recently copied is plain text, and if so, whether it contains a Snapchat profile link. This happens in memory on your device. If you tap Paste, Peekly reads the clipboard to fill the link box. Clipboard text is never saved or logged. Android may show a notice when an app reads the clipboard.</td><td>No. Only the username found in a link is used (next row).</td></tr>
<tr><td><strong>Profile lookups</strong></td><td>To show a profile, your device requests the public profile page from snapchat.com, and the pictures and videos from Snapchat&rsquo;s content servers (for example sc-cdn.net). These requests go directly from your phone to Snap. We do not proxy, copy or store them.</td><td>Yes, to Snap. Snap receives what any web request includes, such as your IP address, a browser-style user agent and the username requested, and handles it under its own privacy policy.</td></tr>
<tr><td><strong>Recent profiles</strong></td><td>Peekly remembers up to 30 recently opened profiles (username, display name and a thumbnail link) so you can reopen them. You can remove entries or tap Clear. It also remembers that you have seen the intro screen.</td><td>No. Stored in the app&rsquo;s private storage and deleted when you uninstall.</td></tr>
<tr><td><strong>Files you save</strong></td><td>Saved photos go to Pictures/Peekly and videos to Movies/Peekly on your device, using Android media storage. Peekly cannot read your other photos or files.</td><td>No.</td></tr>
<tr><td><strong>Advertising data</strong></td><td>The free app shows rewarded ads through Google AdMob (see section 3).</td><td>Yes, to Google.</td></tr>
</tbody></table></div>

<h3>What we do not collect</h3>
<p>We do not ask for or collect your name, email address, phone number, contacts, precise location, camera or microphone data, or any account details. Peekly has no sign-in. We do not operate a server that receives data from the app.</p>

<h2>3. Advertising (Google AdMob)</h2>
<p>Peekly uses Google AdMob to show rewarded ads. You always choose to start an ad. According to Google&rsquo;s documentation, the Google Mobile Ads SDK automatically collects and shares, for advertising, analytics and fraud prevention purposes:</p>
<ul>
<li>your device&rsquo;s IP address, which Google may use to estimate your general location;</li>
<li>product interactions, such as app launches, taps and video views;</li>
<li>diagnostic information about the app and SDK performance, such as launch time and hang rate; and</li>
<li>device identifiers, including the Android advertising ID and app set ID.</li>
</ul>
<p>Peekly declares the advertising ID permission so ads can be served. You can reset or delete your advertising ID, or limit ad personalisation, in your Android settings (usually under Google or Privacy, then Ads), and manage Google ad settings at <a href="https://adssettings.google.com" rel="noopener">adssettings.google.com</a>. Where the law requires consent, for example in the European Economic Area and the United Kingdom, Peekly shows Google&rsquo;s consent form first and does not request ads until consent allows it.</p>
<p>Google processes this data under its own terms. See <a href="https://policies.google.com/privacy" rel="noopener">Google&rsquo;s Privacy Policy</a> and <a href="https://policies.google.com/technologies/ads" rel="noopener">how Google uses data from ads</a>.</p>

<h2>4. How we use information</h2>
<p>Only to run the features you ask for: finding a link, showing a profile, saving files, and showing ads that fund the free app. We do not sell your personal information. We have no user database to sell or share.</p>

<h2>5. Who else is involved</h2>
<ul>
<li><strong>Snap Inc.</strong> receives the profile and media requests described above.</li>
<li><strong>Google</strong> receives ad-related data through AdMob and the User Messaging Platform consent form.</li>
</ul>
<p>We do not control these companies. Their own privacy policies apply to what they receive.</p>

<h2>6. Retention and deletion</h2>
<p>We hold no personal data about you. Data stored on your phone (recent profiles and the intro flag) stays until you remove it or uninstall Peekly. Files you saved stay in your gallery until you delete them. Data held by Google or Snap is governed by their policies and controls.</p>

<h2>7. Security</h2>
<p>Peekly connects only over HTTPS and blocks unencrypted traffic. Its stored data is excluded from Android backups. No method of transmission or storage is perfectly secure, but we keep the amount of data handled to a minimum.</p>

<h2>8. Your choices and rights</h2>
<p>Depending on where you live (for example under the GDPR, UK GDPR, California&rsquo;s CCPA/CPRA or India&rsquo;s Digital Personal Data Protection Act), you may have rights to access, correct, delete or restrict the use of your personal data. Because we do not hold personal data about you, there is usually nothing for us to provide or delete, but you can still contact us and we will respond. To control advertising data, use the Android and Google settings described in section 3.</p>

<h2>9. Children</h2>
<p>Peekly is not directed to children under 13, and ads are not directed to children. Snapchat itself requires users to be at least 13. If you believe a child has used Peekly in a way that concerns you, please contact us.</p>

<h2>10. International processing</h2>
<p>Google and Snap operate globally, so data sent to them may be processed in countries other than yours.</p>

<h2>11. Changes to this policy</h2>
<p>We may update this policy when the app changes, for example if we add a feature that handles data differently. The date at the top shows the latest version. If a change is significant, we will say so on this page and in the app update notes.</p>

<h2>12. Contact</h2>
<p>Questions, requests or concerns: <a href="{ISSUE_PRIVACY}" rel="noopener">open a request on GitHub</a> using the Privacy request form. Please do not put personal details in a public issue. Tell us what you need and we will reply with a private way to continue if one is needed. More options are on the <a href="{root}support/">Support page</a>.</p>
</article>
</div>
</main>
"""
    ld = [breadcrumb_ld("Privacy Policy", "privacy/")]
    write("privacy/index.html", head(title, desc, "privacy/", root, ld) + header(root, "privacy") + body + footer(root))


# ---------------------------------------------------------------- terms
def terms():
    root = "../"
    title = "Terms of Use | Peekly"
    desc = ("The rules for using Peekly: public content only, respect creators’ rights, no affiliation with "
            "Snap Inc., and how ads and availability work.")
    body = f"""
<main id="main" class="page">
<div class="wrap">
<article class="prose glass">
{crumbs(root, "Terms of Use")}
<h1>Terms of Use</h1>
<p class="meta">Effective and last updated: {UPDATED_H}</p>

<h2>1. Agreement</h2>
<p>By installing or using Peekly (the &ldquo;app&rdquo;) or this website, you agree to these terms and to our <a href="{root}privacy/">Privacy Policy</a>. If you do not agree, please do not use them.</p>

<h2>2. What Peekly is</h2>
<p>Peekly is a free Android app that shows what a public profile already publishes openly (such as the profile picture, cover image, highlights and Spotlight) from a link you provide, and lets you save those items to your device. It works only with public information and never asks you to sign in to another service.</p>

<h2>3. Independent app</h2>
<p>{escape(DISCLAIMER)}</p>

<h2>4. Using Peekly responsibly</h2>
<p>You agree that you will:</p>
<ul>
<li>use Peekly only for lawful, personal, non-commercial purposes;</li>
<li>respect the rights of the people who created the content, and not repost, sell or redistribute it without their permission;</li>
<li>not use Peekly to harass, stalk, threaten, impersonate, or expose private information about anyone;</li>
<li>not attempt to access anything that is not public, or to bypass any block or limit set by a third party;</li>
<li>not use Peekly for bulk, automated or repeated collection of profiles; and</li>
<li>follow the terms of any service you use alongside Peekly. You are responsible for how you use what you view or save.</li>
</ul>

<h2>5. Creators&rsquo; content</h2>
<p>Profile pictures, covers, highlights and other content belong to their creators and, where applicable, to the platform they were published on. Peekly does not host, copy or claim ownership of that content. It is fetched directly from the source to your device. Saving an image gives you no licence to use it beyond what the law and the creator allow.</p>

<h2>6. Ads</h2>
<p>The free app shows rewarded ads provided by Google AdMob. You choose when to watch one. Ads are third-party content and we are not responsible for them. See the Privacy Policy for how ad data is handled.</p>

<h2>7. Third-party services and availability</h2>
<p>Peekly depends on third-party services that we do not control. They may change, limit or block access at any time, which can make parts of Peekly stop working or show errors. We do not promise that Peekly will always be available, accurate or error-free, and we may change or discontinue features at any time.</p>

<h2>8. Our property</h2>
<p>The Peekly name, logo, design and app code are the developer&rsquo;s. These terms do not give you any rights to them except to use the app as intended.</p>

<h2>9. No warranty</h2>
<p>Peekly is provided &ldquo;as is&rdquo; and &ldquo;as available&rdquo;, without warranties of any kind, to the fullest extent allowed by law.</p>

<h2>10. Limitation of liability</h2>
<p>To the fullest extent allowed by law, the Peekly developer is not liable for indirect, incidental, special or consequential damages, or for loss of data or profits, arising from your use of Peekly. Nothing in these terms limits any rights or liability that cannot be limited under the law that applies to you, including statutory consumer rights.</p>

<h2>11. Reports and removal requests</h2>
<p>If you are a creator or rights holder and believe Peekly is being misused, or you want to raise a concern, please use the <a href="{root}support/">Support page</a>. We review requests promptly and act where appropriate.</p>

<h2>12. Ending use and changes</h2>
<p>You can stop using Peekly at any time by uninstalling it. We may update these terms; the date above shows the latest version, and continued use after an update means you accept it.</p>

<h2>13. Contact</h2>
<p>See the <a href="{root}support/">Support page</a>.</p>
</article>
</div>
</main>
"""
    ld = [breadcrumb_ld("Terms of Use", "terms/")]
    write("terms/index.html", head(title, desc, "terms/", root, ld) + header(root) + body + footer(root))


# ---------------------------------------------------------------- support
def support():
    root = "../"
    title = "Support and reports | Peekly"
    desc = ("Get help with Peekly, report misuse, make a takedown or removal request, or send a privacy "
            "request. Includes fixes for common problems.")
    body = f"""
<main id="main" class="page">
<div class="wrap">
<article class="prose glass">
{crumbs(root, "Support")}
<h1>Support and reports</h1>
<p class="meta">Last updated: {UPDATED_H}</p>

<h2>Contact us</h2>
<p>The fastest way to reach us is a request on GitHub. Pick the form that fits:</p>
<ul>
<li><a href="{ISSUE_HELP}" rel="noopener"><strong>Get help or report a bug</strong></a>: something is not working.</li>
<li><a href="{ISSUE_REPORT}" rel="noopener"><strong>Report misuse or request removal</strong></a>: you are a creator or rights holder with a concern.</li>
<li><a href="{ISSUE_PRIVACY}" rel="noopener"><strong>Privacy request</strong></a>: questions or requests about your data.</li>
</ul>
<div class="note"><p><strong>Please keep it private.</strong> GitHub requests are public. Do not post personal details, screenshots of private information or anything sensitive. Describe what you need and we will reply with a private way to continue if one is needed.</p></div>

<h2>Common problems</h2>
<h3>Peekly doesn&rsquo;t find my link</h3>
<p>Copy the full profile link and open Peekly again, or paste the link or username into the box on the home screen. Only public profile links are supported.</p>
<h3>&ldquo;No public photo&rdquo; or &ldquo;Profile not found&rdquo;</h3>
<p>Peekly shows only what a profile publishes publicly. A personal account without a public profile has no public photo to show. Check the username for typos.</p>
<h3>The ad won&rsquo;t load</h3>
<p>Check your connection and try again. If an ad can&rsquo;t load after a couple of tries, Peekly lets you continue.</p>
<h3>Where did my saved files go?</h3>
<p>Photos are in Pictures/Peekly/username and videos in Movies/Peekly/username. Look in your gallery or Files app under those folders.</p>
<h3>Something suddenly stopped working</h3>
<p>Peekly relies on a third-party website that can change without notice. Update the app, and if the problem continues, send us a bug report.</p>

<h2>Reports and removal requests</h2>
<p>Peekly does not host or store anyone&rsquo;s content. It shows what a profile already publishes publicly. If you are a creator and do not want your public profile to be visible, the quickest fix is to change your profile&rsquo;s visibility in Snapchat. If you believe Peekly is being used to harm someone or to infringe rights, send us a report using the form above, with the username concerned and what the problem is. We review every request and act where appropriate.</p>

<h2>About Peekly</h2>
<p>{escape(DISCLAIMER)}</p>
<p>See also: <a href="{root}privacy/">Privacy Policy</a> &middot; <a href="{root}terms/">Terms of Use</a></p>
</article>
</div>
</main>
"""
    ld = [breadcrumb_ld("Support", "support/")]
    write("support/index.html", head(title, desc, "support/", root, ld) + header(root, "support") + body + footer(root))


# ---------------------------------------------------------------- 404
def not_found():
    root = "/peekly/"
    body = f"""
<main id="main" class="page">
<div class="wrap">
<article class="prose glass" style="text-align:center;margin-inline:auto">
<h1>That page <span class="grad">peeked out.</span></h1>
<p>We couldn&rsquo;t find what you were looking for.</p>
<p><a class="btn primary" href="{root}">Back to Peekly</a></p>
</article>
</div>
</main>
"""
    page = head("Page not found | Peekly", "This page could not be found.", "404.html", root, None, noindex=True)
    write("404.html", page + header(root) + body + footer(root))


def static_files():
    urls = ["", "privacy/", "terms/", "support/"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"<url><loc>{SITE}/{u}</loc><lastmod>{UPDATED}</lastmod></url>")
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    write(".nojekyll", "")
    manifest = {
        "name": "Peekly", "short_name": "Peekly",
        "description": "Peek at any public profile.",
        "start_url": "./", "scope": "./", "display": "browser",
        "background_color": "#0c0c0d", "theme_color": "#0c0c0d",
        "icons": [
            {"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }
    write("manifest.webmanifest", json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    home()
    privacy()
    terms()
    support()
    not_found()
    static_files()
    print("built into", OUT)
