# SIGNAL — confirmed production plan

Confirmed user brief (25 November 2026): Research different types of online games and evaluate their safety features. Present findings to the class in an interesting way, including how game developers can help protect players. This is for fun, not a marked assessment.

## Scope and acceptance
- Four distinct game types: Roblox user-created experiences; Fortnite competitive multiplayer; Minecraft sandbox/servers; Among Us social deduction.
- Explain safeguards and limitations for every game; comparison table; independent regulator findings, with Among Us explicitly outside the 2026 transparency report.
- Developer Studio: five interactive protection choices, three-layer model and clear explanation. Counts selections, never predicts individual safety.
- Decision Studio: three fictional choices with feedback, next/previous/reset, no real messaging.
- Player, developer and community takeaway; linked primary sources.
- No mandatory loader, forced scrolling, analytics, backend, login or personal data collection.
- Responsive, keyboard-operable, visible focus, reduced motion and a static reading path. Actual browser acceptance is still required.

## Tool choices
Native HTML/CSS/JavaScript and system fonts for this release, no install or CDN runtime. CSS-only signal instrument, grid, motion and progress. The previous tool shortlist is retained as historical research; Three.js, Lenis, Motion, LDRS, Uiverse and media generation are intentionally not bundled until a feature needs them. This avoids excess dependencies and allows school devices to load the content even when CDNs are blocked. No invented game screenshots or assets. Original typographic identifiers are not game logos. Add real appropriately licensed imagery only after verifying source/rights; current release is a designed text-first version.

## Evidence
All case claims link to developer sources. The October 2026 eSafety transparency findings distinguish pre-publication Island review from post-publication detection tools, and third-party server moderation limitations. The report covers Roblox, Fortnite, Minecraft and Steam, not Among Us. Numbers 89%, 79%, 40% refer to 2024 Australian youth gaming research as summarised on that page. They are not game-specific statistics.
 
## Presentation walkthrough (5–7 min)
1. Start with three research numbers and ask who has played with someone unfamiliar.
2. Show the four game types and compare strengths and limitations. Expand one evidence panel.
3. Discuss the comparison table; explain why no game is automatically safe.
4. Let classmates choose protections in Developer Studio. Discuss what prevention, response and improvement each add.
5. Try one Decision Studio case and explain the best response. End with the shared responsibility takeaway.
6. Open source library if the class asks for evidence.

## Release checks
Structural and data coverage checks in CI. Live desktop/mobile layouts, interaction playback, keyboard, reduced-motion and deployment require actual browser verification. No final acceptance claimed from file creation alone.
