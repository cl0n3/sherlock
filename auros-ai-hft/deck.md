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

# The state of AI in trading

## Where it actually is — and how one firm is using it

<span class="small muted">Prepared for Auros · June 2026</span>

<!--
Speaker: A calm open. The title says it plainly — no theatrics.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: '' -->

<span class="kicker">why this, why now</span>

# AI is changing how fast a desk can build

## I'm not here to tell you your business — just to show you where AI actually is, what it's doing to engineering teams, and how Optiver is using it.

<span class="small muted">Three parts: the state of AI · what it does to our teams · a case study.</span>

<!--
Speaker: Measured framing — scout, not consultant: here's what I'm seeing, you'll know what fits. Then kick off the demo on the next slide.
-->

---

<span class="kicker">a quick experiment, running in the background</span>

## Let's put it to the test

<p style="text-align:center; margin:14px 0;"><span style="display:inline-block; border:2px solid #e6ab57; border-radius:14px; padding:14px 36px; font-size:34px; font-weight:700; letter-spacing:2px; color:#f0c074;">AGENT BUILDING&nbsp;…&nbsp;LIVE</span></p>

- While we talk, I've set an **AI agent** on a real task: a small **BTC autotrader** that connects to **Binance** and scalps on a **couple of momentum signals**
- It builds in the **background** — we'll check back at the end
- A simple test of one question: how fast can an idea get to market?

<!--
Speaker: Just before this slide, kick the agent off in a terminal you can return to, using your prepared plan/prompt.
SAFETY: use Binance testnet (testnet.binance.vision) or paper / tiny size — never full-size real capital live on stage. Throwaway API key: trade-only, no withdrawals, IP-restricted.
Signals: keep it simple — e.g. fast/slow EMA crossover + RSI, or order-book imbalance.
Fallback: have a pre-recorded successful run ready in case wifi / login / venue fails.
Then leave it until the reveal at the end.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Part 1
## The state of AI

<!--
Speaker: Quick, current, shared vocabulary.
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

- **The pace is fast** — last year's state-of-the-art is this year's commodity
- **Anthropic's own code is now mostly written by Claude** — the toolmakers use their own tools
- **Inference keeps getting cheaper** — capability per dollar falls steadily, year on year
- **It's general-purpose** — the same model does code, law, medicine and markets; more like electricity than an app

<!--
Speaker: Measured facts. The one worth holding: any plan that assumes today's limits will likely be wrong within a couple of quarters.
-->

---

<span class="kicker">Part 1 · the proof</span>

## It's already writing the code

![w:540](assets/ai-adoption.svg)

> A large share of new code at serious engineering shops is already machine-written — with humans on review.

<!--
Speaker: Concrete proof it's here. Baseline, not frontier.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Part 2
## What it does to our teams

<!--
Speaker: The autotrader is building in the background — leave it until the end.
-->

---

<span class="kicker">The shift</span>

## Engineers are becoming agent-managers

![w:520](assets/ttm-compression.svg)

- The work is moving from **writing code** to **directing and reviewing** the agents that write it
- It's a step up the abstraction ladder — much like the move from **assembly to C++**
- The teams leaning in are shipping in a fraction of the time

<!--
Speaker: Observation, not instruction — the role is changing across the industry (architect / agent-manager). The assembly-to-C++ analogy lands because everyone here gets abstraction levels.
-->

---

<span class="kicker">The economics of code</span>

## Legacy is only worth it if it pays

- AI makes legacy code far cheaper to **read, migrate and modernise** — the grind is largely automatable now
- The deeper shift: **the only code worth its legacy overhead is code that makes money**
- When a rewrite costs a fraction of what it used to, the calculus flips — firms are **willing to throw things out**
- Optiver's tell: rather than nurse old systems, the energy went into **new systematic trading, built fresh**

<!--
Speaker: The "code = P&L" idea, as an observation. AI removes most of the legacy grind; and because rewrites are cheap now, the bar for keeping old code is simply "does it make money?" Illustrate, don't prescribe.
-->

---

<span class="kicker">The catch</span>

## Everyone's a manager overnight

- Hand every engineer a team of agents and you've effectively made them **all managers** — with no training
- It's a real transition: delegation, review, trust, letting go of the keyboard
- And **some won't want to make that leap** — which tends to surface fast

> The tooling is the easy part. The human change is the real work.

<!--
Speaker: The empathy + realism beat. Most failed rollouts are change-management failures, not tooling failures. Give this line a moment.
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
Speaker: The practical "how," compressed. Multi-agent review is the non-obvious one. Tests + monorepo are AI-enablement, not overhead.
-->

---

<span class="kicker">An unexpected dividend</span>

## Ideas get tested without the queue

- Traders & researchers can **prototype and test ideas directly** — the "raise a ticket, wait for a dev" bottleneck fades
- Hypotheses go from **idea → tested in hours**, not sprints
- The irony: working with agents **forces better documentation** — they need the context, so it finally gets written
- Net effect: a **tighter loop between research and the market**

<!--
Speaker: The one the traders in the room will feel. And the irony — to get good output from agents you must write things down, so documentation improves. This sets up Optiver, whose whole strategy is built around it.
-->

---

<!-- _class: section -->
<!-- _paginate: false -->

# Part 3
## Case study: Optiver

<!--
Speaker: The centrepiece — my read from inside Optiver. Say verbally these are recollections.
-->

---

<span class="kicker">Case study · Optiver</span>

## Optiver's strategy, in three lines

