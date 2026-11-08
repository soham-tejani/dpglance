# Data safety form: suggested answers

Play Console > Policy and programs > App content > Data safety.

These answers are derived from (a) the app's source code at version 0.1.0 and (b) Google's published disclosure for
the Google Mobile Ads SDK: https://developers.google.com/admob/android/privacy/play-data-disclosure
(that page applies to SDK version 25.5.0 and says to update older SDK versions to keep disclosures accurate).

> **Before submitting:** re-read Google's page above for the exact SDK version you ship, and compare it with the
> Console's current wording. If you later add analytics, crash reporting, Firebase or any other SDK, this form
> and the privacy policy must be updated first. This is engineering guidance, not legal advice.

## What the app actually does with data

| Behaviour | Where in the code | Data leaves the device? |
|---|---|---|
| Reads clipboard text on app focus and on tapping Paste, in memory only | `data/ClipboardReader.kt` | No |
| Requests the public profile page and media for a username the user chose | `data/SnapProfileFetcher.kt`, `data/Downloader.kt` (hosts limited to snapchat.com and sc-cdn.net) | Yes, directly device to Snap. Never touches the developer. |
| Keeps up to 30 recent profiles and an "intro seen" flag | `data/HistoryStore.kt` (private SharedPreferences) | No. `allowBackup="false"` |
| Saves files with MediaStore to Pictures/DPGlance and Movies/DPGlance | `data/Downloader.kt` | No |
| Rewarded ads and consent | `ads/RewardedAdGate.kt`, `ads/ConsentManager.kt` (Google AdMob and UMP) | Yes, to Google |
| Developer-operated server, analytics, crash reporting, accounts | None present | n/a |

## Section: Data collection and security

| Console question | Suggested answer |
|---|---|
| Does your app collect or share any of the required user data types? | **Yes** (through the Google Mobile Ads SDK) |
| Is all of the user data collected by your app encrypted in transit? | **Yes.** The app blocks cleartext traffic, and Google states ad SDK data is encrypted in transit with TLS. |
| Do you provide a way for users to request that their data be deleted? | **Verify in Console.** The developer holds no user data and there are no accounts. Ad data is held by Google and controlled through Android and Google ad settings. Answer truthfully for your situation; the privacy policy (section 6 and 8) explains the controls. |

## Data types to declare (all come from the Google Mobile Ads SDK)

Google says the SDK "collects and shares ... automatically for advertising, analytics, and fraud prevention
purposes". Map its four rows to Play's categories like this:

| Google's row | Play data type | Collected | Shared | Optional? | Purposes to tick |
|---|---|---|---|---|---|
| IP address (may estimate general location) | Location > **Approximate location** | Yes | Yes | No (automatic) | Advertising or marketing, Analytics, Fraud prevention, security and compliance |
| User product interactions (app launch, taps, video views) | App activity > **App interactions** | Yes | Yes | No | Advertising or marketing, Analytics, Fraud prevention, security and compliance |
| Diagnostic information (launch time, hang rate, energy use) | App info and performance > **Diagnostics** | Yes | Yes | No | Advertising or marketing, Analytics, Fraud prevention, security and compliance |
| Android advertising ID, app set ID | Device or other IDs > **Device or other IDs** | Yes | Yes | The ad ID collection is optional for users (reset or delete in Android settings) | Advertising or marketing, Analytics, Fraud prevention, security and compliance |

Notes:

- Google's page gives one shared purpose statement for the whole group, not one per row, so the same three
  purposes are listed for each row. Tick only purposes you can justify.
- "Shared" is used because Google's page says the SDK "collects and shares" these types. Do not downgrade it.

## Data types NOT to declare, and why

| Data | Why it is not declared |
|---|---|
| Clipboard text | Processed in memory on the device and never transmitted off-device, so it is not "collected" under Play's definition. |
| The username sent to snapchat.com | It goes directly from the device to a third party as part of a user-initiated lookup the user expects. The developer never receives it. **Verify against Play's current definition of "sharing" and its user-initiated-transfer exception** and mention it in the policy (it is already there). |
| Recent profiles list | Stored only on the device. |
| Saved media | Written to the device's gallery only. |
| Name, email, phone, precise location, contacts, photos library, microphone, camera, financial or health data | Never requested. |

## Other App content declarations

See `DECLARATIONS.md`.
