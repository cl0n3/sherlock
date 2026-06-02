---
marp: true
theme: auros
paginate: true
footer: 'AI in trading & engineering · prepared for Auros · confidential draft'
---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _footer: '' -->

![w:320](assets/cover-heptagon.svg)

# A tenth of the people

## What AI is doing to trading & engineering — and the firm that already proved it

<span class="small muted">Prepared for Auros · June 2026</span>

<!--
Speaker: Let the cover sit. The title is the whole talk in four words. Don't explain it yet.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: '' -->

<span class="kicker">where we're going</span>

# Optiver-level revenue. A tenth of the people.

## You've probably never heard of them. By the end of tonight you'll know exactly how — and why it's now your game too.

<span class="small muted">Tonight: where AI actually is · what it does to our teams · and the firm that proves it.</span>

<!--
Speaker: COLD OPEN — do not warm up. Say line one, pause, let "a tenth of the people" land. That's XTX, but don't name them yet — the reveal is Part 4. Promise the payoff, then go straight into the state of AI.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Part 1
## The state of AI

<!--
Speaker: Quick, current, shared vocabulary. Set the pace before we get tactical.
-->

---

## The tools at the frontier

<div class="cols">
<div>

- **Claude Code** — terminal/IDE agent; writes the majority of Anthropic's own code
- **OpenAI Codex** — cloud agent, runs tasks in parallel
- **Cursor** — AI-native IDE (firm-wide at Coinbase, Optiver)

</div>
<div>

- **GitHub Copilot (agent)** — issue → pull request
- **Gemini CLI / Amazon Q** — agents in the terminal & cloud
- **Devin (Cognition)** — autonomous software engineer

</div>
</div>

> These aren't autocomplete. They read a codebase, plan, edit across files, run the tests, and open the PR.

<!--
Speaker: The shift: the unit of work went from "a suggestion" to "a task." A year ago, demos. Now, production code daily.
-->

---

## AI vs ML vs LLMs — the same family

![w:560](assets/ai-ml-llm.svg)

<span class="src">So we use words the same way: "AI" is the field, "ML" learns from data, "deep learning" is neural nets (incl. transformers), "LLMs/GenAI" are the frontier. Trading uses the whole stack — not just chatbots.</span>

<!--
Speaker: Defuse jargon fast. The edge in trading lives across all of it — keep this to ~30 seconds.
-->

---

<span class="kicker">Part 1 · the pace</span>

## What's actually true right now

- **The pace is absurd** — last year's state-of-the-art is this year's free tier
- **Anthropic's own code is now mostly written by Claude** — the toolmakers eat their own cooking
- **Inference is ~10× cheaper every year** — capability-per-dollar in free-fall (the good kind)
- **It's horizontal** — the same model does code, law, medicine *and* markets. This is electricity, not an app.

<!--
Speaker: Fewer, harder facts. The one to hammer: any plan that assumes today's limits is wrong within two quarters. Build for where it's going.
-->

---

<span class="kicker">Part 1 · the proof</span>

## It's already writing the code

![w:540](assets/ai-adoption.svg)

> Half of new code at serious engineering shops is already machine-written. That's the floor — not the ceiling.

<!--
Speaker: Concrete proof of "it's here." A quarter-to-a-half of new code, with humans on review. Baseline, not frontier.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Part 2
## What it does to our teams

<!--
Speaker: The heart of the talk. But first — show, don't tell.
-->

---

<span class="kicker">Don't take my word for it</span>

## Watch it build

<p style="text-align:center; margin:18px 0;"><span style="display:inline-block; border:2px solid #5cb8a8; border-radius:14px; padding:16px 40px; font-size:38px; font-weight:700; letter-spacing:3px; color:#8fd0c4;">LIVE&nbsp;DEMO</span></p>

- An agent builds a small **exchange-connectivity adapter** from a one-paragraph spec — writes it, runs the tests, opens the PR
- ~90 seconds. The point isn't the code. It's the **cycle time.**

<!--
Speaker: DEMO (~90s) — live or pre-recorded.
Suggested prompt in a small repo: "Add a connectivity adapter for <venue> implementing our ExchangeAdapter interface — connect, subscribe to the order book, normalise to our internal types. Write unit tests against the recorded fixtures and open a PR."
Narrate: it reads the existing interface, writes the code, runs the tests, fixes its own error, opens the PR.
Fallback: have a screen-recording ready in case wifi/login fails.
The line to land: "that adapter used to be a two-day ticket."
-->

---

<span class="kicker">The shift</span>

## Your engineers just became agent-managers — and it's not optional

![w:520](assets/ttm-compression.svg)

- The job moves from **writing code** to **directing and reviewing** the agents that write it
- Refuse, and you're **hand-writing assembly while competitors ship in C++** — the jury is in

<!--
Speaker: Two ideas, one breath: the role changed (architect/agent-manager), and opting out is a competitive choice. The assembly-vs-C++ line lands because everyone here gets abstraction levels.
-->

---

<span class="kicker">The catch</span>

