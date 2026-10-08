# Road alerts: Google integration launch requirements

Recorded 2026-10-05. This is a launch gate, not a statement that integration exists. The current GitHub Pages prototype is simulated. No live sharing service is connected.

## Verified boundary

Google Navigation SDK for iOS supports a custom reporting launcher which opens Google's incident reporting panel. Availability must be checked during active navigation. Google processes submissions and votes and may display reports to other Google Maps and Navigation SDK users. Google documents its own approaching-incident prompts. The reviewed documentation does not expose arbitrary submission of NaVue's custom category/subcategory selections or an exact fixed report expiry time.

Google Maps supports custom markers with coordinates and custom icons. Displaying a NaVue marker does not submit an incident to Google's reporting network. Waze consumer screenshots do not establish Google SDK API support. The native iOS SDK is not a drop-in connection for this browser prototype.

Sources:
- https://developers.google.com/maps/documentation/navigation/ios-sdk/real-time-disruptions
- https://developers.google.com/maps/documentation/ios-sdk/reference/objc/Classes/GMSMarker

## Product requirements retained

- Blue triangle with yellow exclamation launcher; original NaVue Option C artwork, compact labels and bottom drawers.
- Eleven main categories; no Place or Debug. Traffic, police, crash, hazard, blocked-lane, weather and animal subtypes supplied as design references. Map feedback, gas prices and roadside assistance have different workflows and must not claim a report or assistance request was sent unless connected.
- Tapping alerts temporarily starts the microphone, readiness beep and truthful listening status, retaining tap input. Restore prior microphone state on completion/cancel/exit. Do not enable speaker guidance.
- Confirmed reports use the incident location, not a moving screen position. Local prototype simulation is explicitly labelled.
- Relevant nearby reports may ask Still there? Yes/No via tap or supported voice. Silence is unknown, never a No vote.

## Required architecture decision before production reporting

Choose whether Google-supported incident reports use Google's native reporting interface, or whether NaVue runs an independent reporting service for the custom interface. Do not imply our custom icons/voice/subtypes directly submit to Google without a supported and tested API. Preserve the custom prototype as a draft until this implication has been explained and the desired production path agreed.

## Must pass before live launch

1. Select and connect the actual production maps/navigation platform. Configure credentials, availability and failure handling on target devices/regions.
2. Prove report submission and acknowledgment on the chosen service. Custom NaVue reports need a backend, location/direction, timestamps, moderation, sharing and lifecycle handling; markers alone are insufficient.
3. Establish source ownership: Google-managed incidents remain under Google's lifecycle. NaVue-managed incidents need separately approved expiry/confidence rules. Do not duplicate or independently extend Google incidents. Avoid conflicting visual/audio prompts; evaluate SDK prompt visibility callbacks.
4. Test stale reports, duplicate submissions, inaccurate/absent location, wrong carriageway, offline/failure cases, expiry without votes, and reconnect behavior. Do not claim zero misinformation or zero bugs.
5. Test supported reporting and approach prompts on actual devices, including speaker off, microphone off, temporary listening permission denied, cancellation, and map attribution/UI overlap.
6. Verify two-device NaVue sharing if the independent service is chosen. Keep demo reports out of all production feeds.
7. Do not call this connected or ready for public navigation until these checks are complete. This will not happen automatically through a Google map integration.

## Approved prototype scope — 2026-10-05, 17:10 Toronto

Proceed only with clearly labelled, explicitly triggered accident and traffic demo warnings. One shared incident warning at a time, optional speech controlled by the existing speaker setting, no microphone activation, and simulated ETA adjustment for the traffic fixture. Keep approved NaVue styling. Pause new custom reporting sub-options and sharing. Existing Option C report-preview design remains a simulation, not a Google reporting implementation. The separate custom-report draft is unpublished and is not approved for production.

The recommended first live integration uses Google's incident system as the single incident-alert source, subject to a real Navigation SDK trial confirming menus, symbols, audio and prompt behaviour. Do not claim replacement of Google-supplied incident icons or cross-source incident deduplication: neither is established by the reviewed public SDK documentation. This supersedes any earlier assumption that the custom interface can be wired directly into Google's incident feed.

## Launch requirements confirmed — 2026-10-07, 22:02 Toronto

Gio requires a NaVue shared reporting service to be built before custom reports are advertised as shared with other NaVue drivers. This is a future build requirement, not authorization to implement it now. Store category/sub-option, incident coordinates/direction and timestamps; provide nearby delivery, duplicate handling, Still there/Gone votes, moderation and expiry. Verify sharing on two devices. The prototype currently has no connected sharing service.

Also require a production Google Navigation SDK integration trial to verify that Google-managed incidents, including police reports originating with Google Maps users, can appear and notify NaVue drivers where supported. Availability depends on region, incident type and Google processing; never promise every submitted report will appear. A Maps JavaScript map or API key alone does not enable native Navigation SDK incident alerts in Safari.

Treat these as two separate integration workstreams. Keep Google incidents in Google's supported presentation/lifecycle and NaVue reports in our service. Reassess the earlier single-source recommendation before combining sources; verify prompt coordination without promising unsupported cross-source deduplication or replacement of Google's icons. Test speaker off/on and avoid overlapping notifications. Re-check official documentation at implementation time:
https://developers.google.com/maps/documentation/navigation/ios-sdk/real-time-disruptions

NaVue onboarding fuel prices, consumption and global measurement settings remain our own approved calculation feature. Preserve them; use selected-route distance with correct unit conversions when live routing is connected. No redesign of that feature is requested by this reporting work.
