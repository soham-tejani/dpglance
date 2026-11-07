# Play Console declarations: suggested answers

Play Console > Policy and programs > App content. Check each answer against the Console's wording on the day you
submit. This is engineering guidance, not legal advice.

| Declaration | Suggested answer | Why |
|---|---|---|
| Privacy policy | https://soham-tejani.github.io/peekly/privacy/ | Required for every app. Must also be reachable inside the app (see CHECKLIST.md, blocker 1). |
| App access | All functionality is available without login | Peekly has no accounts. |
| Ads | **Yes, the app contains ads** | Rewarded ads via Google AdMob. |
| Advertising ID | **Yes**, used for advertising | The manifest declares `com.google.android.gms.permission.AD_ID`. If you ship a build without ads, remove the permission and answer No. |
| Target audience and content | Choose age groups **16 and over** (or 13 and over only after reading the Families and ads requirements) | Snapchat's own minimum age is 13, but not targeting children avoids Families Policy obligations. Do not select any under-13 group. Peekly is not designed for children and ads are not child-directed. |
| Appeals to children | No | |
| Content rating (IARC questionnaire) | Answer every question truthfully. Peekly shows, from a third-party social platform, public profile pictures and highlights that you do not control. Be honest about that user-generated content in the questionnaire. Expect a teen-level rating; do not try to push it lower. | Misstating content is a common reason for removal. |
| Government app | No | |
| Financial features | None | |
| Health features | None | |
| News app | No | |
| Data safety | See `DATA_SAFETY.md` | |

## Permissions in the manifest (version 0.1.0)

| Permission | Purpose | Sensitive? |
|---|---|---|
| `INTERNET` | Look up profiles, load images, show ads | No |
| `ACCESS_NETWORK_STATE` | Ads SDK network check | No |
| `com.google.android.gms.permission.AD_ID` | Advertising ID for ads | Declared in Console (see above) |

No storage permission is requested (files are saved with MediaStore on Android 10 and later). No background
clipboard access is used; the clipboard is read only while the app is in the foreground.

## Policy areas most likely to be reviewed for this app

1. **Impersonation and intellectual property.** Name, icon and listing must not suggest affiliation with Snap.
   The non-affiliation line must appear in the listing and on the website (it does).
2. **Deceptive behaviour / downloader-style apps.** The listing must describe a public-profile *viewer*, with
   saving presented as personal use. Never use the words "downloader" or "Snapchat downloader".
3. **User data.** The privacy policy, in-app disclosure and Data safety form must agree with each other and with
   what the app does. The app explains clipboard use on first run ("Before you start" screen).
4. **Ads.** Rewarded ads must be user-initiated and clearly labelled. Never click your own live ads.
5. **Third-party terms.** Peekly depends on a website it does not control. Have a lawyer review the concept
   (the app repo's doc 6 explains the risk).
