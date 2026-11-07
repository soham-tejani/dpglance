# Pre-submission checklist

Status as of 8 November 2026, app version 0.1.0. Items marked **BLOCKER** must be done before Play will accept or
keep the app. Items marked *you* need a decision or an account only you can provide.

## Blockers found in the app (as of 0.1.0)

1. **BLOCKER: no privacy policy link inside the app.** Play requires the policy to be reachable from the store
   listing *and* inside the app. The app has a first-run "Before you start" screen but no screen or button that
   links to the policy. Add an About/Info entry that opens
   https://soham-tejani.github.io/peekly/privacy/ and repeat the "not affiliated with Snap Inc." line there.
   The same screen should show a "Privacy options" row that calls `ConsentManager.showPrivacyOptions()` when
   `privacyOptionsRequired` is true. That method exists in `ads/ConsentManager.kt` but no screen uses it yet, and
   Google's consent framework expects EEA and UK users to be able to change their choice.
2. **BLOCKER: Google's test AdMob IDs are still in `app/build.gradle.kts`.** Replace the app ID
   (`ca-app-pub-3940256099942544~3347511713`) and rewarded unit ID (`.../5224354917`) with your real AdMob IDs
   for the release build. Never click your own live ads. Keep test IDs for debug builds.
3. **BLOCKER: the release build is unsigned.** Create an upload keystore, configure `signingConfigs`, and build an
   Android App Bundle (`./gradlew bundleWithAdsRelease`). Enrol in Play App Signing. Keep the keystore backed up.
4. **Decide the build to ship.** The `adfree` flavor has a different application ID (`.adfree`) and shows no ads.
   Decide whether it is distributed at all. The privacy policy and declarations on this site describe the
   ad-supported `withAds` build. If you ever publish an ad-free build, remove the `AD_ID` permission and update the
   declarations.

## Store listing assets

- [ ] Real phone screenshots (min 2) captured from a device. See `LISTING.md` for rules.
- [ ] Feature graphic 1024x500: `graphics/feature-graphic-1024x500.png` (ready)
- [ ] App icon 512x512: `graphics/app-icon-512.png` (ready)
- [ ] Listing text pasted from `LISTING.md`
- [ ] *you:* a public contact email in the Console (use a dedicated address)

## Console forms

- [ ] Privacy policy URL, Data safety, Ads, Advertising ID, Target audience, Content rating: see
      `DATA_SAFETY.md` and `DECLARATIONS.md`
- [ ] Complete the content rating questionnaire truthfully
- [ ] Review the Console's "Policy status" and pre-launch report before rollout

## Developer account

- [ ] *you:* decide the publisher identity (personal or company). Open question Q7 in the app repo's doc 8.
      Update the privacy policy and terms on this site if you publish under a registered company name.
- [ ] Complete Google's current developer verification and account requirements. New personal accounts may need a
      closed test with a minimum number of testers for a minimum number of days before production access. **Check
      Play Console Help for the current numbers.**

## Advertising setup (recommended)

- [ ] Create the AdMob app and rewarded ad unit; link the app to its Play listing once published.
- [ ] Configure the consent message in AdMob > Privacy and messaging (the app already uses Google's UMP SDK) for
      the EEA and UK, plus any US state regulations you want covered.
- [ ] `app-ads.txt` is verified from the **root** of the developer website domain listed in Play. This site is a
      GitHub *project* page (`soham-tejani.github.io/peekly/`), so its root is not controlled here. If you want
      `app-ads.txt`, serve it from a domain root you control (for example a custom domain or a
      `soham-tejani.github.io` user site).

## Legal and risk

- [ ] Have a lawyer review the concept, privacy policy and terms (the app repo's doc 6 explains the Snapchat
      terms and Play "downloader" risks).
- [ ] Keep the listing and website framed as a **viewer of public profiles**, never a "downloader".
- [ ] Prepare a response process for takedown requests (Support page points creators to GitHub issues).

## Site (already done)

- [x] Home page with SEO tags, Open Graph and Twitter cards, JSON-LD (WebSite, SoftwareApplication, FAQPage)
- [x] Privacy Policy, Terms of Use, Support and reports pages
- [x] Non-affiliation disclaimer on every page
- [x] robots.txt, sitemap.xml, canonical URLs, web manifest, favicons
- [x] No third-party requests: font and scripts are self-hosted, no analytics or cookies
- [ ] After the app is live on Google Play: add the real Play Store link and official badge to the home page, and
      add the listing URL to `sameAs`/`downloadUrl` in the structured data (`tools/build.py`).
