# Sources & evidence log — "AI & the Speed Moat"

Citation key (matches the deck badges):
- **(unbadged) Verified** — corroborated in a primary/secondary public source (URLs below).
- 🟡 **I — Inference / insider** — reasoned from public signals or proprietary; not independently confirmed.
- 🔴 **M — Myth-flagged** — a common claim the deck deliberately corrects.

> ⚠️ Many figures are company-reported or from press/analyst coverage; some 2026 stats are forecasts.
> **Verify headline numbers against primary sources before presenting.** Definitions (e.g. "AI-written code") vary by company.

---

## Force 1 — Developer & worker productivity
- GitHub Copilot — 55% faster (peer-reviewed) — https://cacm.acm.org/research/measuring-github-copilots-impact-on-productivity/
- Google — ~25%+ of new code AI-generated (Pichai, 2024) — https://www.theverge.com/2024/10/29/24282757/google-new-code-25-percent-ai (later statements indicate rising share)
- Amazon Q — $260M / ~4,500 dev-years (Java migration) — https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone/
- Stripe "Minions" — ~1,300 PRs/week — https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2
- JPMorgan LLM Suite — 3–6 hrs/week/employee — https://thedigitalbanker.com/jpmorgan-chases-llm-suite-drives-ai-transformation-across-the-enterprise/
- Vodafone — 3 hrs/week, 68k staff (M365 Copilot) — https://news.microsoft.com/source/emea/features/vodafone-to-roll-out-microsoft-365-copilot-to-68000-employees-to-boost-productivity-innovation-and-quality/
- Anthropic — 81% median time saved (internal study) — https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- Anthropic — ~1.8% potential US productivity-growth uplift — https://www.anthropic.com/research/estimating-productivity-gains
- Moderna — 750+ custom GPTs — https://openai.com/index/moderna/
- **Deep dive — Coinbase:** AI-tool mandate; 33%→50% AI-written code; 51% task speedup — https://www.coinbase.com/blog/Tools-for-Developer-Productivity-at-Coinbase · https://fortune.com/2025/08/25/coinbase-ceo-brian-armstrong-ai-coding-assistants-mandate-tech/

## Force 2 — Autonomous system building
- Cognition Devin — SWE-bench, ~25% of own code — https://cognition.ai/blog/introducing-devin · https://www.swebench.com/
- **Devin @ Nubank** — ~12x hours / 20x cost, weeks not years — https://building.nubank.com/enhancing-engineering-workflows-with-ai-a-real-world-experience
- Devin @ Goldman Sachs — agents across 12k-eng org — https://www.bloomberg.com/news/articles/2025-07-11/goldman-sachs-deploys-ai-agents-for-software-development
- Claude Code — majority of Anthropic's code — https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously
- GitHub Copilot agent — ~56% SWE-bench Verified — https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/
- Waymo — 450k+ paid rides/week — https://electrek.co/2026/02/12/waymo-begins-fully-autonomous-ops-with-6th-gen-driver-targets-1m-weekly-rides/
- Figure @ BMW — 99%+ accuracy, 90k+ parts — https://www.repairerdrivennews.com/2025/11/25/humanoid-robots-complete-11-month-project-at-bmw-plant/
- Amazon — 1M+ robots; ~$12.6B savings (Morgan Stanley est.) — https://www.cnbc.com/2025/10/22/amazon-switch-to-robots-will-save-it-up-to-4-billion-a-year-morgan-stanley-says.html
- Agility Digit — 100k+ totes — https://www.agilityrobotics.com/content/digit-moves-over-100k-totes

## Force 3 — Cost reduction
- Klarna — ≈700-agent workload; −40% cost/txn (＊2025 human-in-loop re-added) — https://openai.com/index/klarna/ · https://www.customerexperiencedive.com/news/klarna-ai-slash-customer-service-costs/748647/
- Salesforce Agentforce — $100M+ savings — https://www.salesforce.com/agentforce/metrics/
- IBM AskHR — −40% HR cost; ~$4.5B productivity — https://www.ibm.com/case-studies/ibm-askhr
- ServiceNow / Intercom Fin — 80–90% deflection — https://www.intercom.com/blog/announcing-fin-2-ai-agent-customer-service/
- JPMorgan LOXM — 15% execution efficiency — https://medium.com/@navnoorbawa/jpmorgans-29-8b-trading-operation-machine-learning-execution-c6527a679518
- Manufacturing predictive maintenance — 25–40% (aggregate) — https://www.netguru.com/blog/ai-predictive-maintenance
- Duolingo — AI-first contractor shift — https://www.computing.co.uk/news/2025/ai/duolingo-goes-ai-first-as-it-phases-out-human-contractors

