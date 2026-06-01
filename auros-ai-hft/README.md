# AI & the Speed Moat — deck for Auros

A [Marp](https://marp.app) presentation on the **state of AI across industry, the economy and trading**,
told through ~50 sourced company examples and tailored for a crypto-market-making audience (**Auros**).

**Thesis:** *time-to-market is the most important metric in any trading or technology business — speed is the
moat, and AI is the multiplier.* The deck is organised around four forces that compress time-to-market —
**(1) developer/worker productivity, (2) autonomous system building, (3) cost reduction, (4) R&D** — then a
**crypto-trading deep-dive** (named competitors, agent-native exchanges, the on-chain agent frontier, and the
TradFi quant bar).

## Files

| Path | What it is |
|------|------------|
| `deck.md` | The slides (Marp markdown). **Edit this.** Speaker notes are the `<!-- ... -->` comments. |
| `themes/auros.css` | Dark "quant terminal" theme. Edit the `:root` colours to rebrand to Auros. |
| `assets/*.svg` | Hand-authored visuals (no dependencies): time-to-market compression, AI code-adoption, latency→velocity, XTX financials. |
| `tools/inline-assets.mjs` | Post-build step that inlines the SVGs into `deck.html` so it's a single portable file. |
| `sources.md` | Every figure → source URL, with the verified / inference / myth key. |
| `deck.html` | Rendered, self-contained slides — open in any browser. (`deck.pdf` / `deck.pptx` if you build them.) |

## Render

```bash
npm install        # one-time: installs @marp-team/marp-cli locally
npm run build      # → deck.html  (self-contained, no browser needed)
npm run pdf        # → deck.pdf   (needs Chromium; see note)
npm run pptx       # → deck.pptx  (editable in PowerPoint / Google Slides)
npm run watch      # live re-render to deck.html while you edit
```

**PDF / PPTX note:** those exports drive a headless **Chromium** via Marp. In a locked-down/offline
environment Chromium may be unavailable — `npm run build` (HTML) always works. To render PDF/PPTX locally,
either let Marp download its browser, or point it at an installed one:

```bash
CHROME_PATH="/path/to/google-chrome" npm run pdf
```

Open `deck.html` in any browser; press <kbd>F</kbd> for fullscreen, arrow keys to navigate.
For presenter notes, export PPTX or use Marp's preview.

## Before you present — checklist

- [ ] Set the date / "prepared for Auros" line on the **title slide** (presenter name intentionally omitted).
- [ ] **Verify headline numbers** against the primary sources in `sources.md` — several are company-reported or 2026 forecasts.
- [ ] Sanity-check the **crypto-competitor** claims you'll say out loud (most market-maker internals are flagged inference).
- [ ] Optional: rebrand `themes/auros.css` `:root` colours; drop in an Auros logo on the title slide.

## Customising

- **Slide count / order:** add or remove `---`-delimited sections in `deck.md`.
- **Two-column layout:** wrap content in `<div class="cols"> … </div>` (or `.cols3`), with a blank line
  around any markdown inside each column so it renders.
- **Evidence badges:** `<span class="badge v">Verified</span>`, `badge i` (inference/insider), `badge m` (myth).
