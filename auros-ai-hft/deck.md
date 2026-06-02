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

# AI & the Speed Moat

## The state of the art, what it means for trading & engineering, and a look at XTX

<span class="small muted">Prepared for Auros · June 2026</span>

<!--
Speaker: Let the cover breathe. One line: AI has moved from novelty to table-stakes; tonight is about where it actually stands, what it does to our teams, and two firms worth learning from.
-->

---

## Why are we here?

<div class="cols3">
<div class="card">

### 1 · The state of AI
Where the art actually is right now — the tools, the terms, the pace.

</div>
<div class="card">

### 2 · The trading industry
What it means for engineering teams — and what firms are already doing.

</div>
<div class="card">

### 3 · A case study
**XTX** — Optiver-level revenue, a tenth of the people.

</div>
</div>

<br>

<span class="muted small">Three beats. The middle one is the longest — it's where the work is.</span>

<!--
Speaker: Set expectations. This isn't a hype tour; it's a practitioner's read. We'll go general → specific: the field, then our world, then one firm that did it early.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Part 1
## The state of AI

<!--
Speaker: Start broad and current. The goal here is shared vocabulary and an honest sense of pace before we get tactical.
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
Speaker: The key shift to land: the unit of work moved from "a suggestion" to "a task." A year ago these were demos; now they ship production code daily.
-->

---

## AI vs ML vs LLMs — the same family

![w:560](assets/ai-ml-llm.svg)

<span class="src">A quick map so we're using words the same way: today's "AI" conversation is mostly the innermost ring — large models — but the edge in trading still lives across all of it.</span>

<!--
Speaker: Defuse jargon. "AI" is the broad field; "ML" learns from data; "deep learning" is neural nets (incl. transformers); "LLMs/GenAI" are the frontier we all talk about. Trading uses the whole stack — not just chatbots.
-->

---

## State of the art: what's actually true

<div class="cols">
<div>

- **The pace is breathtaking** — frontier capability steps up every few months; last year's best is now commodity
- **Chat → agents** — models now *plan and execute* multi-step work, not just answer
- **Cost is collapsing** — price per token down ~10× a year; capability-per-dollar rising just as fast

</div>
<div>

- **Reasoning is the new frontier** — "thinking" models spend compute at test time to crack what stumped earlier LLMs
- **Open weights are close behind** — DeepSeek, Llama, Qwen diffuse the frontier cheaply
- **It's horizontal** — same models do code, law, medicine, finance. Like electricity, not an app

</div>
</div>

<!--
Speaker: These are my framing points — edit freely. The one to hammer is pace: any plan that assumes today's limits will be wrong within two quarters. Build for where it's going.
-->

---

## It's already writing the code

![w:560](assets/ai-adoption.svg)

<span class="src">Company-reported share of new code AI-written/assisted. Definitions vary — but the direction is unambiguous.</span>

<!--
Speaker: Concrete proof of "it's here." A quarter to a half of new code at serious engineering orgs is already AI-assisted, with humans on review. This is the baseline, not the frontier.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Part 2
## The trading industry — teams & engineering

<!--
Speaker: Now make it ours. This section is the heart of the talk: what this does to how we build and who we hire.
-->

---

<span class="kicker">The role shift</span>

## Engineers become agent-managers & architects

- The job moves from **writing code** to **specifying, directing and reviewing** agents that write it
- Value concentrates in **system design, problem framing and judgement** — the architect's work
- Typing speed stops mattering; **taste and verification** become the bottleneck

> The best engineers won't be the fastest coders. They'll be the ones who manage a team of agents well.

<!--
Speaker: This is the mental-model change. Frame it as a promotion, not a threat: every good engineer effectively gets a team. But managing agents is a real, different skill.
-->

---

<span class="kicker">The must-have</span>

## AI is not optional — the jury is in

![w:560](assets/ttm-compression.svg)

- You are **falling behind** if your engineers aren't building with these tools
- The analogy: insisting on **hand-writing assembly** while competitors ship in **C++**

<!--
Speaker: Be blunt. This is the conviction slide. The assembly-vs-C++ line lands because everyone in the room understands abstraction levels. The compounding gap is the risk.
-->

---

<span class="kicker">The people problem</span>

## Everyone's a manager overnight

