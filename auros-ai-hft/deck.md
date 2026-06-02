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

<span class="kicker">Live · starting now</span>

## Let's put it to the test

<p style="text-align:center; margin:14px 0;"><span style="display:inline-block; border:2px solid #e6ab57; border-radius:14px; padding:14px 36px; font-size:34px; font-weight:700; letter-spacing:2px; color:#f0c074;">AGENT BUILDING&nbsp;…&nbsp;LIVE</span></p>

- Right now I'm setting an **AI agent** loose on a real task: a **BTC autotrader** that connects to **Binance** and scalps on a **couple of momentum signals**
- It builds in the **background** while we talk
- The bet: by the time I finish, there's a **strategy live in the market** — written, tested, trading

<!--
Speaker: FIRST mention of the demo. Just before this slide, kick the agent off in a terminal you can return to, using your prepared plan/prompt.
SAFETY: use Binance testnet (testnet.binance.vision) or paper / tiny size — never full-size real capital live on stage. Throwaway API key: trade-only, no withdrawals, IP-restricted.
Signals: keep it simple — e.g. fast/slow EMA crossover + RSI, or order-book imbalance.
Fallback: have a pre-recorded successful run ready in case wifi / login / venue fails.
Then DON'T mention it again until the reveal at the end.
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
Speaker: The heart of the talk. The autotrader is building in the background — don't mention it yet; the payoff comes at the end.
-->

---

<span class="kicker">The shift</span>

## Engineers are becoming agent-managers

![w:520](assets/ttm-compression.svg)

- The work is moving from **writing code** to **directing and reviewing** the agents that write it
- It's a step up the abstraction ladder — much like the move from **assembly to C++**
- The teams leaning in are shipping in a fraction of the time

<!--
Speaker: Observation, not instruction — the role is changing across the industry (architect / agent-manager). The assembly-to-C++ analogy lands because everyone here gets abstraction levels. Keep it "here's what's happening," not "here's what you must do."
-->

---

<span class="kicker">The economics of code</span>

## Legacy is only worth it if it pays

- AI makes legacy code far cheaper to **read, migrate and modernise** — the grind is largely automatable now
- The deeper shift: **the only code worth its legacy overhead is code that makes money**
- When a rewrite costs a fraction of what it used to, the calculus flips — firms are **willing to throw things out**
- Optiver's tell: rather than nurse old systems, the energy went into **new systematic trading, built fresh**

<!--
Speaker: The "code = P&L" idea, as an observation. AI removes most of the legacy grind; and because rewrites are cheap now, the bar for keeping old code is simply "does it make money?" Optiver's systematic-trading bet is the example — build fresh rather than carry legacy. Illustrate, don't prescribe.
-->

---

<span class="kicker">The catch</span>

## Everyone's a manager overnight

- Hand every engineer a team of agents and you've effectively made them **all managers** — with no training
- It's a real transition: delegation, review, trust, letting go of the keyboard
- And **some won't want to make that leap** — which tends to surface fast

> The tooling is the easy part. The human change is the real work.

<!--
Speaker: The empathy + realism beat. Most failed rollouts are change-management failures, not tooling failures. Name that some of your best ICs may resist. This is your best line — give it a moment.
-->

---

<span class="kicker">What the winners have in common</span>

## The substrate that makes it work

<div class="cols">
<div>

- **Multi-agent code review** — a panel, not one model; different models catch different bugs
- **Skills over chats** — reusable tools, not one-off prompts
- **Monorepos + real tests** — so agents see the whole picture and can't break things quietly

</div>
<div class="card">

### And it reaches everyone
**Data** is the moat, and the clean-up is unavoidable — though **AI can help.** **Legal, finance, HR** are on the same curve. It's a firm-wide story.

</div>
</div>

<!--
Speaker: The practical "how," compressed. Multi-agent review is the non-obvious one. Tests + monorepo are AI-enablement, not overhead. Then widen the lens: every specialist function is on engineering's curve.
-->

---

<span class="kicker">An unexpected dividend</span>

## Ideas get tested without the queue

- Traders & researchers can **prototype and test ideas directly** — the "raise a ticket, wait for a dev" bottleneck fades
- Hypotheses go from **idea → tested in hours**, not sprints
- The irony: working with agents **forces better documentation** — they need the context, so it finally gets written
- Net effect: a **tighter loop between research and the market**

<!--
Speaker: The one the traders in the room will feel. The engineering queue was always the choke point between a research idea and a live test; AI loosens it. And the lovely irony — to get good output from agents you must write things down, so documentation finally improves. Ends Part 2; leads into what firms are actually doing.
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

![w:660](assets/xtx-revenue-timeline.svg)

> **XTX's revenue climbed to match Optiver's — on roughly a tenth of the headcount.** ~£15M of revenue per employee, close to 10× Optiver's.

<span class="src">XTX revenue bars (turnover) + headcount line; Optiver shown as 2025 reference (NTI ≈£3.9bn / €4.6bn; ~2,600 staff). €→£ approx; 2016–19 single entity, 2020+ combined.</span>

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

## What this makes possible

<div class="cols">
<div>

- **Strategies live in days, not quarters** — the demo wasn't a trick
- **Small teams, huge surface area** — XTX's tenth-of-the-people is the proof
- **The boring toil, handled** — triage, re-entry, connectivity (Optiver & IMC already do this)

</div>
<div>

- **Legacy stops being a prison** — rewrite cheaply, keep only what pays
- **It compounds** — the firms leaning in pull away a little more each quarter
- **Every function, not just engineering** — the same curve, firm-wide

</div>
</div>

<!--
Speaker: Concrete, quarter-sized asks. Then the payoff, then the close.
-->

---

<span class="kicker">Live · the payoff</span>

## Remember the autotrader?

<p style="text-align:center; margin:14px 0;"><span style="display:inline-block; border:2px solid #5fc59a; border-radius:14px; padding:14px 36px; font-size:34px; font-weight:700; letter-spacing:2px; color:#7fd9b0;">LIVE ON BINANCE</span></p>

- It's **connected to Binance**, scalping **BTC** on momentum signals — and **placing trades**
- Built by an agent **during this talk**: the connector, the signals, the order logic, the tests
- One prompt. One session. **A live strategy by the end of the hour.**

<!--
Speaker: THE PAYOFF — switch to the running bot. Show the trades / PnL / logs and narrate what it built. The line: "this used to be weeks of work for a team — it happened while I talked." Fall back to the recording if needed. Then the close.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# A tenth of the people.

## That used to be XTX's secret. It isn't anymore — it's on the table for anyone willing to pick it up.

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