## Force 4 — R&D
- AlphaFold 3 / Isomorphic (2024 Nobel) — https://deepmind.google/science/alphafold/ · https://www.isomorphiclabs.com/
- Insilico ISM001-055 (rentosertib) Phase IIa — https://insilico.com/news/tnik-ipf-phase2a
- DeepMind GNoME — 2.2M materials / 736 synthesised — https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/
- DeepMind AlphaChip — 3 TPU generations — https://deepmind.google/blog/how-alphachip-transformed-computer-chip-design/
- DeepMind GraphCast — https://deepmind.google/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/
- Microsoft MatterGen — https://www.microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/
- Commonwealth Fusion + DeepMind digital twin — https://cfs.energy/news-and-media/commonwealth-fusion-systems-accelerates-commercial-fusion-with-siemens-and-nvidia-leveraging-ai-powered-digital-twins/
- Kronos (foundation model for K-lines) — https://arxiv.org/html/2508.02739v1

## Crypto trading — competitors (internals largely 🟡 inference)
- Wintermute — 313% vol growth, ~$5B/day — https://www.ainvest.com/news/wintermute-algorithmic-trading-resilience-strategic-confidence-market-adaptability-volatile-era-2510/
- GSR — market making / ML — https://www.gsr.io/services/trading-market-making
- Jump Crypto — DL/RL/LLMs — https://www.jumptrading.com/ai-ml
- B2C2 — vector/time-series ML; $2T+ volume — https://kx.com/blog/crypto-analytics-at-scale-how-b2c2-trades-smarter-in-a-24-7-market
- Cumberland (DRW) — https://www.cumberland.io/about
- Keyrock — 85+ venues — https://keyrock.com/
- Flowdesk — 1M+ orders/day — https://cloud.google.com/customers/flowdesk
- FalconX — Satoshi LLM copilot; Focal — https://www.falconx.io/newsroom/meet-focal-ai-insights-engine-for-institutional-crypto
- DWF Labs — autonomous trading agents — https://coinedition.com/ai-in-crypto-dwf-labs-launches-autonomous-trading-agents/
- Amber Group — AgentFi — https://www.ambergroup.io/

## Crypto — agent-native exchanges & on-chain frontier
- Coinbase AgentKit — https://www.coinbase.com/developer-platform/discover/launches/introducing-agentkit
- Kraken CLI (MCP-native) — https://blog.kraken.com/news/industry-news/announcing-the-kraken-cli
- OKX Agent Trade Kit / OnchainOS — https://www.okx.com/en-us/learn/onchainos-our-ai-toolkit-for-developers
- Binance AI (fraud models; AI Pro) — https://www.binance.com/en/academy/articles/how-to-use-ai-for-crypto-trading
- Virtuals Protocol (~$479M Q1 on-chain) — https://messari.io/report/understanding-virtuals-protocol-a-comprehensive-overview
- Bittensor (~$43M Q1 on-chain revenue) — https://1kx.capital/writing/2025-onchain-revenue-report
- ai16z / ElizaOS — https://cryptoslate.com/ai16z-rebrands-into-elizaos-as-adoption-grows/
- Agentic-finance landscape (forecasts — 🔴 treat as hype) — https://www.cambrian.org/blog/agentic-finance-landscape-q1-2026

## TradFi quant bar
- XTX — 25k GPUs; €1bn Kajaani; **Companies House** (`09415174`, `12300034`), *not HMRC* — https://find-and-update.company-information.service.gov.uk/company/09415174 · https://www.datacenterdynamics.com/en/news/xtx-markets-to-build-data-center-campus-in-kajaani-finland/
  - 🟡 **Presenter hypothesis (not asserted as fact):** XTX's revenue inflection reflects deepening ML / deep-learning adoption (incl. transformers post-2017). Group revenue by year (£bn): 2016 0.13 · 2017 0.15 · 2018 0.31 · 2019 0.34 · 2020 ~1.05 · 2021 1.48 · 2022 2.49 · 2023 2.01 · 2024 2.74 · 2025 3.93. **Caveats:** founded **2015** (already systematic); the 2018 ~doubling likely pre-dates transformers in production (~2–3 yr lag); the **2020 entity restructure** breaks comparability and coincides with COVID volatility. Sources: FX News Group; Finance Magnates; LeapRate; Companies House (`09415174`, `12300034`, `12832334`). Paper: https://arxiv.org/abs/1706.03762
- Jane Street — $6B CoreWeave commitment — https://finance.yahoo.com/sectors/technology/articles/jane-street-signs-6-billion-121800153.html
- Bridgewater — $2B AIA ML fund — https://www.bridgewater.com/aia-labs
- Citadel — crypto market-making entry (Feb 2025) — https://www.coindesk.com/business/2025/02/24/citadel-plans-crypto-market-making-business-bloomberg
- Renaissance / Man AHL — https://www.man.com/insights/the-rise-of-machine-learning

## Macro
- Hyperscaler AI capex (~$500B+/yr, reported) — see Citadel Securities 2026 outlook & press coverage — https://www.citadelsecurities.com/news-and-insights/
- Automated-crypto-trading market size — https://www.grandviewresearch.com/industry-analysis/automated-crypto-trading-market-report