- Hand every engineer a team of agents and you've made them **all managers** — with no training
- That's a **hard transition**: delegation, review, trust, letting go of the keyboard
- **Some won't want to take the step** — and that's information you need early
- Invest in the change deliberately: it won't happen by buying licences

> The tools are the easy part. Re-skilling the people is the program.

<!--
Speaker: The empathy + realism slide. Most failed AI rollouts are change-management failures, not tooling failures. Name that some of your best individual contributors may resist — plan for it.
-->

---

<span class="kicker">Patterns that work · engineering</span>

## Practices to embrace

<div class="cols">
<div class="card">

### Review with agents
**AI code reviewers** — and a **multi-agent** panel, not a single model. Different models catch different bugs.

</div>
<div class="card">

### Skills over chats
Build **reusable skills / tools** for agents, not one-off chat sessions. Compound the leverage.

</div>
</div>
<div class="cols">
<div class="card">

### AI-friendly codebases
**Monorepos** and clean structure so agents can see the whole picture.

</div>
<div class="card">

### Real test environments
**High-quality tests** are the guardrail that lets agents move fast safely.

</div>
</div>

<!--
Speaker: These are the concrete "how." The multi-agent reviewer point is non-obvious and powerful. Tests + monorepo are what make agents reliable — they're an AI-enablement investment, not overhead.
-->

---

<span class="kicker">Patterns that work · the whole firm</span>

## It's bigger than engineering

<div class="cols">
<div class="card">

### Data is the moat
Your data is **more valuable than ever** — and you can't escape the clean-up. The good news: **AI can help do it.** This matters for **every department**, not just engineering.

</div>
<div class="card">

### Specialists are next
Legal, accounting, HR and finance are being **challenged by AI tools** — exactly like engineering. The same playbook (enablement, review, re-skilling) applies firm-wide.

</div>
</div>

<!--
Speaker: Widen the lens so leadership sees this as a firm-wide program. Data quality is the unglamorous prerequisite — and a place AI pays for itself. Every specialist function is on the same curve engineering is.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Part 3
## AI in the trading industry — what firms are doing

<!--
Speaker: From principles to evidence. This is my read from inside Optiver and the wider industry. Flag verbally that these are my recollections.
-->

---

<span class="kicker">Optiver · my account <span class="badge i">Insider</span></span>

## From a standing start to serious money

- When I left, Optiver was **only just starting** its AI journey
- Now: **major investment in systematic trading** — ~**€500M NTI** on the Austin desk at that time
- **~€100M** on a **private GPU cluster & data centre** — and **more is being spent this year**

<span class="src">My recollection / insider perspective — figures approximate and not independently verified.</span>

<!--
Speaker: CONFIDENTIALITY — these are internal recollections of a former employer; only say what you're comfortable sharing with this audience. Keep figures as round, "at that time" numbers. The story: a late starter is now spending at scale.
-->

---

<span class="kicker">Optiver · my account <span class="badge i">Insider</span></span>

## AI in production — and a mindset that flipped

- **AI-only connectivity** projects **in production** for **US cash trading** — many markets to connect to, quickly
- Overcame the **"ATR moral hazard"** that stalled this kind of work before
- The old belief — *"it won't work in our system, our engineering is too specialised"* — was **very wrong**
- Optiver now runs **dedicated AI-enablement teams** with **partner-level sponsorship**

<span class="src">Insider perspective — directional, not a public disclosure.</span>

<!--
Speaker: CONFIDENTIALITY applies. The headline for Auros: the "we're too specialised for this" objection is the exact thing that got disproven. Top-level sponsorship is what made it real.
-->

---

<span class="kicker">Optiver & IMC · my account <span class="badge i">Insider</span></span>

## AI Apps Engineers, in the wild

- **Both Optiver and IMC** use **AI Apps Engineers** extensively
- Concrete wins: **faster triage** and **faster market re-entry** after issues
- Removes a **stressful, mundane on-call task** from humans — and **improves availability metrics**

> A boring, painful job done better by AI — that's where the early ROI actually shows up.

<!--
Speaker: This is the most relatable, least-hype example — operational toil. Availability went up and a horrible job got easier. That's the pattern to copy first at Auros.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Part 4
## Case study: XTX

<!--
Speaker: One firm that did all of this early. The numbers do the talking.
-->

---