## Everyone's a manager overnight

- Hand every engineer a team of agents and you've made them **all managers** — with no training
- A hard transition: delegation, review, trust, letting go of the keyboard
- **Some won't want to take the step** — that's information you need early

> The tools are the easy part. Re-skilling the people is the program.

<!--
Speaker: The empathy + realism beat. Most failed rollouts are change-management failures, not tooling failures. Name that some of your best ICs may resist. This is your best line — give it a moment.
-->

---

<span class="kicker">How not to screw it up</span>

## Get the substrate right

<div class="cols">
<div>

- **Multi-agent code review** — a panel, not one model; different models catch different bugs
- **Skills over chats** — build reusable tools, not one-off prompts
- **Monorepos + real tests** — so agents see the whole picture and can't break it quietly

</div>
<div class="card">

### And it's not just engineering
Your **data** is the moat — you can't escape the clean-up, but **AI can help.** **Legal, finance, HR** are on the same curve. This is a **firm-wide** program.

</div>
</div>

<!--
Speaker: The practical "how," compressed. Multi-agent review is the non-obvious one. Tests + monorepo are AI-enablement, not overhead. Then widen the lens: every specialist function is on engineering's curve.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Part 3
## What firms are actually doing

<!--
Speaker: From principles to evidence — my read from inside Optiver and the wider industry. Say verbally these are recollections.
-->

---

<span class="kicker">Optiver · my account <span class="badge i">Insider</span></span>

## From a standing start to serious money

- When I left, Optiver was **only just starting** its AI journey
- Now: **major investment in systematic trading** — ~**€500M NTI** on the Austin desk at that time
- **~€100M** on a **private GPU cluster & data centre** — and **more is being spent this year**

<span class="src">My recollection / insider perspective — figures approximate and not independently verified.</span>

<!--
Speaker: CONFIDENTIALITY — internal recollections of a former employer; say only what you're comfortable sharing. Keep figures round and "at that time." Story: a late starter now spending at scale.
-->

---

<span class="kicker">Optiver · my account <span class="badge i">Insider</span></span>

## "It won't work here." It worked.

- The objection everyone had: *"our engineering is too specialised — AI can't help us"*
- Then **AI-only connectivity** went **into production** for US cash trading — many markets, connected fast
- It cleared the **"ATR moral hazard"** that had stalled this work for years
- Today: **dedicated AI-enablement teams** with **partner-level sponsorship**

> The "we're different" excuse died at the firm most likely to be right about it.

<!--
Speaker: CONFIDENTIALITY applies. This is the reversal story — tell it with a beat before the punchline. The read-through for Auros: the "too specialised for this" objection is exactly what got disproven, once the top sponsored it.
-->

---

<span class="kicker">Optiver & IMC · my account <span class="badge i">Insider</span></span>

## AI Apps Engineers, in the wild

- **Both Optiver and IMC** use **AI Apps Engineers** extensively
- Concrete wins: **faster triage** and **faster market re-entry** after issues
- Removes a **stressful, mundane on-call task** from humans — and **improves availability metrics**

> A boring, painful job done better by AI — that's where the early ROI actually shows up.

<!--
Speaker: The most relatable, least-hype example: operational toil. Availability up, a horrible job easier. This is the pattern to copy first at Auros.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Part 4
## The reveal: XTX

<!--
Speaker: The firm from the cold open. Pay it off as a story.
-->

---

<span class="kicker">Case study · XTX</span>

## The contrarian bet

- 2015: all of HFT was racing on **latency** — microwave towers, co-location, nanoseconds
- **Alexander Gerko** bet the other way: **out-predict, don't out-race**
- He put **transformer techniques** — the precursor to today's LLMs — on raw **PCAP** market data, **before the paper was even famous**
- The wager: **prediction quality + compute** beats raw speed

<!--
Speaker: Tell it like a thriller. The villain is the arms race everyone else ran. Gerko (maths olympiad) zigs. The "transformers on PCAP before it was cool" line is the hook — then turn the page to the payoff.
-->

---

<span class="kicker">Case study · XTX</span>

## The payoff

![w:540](assets/xtx-revenue-timeline.svg)

> **Optiver-level revenue — with roughly a tenth of the headcount.**

<span class="src">Revenue: Companies House via FX News Group / Finance Magnates. Headcount approximate (group). 2016–19 single entity; 2020+ combined — see chart note.</span>

<!--
Speaker: This is the reveal the whole talk has been building to. Let the gap between the two lines speak: billions in revenue, a few hundred people. Pause on it.
-->

---

<span class="kicker">Case study · XTX</span>

## Why it rhymes with Auros

<div class="cols">
<div>

- Prices **50,000+ instruments** across equities, fixed income, FX, commodities **and crypto**
- **$250bn traded/day across 35 countries**; deep liquidity in **10,000+ assets**
- A **breadth** play — *not* options-style depth (not competitive with options trading as at 2025)

</div>
<div class="card">

### The parallel
Breadth across many instruments and venues, won with **models and connectivity** rather than options-style depth — that's **Auros's game too.**

