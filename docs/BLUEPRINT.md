# SIGNAL — Production blueprint v0.1

**Status: provisional.** Exact Task 3 prompt and rubric are the next required input; the website's subject and required features must be confirmed before final production. This is not a submitted or accepted assessment.

## Creative direction
A digital field guide that feels like a game-lobby safety console. Use a dark, nearly black graphite ground, warm-white type, restrained ice-blue and acid-green accents, and a distinctive circular signal instrument. Contrast calm editorial reading with one purposeful interactive scene at a time. The instrument responds to safety settings as an illustrative system, not a risk prediction. No fake scanning, mandatory introductory waits, invented metrics, or gratuitous glassmorphism. Use authentic, licensed game screenshots/photography only where they explain a topic; source each image and keep a local compressed copy when rights allow.

## Provisional journey (based on Tasks 1–2; replace if Task 3 differs)
1. Entry: establish why positive gaming and safety can coexist; two clear entry paths.
2. Safety control lab: test fictional privacy, communication, purchase and reporting preparation controls; explain consequences rather than scoring real-world risk.
3. Scenario studio: practise an appropriate response to unwanted contact, bullying, requests for personal information or a purchase scam; give feedback and let learners retry.
4. Game atlas: compare Roblox, Fortnite, Minecraft and Among Us using documented safeguards, limitations and dated source links. No numerical platform rankings.
5. Developer studio: show why private defaults, reporting, accessible moderation and age-appropriate settings matter; demonstrate design choices.
6. Family mode: actionable co-play, check-in and healthy-balance guide; printable checklist.
7. Help pathway: calm evidence collection where safe, platform reporting where appropriate, stopping contact, trusted-adult support, eSafety's current reporting advice and urgent help for immediate danger.
8. Sources, attribution and assessment mapping.

Prototype includes an initial settings lab, one decision scenario and a short help route. It deliberately does not include unfinished simulated pages or real messaging. Full build scope awaits the task prompt.

## Tool decision matrix
| Tool | Decision | Purpose |
|---|---|---|
| Vite | Adopt for full build if dependencies are needed | Small static bundle; GitHub Pages repo base path |
| Native HTML/CSS/JS | Adopt now | Accessible controls and a zero-install prototype |
| Astro | Alternative to Vite+React | Static content islands if content becomes the main focus; do not combine unnecessarily |
| Motion | Preferred animation library candidate | Meaningful layout and scroll animation; reduced motion support |
| GSAP ScrollTrigger | Alternative for complex scene choreography | Use only if Motion cannot achieve the required effect; one motion owner |
| Lenis | Optional | Smooth desktop scroll; bypass on reduced motion, touch or incompatible environments |
| Three.js | Optional visual layer | Single lazy-loaded scene, capped pixel ratio; HTML fallback and disposal; never encode essential text in WebGL |
| LDRS / UI Ball | Optional | Actual async loading indicator only; avoid forced loading delays |
| Uiverse Galaxy | Select individual MIT components | Review accessibility and attribute original authors; normalize to our design tokens |
| Radix Primitives | Adopt if React is selected | Accessible dialogs, tabs and switches; native controls otherwise |
| Lucide | Candidate for utility icons | Consistent iconography; preserve license |
| Playwright + axe-core | Adopt in full build | Interaction, keyboard, viewport and accessibility regression testing |
| Canva | Optional art direction | Produce a visual reference, not a raster replacement for UI |
| Higgsfield | Optional asset production | Only if authentic or permitted media cannot meet the brief and account authorization/rights are clear; no paid generation required |
| GitHub connector | Adopt | Version controlled source and documentation; inspect CI results |
| Browser connector | Optional | Device-specific verification if connected and supported |

### References checked
- eSafety: https://www.esafety.gov.au/young-people/online-gaming
- eSafety parents: https://www.esafety.gov.au/parents/issues-and-advice/gaming
- eSafety research: https://www.esafety.gov.au/research/the-risks-and-benefits-of-online-gaming-for-children-and-young-people
- Vite deployment: https://vite.dev/guide/static-deploy.html
- Astro Pages: https://docs.astro.build/en/guides/deploy/github/
- Motion: https://motion.dev/docs/scroll and https://motion.dev/docs/lenis
- Lenis: https://github.com/darkroomengineering/lenis
- GSAP: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- Three: https://threejs.org/docs/pages/WebGLRenderer
- LDRS: https://uiball.com/ldrs/
- Uiverse: https://github.com/uiverse-io/galaxy
- Radix: https://www.radix-ui.com/primitives
- Lucide: https://lucide.dev/
- Playwright: https://playwright.dev/docs/accessibility-testing

## Engineering rules
No backend, accounts, analytics, real contact, or collection of personal data. Use relative asset paths. No content locked behind motion, hover, or quiz results. Avoid forced smooth scrolling; no auto-playing audio. Ensure visible focus, keyboard operability, contrast, responsive type, and reduced-motion CSS. Use real progress indicators only. A single renderer/RAF owner if 3D is implemented; dispose off-screen resources and use a static fallback. Keep dependencies pinned and licenses recorded; inspect school-device constraints before adding costly effects.

## Acceptance gates
- G0: exact task wording, rubric, audience, presentation conditions; requirement-to-section traceability.
- G1: source/claim ledger and asset licensing; each interactive state storyboarded.
- G2: mobile and desktop art-direction prototype; verify core reading order without JS.
- G3: implement required modules, no placeholder interactions; keyboard and reduced motion support.
- G4: Playwright flows for every interaction, axe review plus manual checks, screen size coverage, no console errors, broken links or missing assets; check Chrome and Safari where available.
- G5: GitHub Pages configuration and live URL verification, teacher-friendly walkthrough, known limitations and final evidence.
 
No final grade or deployment claim until evidence exists. Initial prototype is not a production release.