<span class="kicker">Case study · XTX</span>

## Optiver-level revenue — a tenth of the people

![w:560](assets/xtx-revenue-timeline.svg)

<span class="src">Revenue: Companies House via FX News Group / Finance Magnates. Headcount approximate (group). 2016–19 single entity; 2020+ combined — see chart note.</span>

<!--
Speaker: The punchline is the gap between the two lines: revenue into the billions while headcount stays a few hundred. ~€/£ billions of revenue with ~10% of an Optiver-sized workforce. That's the AI-and-compute leverage thesis, proven.
-->

---

<span class="kicker">Case study · XTX</span>

## What they did

- **Transformer techniques** — the precursor to today's LLMs — applied to markets **before it was cool**
- Trained on **raw PCAP** market-data captures, at scale
- The bet: **prediction quality + compute**, not the latency arms race
- Result: revenue that **inflected and compounded** through the deep-learning era

<!--
Speaker: This is the case-study thesis, stated plainly. XTX was using the transformer toolkit on packet-capture data years before the rest of the market. Present it as the argued read; the chart backs the compounding.
-->

---

<span class="kicker">Case study · XTX</span>

## Parallels to Auros

<div class="cols">
<div>

- Prices **50,000+ instruments** across equities, fixed income, FX, commodities **and crypto**
- **$250bn traded/day across 35 countries**; deep liquidity in **10,000+ assets**
- A **breadth** play — *not* options-style depth (not competitive with options trading as at 2025)

</div>
<div class="card">

### Why this rhymes with Auros
Breadth across many instruments and venues, won with **models and connectivity** rather than options-style depth — that's **Auros's game too.**

</div>
</div>

<span class="src">Figures: xtxmarkets.com — over 50,000 instruments · 10,000+ assets · $250bn/day · 35 countries.</span>

<!--
Speaker: Bring it home. XTX's edge is breadth + ML + connectivity across a huge instrument universe — structurally close to crypto market making. The lesson travels.
-->

---

## So what — for Auros

<div class="cols">
<div>

- **It's here and it's a must-have** — the leaders are already compounding
- **Re-skill the people** — everyone becomes an agent-manager; help them
- **Invest in the substrate** — tests, monorepos, clean data, multi-agent review

</div>
<div>

- **Sponsor it from the top** — partner-level, like Optiver did
- **Start with the toil** — triage, re-entry, connectivity — where ROI is obvious
- **Breadth + models + connectivity** — XTX shows where that leads

</div>
</div>

<!--
Speaker: Land the asks. Keep it to things Auros can start in a quarter. End on conviction: the firms that move now compound; the rest fall behind.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Appendix
## Evidence & references

<!--
Speaker: Reference material for Q&A — three buckets: TradFi spenders, the macro trend, and crypto/DeFi. Leave up while questions come.
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

<!--
Speaker: The point of this slide: the most sophisticated money is pouring capital into AI compute and talent. Names available for anyone who wants to dig.
-->

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

<!--
Speaker: The macro backdrop — AI is the fastest-diffusing general-purpose tech we've seen, across every sector. Use selectively to answer "is this just hype?".
-->

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

<!--
Speaker: Your peer set, mapped. The pattern: everyone's investing in ML + agent infrastructure; the on-chain-agent narrative is partly real, partly hype — draw that line yourself.
-->

---

## Sources & method

- **XTX:** Companies House (`09415174`, `12300034`, `12832334`); FX News Group; Finance Magnates
- **TradFi:** CoinDesk, Bloomberg, Fortune, company disclosures (Citadel, Jane Street, Bridgewater, Two Sigma, HRT, Man AHL, JPMorgan)
- **Economy:** Anthropic & GitHub productivity research; AWS; OpenAI case studies; DeepMind; analyst market reports
- **Crypto:** company statements; AWS/Google Cloud case studies; Messari; 1kx
- **Optiver / IMC (Part 3):** my own insider perspective — directional, not public disclosures

<span class="src">Full URL list in <code>sources.md</code>. Key: unbadged = sourced · <span class="badge i">I</span> inference/insider · <span class="badge m">M</span> hype-flagged. Verify headline figures before presenting.</span>

<!--
Speaker: Close on rigour. Be explicit that Part 3 is your recollection, not a citation — that honesty protects you.
-->
