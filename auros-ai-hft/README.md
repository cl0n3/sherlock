# AI in High-Frequency Trading — deck for Auros

A [Marp](https://marp.app) presentation: how the quant giants (**XTX, Optiver, Citadel**) use AI,
tailored for a crypto-market-making audience (**Auros**).

The argument is built around three messages:

- **A — It's here.** AI is table-stakes in quant trading; competitors are already spending.
- **B — Code = P&L.** Legacy code only matters if it's making money; AI collapses the cost of rewriting the rest.
- **C — People.** Engineering becomes a different skill — the best people matter *more*, or you accelerate poor outcomes.

## Files

| Path | What it is |
|------|------------|
| `deck.md` | The slides (Marp markdown). **Edit this.** Speaker notes are the `<!-- ... -->` comments. |
| `themes/auros.css` | Dark "quant terminal" theme. Edit the `:root` colours to rebrand to Auros. |
| `assets/*.svg` | Hand-authored charts (no dependencies): XTX & Optiver financials, the speed→signal diagram. |
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

- [ ] Replace the presenter name / date on the **title slide**.
- [ ] **Confidentiality:** slides 9 & 19 use my read of Optiver internals — confirm what's cleared to share with Auros.
- [ ] **Verify headline numbers** against primary filings (Companies House for XTX; Optiver results for Optiver) — see `sources.md`.
- [ ] Optional: rebrand `themes/auros.css` `:root` colours; drop in an Auros logo on the title slide.

## Customising

- **Slide count / order:** add or remove `---`-delimited sections in `deck.md`.
- **Two-column layout:** wrap content in `<div class="cols"> … </div>` (or `.cols3`), with a blank line
  around any markdown inside each column so it renders.
- **Evidence badges:** `<span class="badge v">Verified</span>`, `badge i` (inference/insider), `badge m` (myth).