- **Time to market is the goal** — ship and adapt faster than the field
- **Developer productivity is the byproduct** — it follows from the goal; it was never the point
- **Remove the engineering bottleneck** — so traders & researchers can test ideas directly

<!--
Speaker: Anchor the whole section here. The order matters: they're chasing speed-to-market; productivity and self-serve research are consequences, not targets.
-->

---

<span class="kicker">Case study · Optiver <span class="badge i">Insider</span></span>

## Backing it with real money

- When I left, Optiver was **only just starting** its AI journey
- Now: **major investment in systematic trading** — ~**€500M NTI** on the Austin desk at that time
- **~€100M** on a **private GPU cluster & data centre** — and **more is being spent this year**

<span class="src">My recollection / insider perspective — figures approximate and not independently verified.</span>

<!--
Speaker: CONFIDENTIALITY — internal recollections; say only what you're comfortable sharing. The point: the time-to-market strategy is backed with serious capital.
-->

---

<span class="kicker">Case study · Optiver <span class="badge i">Insider</span></span>

## "It won't work here." It worked.

- The objection everyone had: *"our engineering is too specialised — AI can't help us"*
- Then **AI-only connectivity** went **into production** for US cash trading — many markets, connected fast
- It cleared the **"ATR moral hazard"** that had stalled this work for years
- Today: **dedicated AI-enablement teams** with **partner-level sponsorship**

> Speed to market beat the "we're different" objection.

<!--
Speaker: CONFIDENTIALITY applies. The reversal — tell it with a beat. "Too specialised" got disproven once the goal was clearly time-to-market and the top sponsored it.
-->

---

<span class="kicker">Case study · Optiver & IMC <span class="badge i">Insider</span></span>

## AI Apps Engineers, in the wild

- **Both Optiver and IMC** use **AI Apps Engineers** extensively
- Concrete wins: **faster triage** and **faster market re-entry** after issues
- Removes a **stressful, mundane on-call task** from humans — and **improves availability metrics**

> Faster re-entry is time-to-market by another name — and a horrible job got easier.

<!--
Speaker: The most relatable example: operational toil. Availability up, a painful job easier. Tie it back: re-entry speed is time-to-market.
-->

---

<span class="kicker">Optiver isn't alone</span>

## A quick word on XTX

- A pure-quant market maker that took a contrarian bet early: **out-predict, don't out-race**
- Put **transformer techniques** on raw **PCAP** market data **before that was common**
- Trades **50,000+ instruments** across asset classes — a **breadth** play, much like Auros
- The point: the AI-first approach isn't theory — others have built real businesses on it

<span class="src">xtxmarkets.com; Companies House. More on XTX in the appendix.</span>

<!--
Speaker: Brief. XTX is supporting evidence, not the headline — Optiver is the case study. About a minute, then move on.
-->

---

## Where this leaves us

<div class="cols">
<div>

- **Ideas reach the market faster** — the prize Optiver is chasing
- **Productivity follows** — more output per engineer, as a byproduct
- **The boring toil gets handled** — triage, re-entry, connectivity

</div>
<div>

- **Legacy stops being a prison** — rewrite cheaply, keep only what pays
- **Research self-serves** — fewer ideas stuck in the engineering queue
- **It's firm-wide** — not just engineering

</div>
</div>

<!--
Speaker: Observations, not instructions — what's on the table now, shown through what's already happening. Then the demo, then a calm close.
-->

---

<span class="kicker">back to the experiment</span>

## The autotrader

<p style="text-align:center; margin:14px 0;"><span style="display:inline-block; border:2px solid #5fc59a; border-radius:14px; padding:14px 36px; font-size:34px; font-weight:700; letter-spacing:2px; color:#7fd9b0;">LIVE ON BINANCE</span></p>

- It's **connected to Binance**, scalping **BTC** on momentum signals — and **placing trades**
- Built by an agent **while we talked**: the connector, the signals, the order logic, the tests
- One prompt, one session — an idea **in the market by the end of it**

<!--
Speaker: Switch to the running bot. Show the trades / logs and narrate what it built. Keep it matter-of-fact: "this used to be weeks of work." Fall back to the recording if needed.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# Where AI really moves the needle is speed.

## How fast a desk can take an idea to market is becoming the thing that separates firms. The tools are here — for anyone.

<!--
Speaker: A calm close, not a challenge. State it, pause, and open it up for discussion. No ultimatum.
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

- **XTX** — ~£3.9bn revenue on ~260 staff; 25k GPUs, transformers
- **Citadel Securities** — AI spend rising; entered **crypto market-making** (Feb 2025)
- **Jane Street** — **$6B** CoreWeave AI-compute commitment
- **Bridgewater** — **$2B** "AIA" ML fund

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

- **Optiver / IMC (Part 3):** my own insider perspective — directional, not public disclosures
- **XTX:** Companies House (`09415174`, `12300034`, `12832334`); FX News Group; Finance Magnates; xtxmarkets.com
- **TradFi:** CoinDesk, Bloomberg, Fortune, company disclosures (Citadel, Jane Street, Bridgewater, Two Sigma, HRT, Man AHL, JPMorgan)
- **Economy:** Anthropic & GitHub productivity research; AWS; OpenAI case studies; DeepMind; analyst market reports
- **Crypto:** company statements; AWS/Google Cloud case studies; Messari; 1kx

<span class="src">Full URL list in <code>sources.md</code>. Key: unbadged = sourced · <span class="badge i">I</span> inference/insider · <span class="badge m">M</span> hype-flagged. Verify headline figures before presenting.</span>

<!--
Speaker: Close on rigour. Part 3 is recollection, not citation — that honesty protects you.
-->
