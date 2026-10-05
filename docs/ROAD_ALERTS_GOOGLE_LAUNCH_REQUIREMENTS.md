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