</div>
</div>

<span class="src">Figures: xtxmarkets.com — over 50,000 instruments · 10,000+ assets · $250bn/day · 35 countries.</span>

<!--
Speaker: Bring it home. XTX's edge — breadth + ML + connectivity across a huge instrument universe — is structurally close to crypto market making. The lesson travels directly.
-->

---

## So what — for Auros

<div class="cols">
<div>

- **It's a must-have** — the leaders are already compounding
- **Re-skill the people** — everyone's an agent-manager now; help them
- **Fix the substrate** — tests, monorepos, clean data, multi-agent review

</div>
<div>

- **Sponsor it from the top** — partner-level, like Optiver
- **Start with the toil** — triage, re-entry, connectivity — where ROI is obvious
- **Breadth + models + connectivity** — XTX shows where that leads

</div>
</div>

<!--
Speaker: Concrete, quarter-sized asks. Then the close.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# A tenth of the people.

## That's not XTX's secret — it's the new default. The only question is which side of that ratio Auros wants to be on.

<!--
Speaker: The mic drop. Callback to the open. Say it, hold the beat, stop talking. Don't undercut it with "any questions?" — let it sit, then take questions off the appendix.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Appendix
## Evidence & references

<!--
Speaker: Reference material for Q&A — three buckets. Leave up while questions come.
-->

---

<span class="kicker">Appendix A</span>

## TradFi firms spending big

<div class="cols">
<div>

- **Citadel Securities** — AI spend rising; entered **crypto market-making** (Feb 2025)
- **Jane Street** — **$6B** CoreWeave AI-compute commitment
- **Bridgewater** — **$2B** "AIA" ML fund
- **XTX** — 25k GPUs, transformers (see case study)

</div>
<div>

- **Two Sigma** — DL on unstructured data
- **Renaissance** — decades of statistical ML
- **Hudson River Trading** — sequence models / LLMs on market data
- **Man AHL / JPMorgan (LOXM)** — production ML in execution

</div>
</div>

<span class="src">Sources in <code>sources.md</code>. Verified public unless flagged.</span>

---

<span class="kicker">Appendix B</span>

## Economic trends

<div class="cols">
<div>

- **AI capex** — ~**$500B+/yr** hyperscaler spend (2026)
- **Code adoption** — Google ~25%+, GitHub 46%, Coinbase 50% target
- **Productivity** — Copilot +55% task speed; Anthropic 81% median time saved
- **Enterprise** — Amazon Q **$260M**; Klarna −40% cost/txn; IBM AskHR −40%

</div>
<div>

- **R&D** — AlphaFold (Nobel), GNoME (2.2M materials), AlphaChip
- **Autonomy** — Waymo 450k rides/wk; Amazon 1M robots; Devin @ Nubank/Goldman
- **Markets** — AI-agent & automated-trading TAMs growing 40%+ CAGR

</div>
</div>

<span class="src">Company-reported / press / analyst; several 2026 figures are forecasts. See <code>sources.md</code>.</span>

---

<span class="kicker">Appendix C</span>

## Crypto / DeFi firms embracing AI

<div class="cols">
<div>

- **Wintermute** — ML risk/MM; ~$5B/day
- **B2C2** — vector/time-series ML; $2T+ volume
- **Keyrock · Flowdesk** — ML across 85+ venues; 1M+ orders/day
- **FalconX · DWF · Amber** — LLM copilots; autonomous trading agents
- **GSR · Jump · Cumberland** — DL/RL/LLMs at scale

</div>
<div>

- **Exchanges going agent-native** — Coinbase AgentKit, Kraken CLI (MCP), OKX Agent Trade Kit, Binance AI
- **On-chain agents** — Virtuals (~$479M Q1), Bittensor (~$43M Q1), ai16z/ElizaOS — *real revenue, lots of hype* <span class="badge m">M</span>

</div>
</div>

<span class="src">Most market-maker internals are proprietary — ML use sourced from statements/jobs; specifics are <span class="badge i">inference</span>.</span>

---

## Sources & method

- **XTX:** Companies House (`09415174`, `12300034`, `12832334`); FX News Group; Finance Magnates; xtxmarkets.com
- **TradFi:** CoinDesk, Bloomberg, Fortune, company disclosures (Citadel, Jane Street, Bridgewater, Two Sigma, HRT, Man AHL, JPMorgan)
- **Economy:** Anthropic & GitHub productivity research; AWS; OpenAI case studies; DeepMind; analyst market reports
- **Crypto:** company statements; AWS/Google Cloud case studies; Messari; 1kx
- **Optiver / IMC (Part 3):** my own insider perspective — directional, not public disclosures

<span class="src">Full URL list in <code>sources.md</code>. Key: unbadged = sourced · <span class="badge i">I</span> inference/insider · <span class="badge m">M</span> hype-flagged. Verify headline figures before presenting.</span>

<!--
Speaker: Close on rigour. Part 3 is recollection, not citation — that honesty protects you.
-->
