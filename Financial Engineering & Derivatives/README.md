# Financial Engineering and Derivatives (MSQF 542)

**Course:** MSQF 542: Financial Engineering and Derivatives  
**Degree:** M.Sc. Quantitative Finance (Semester III)  
**Institution:** Department of Statistics, Ramanujan School of Mathematical Sciences, Pondicherry University  
**Credits:** 3  
**Nature of Course:** Soft Core (Elective)  
**Official Syllabus Reference:** [`./syllabus.md`](./syllabus.md) | Master Curriculum: [`../SYLLABUS.md`](../SYLLABUS.md) | Official PDF: [`../Semester_III_Syllabus.pdf`](../Semester_III_Syllabus.pdf) (Page 8)

---

## 📂 Directory Contents

| File / Folder | Description |
| :--- | :--- |
| [`project_report/`](./project_report/) | **Empirical Term Project (MSQF 542):** *Black–Scholes Option Pricing, Volatility Surface Analytics, and Derivative Hedging Architectures: An Empirical Investigation of ITC Limited (2025–2026)* (MSQF 542 Unit IV & Case Study CO3/CO5). |
| ├── [`main.pdf`](./project_report/main.pdf) | **Dedicated 15-Page Academic Empirical Report** in strict monochrome format, featuring the official Pondicherry University Department of Statistics title page layout, continuous document flow, Merton dividend PDE calibration, Greek surface sensitivities, IV skew curves, and multi-strategy hedging efficiency. Evaluated under Course Instructor Dr. Kamalakkannan Adhisekar (November 2026). Exactly 15 pages. |
| ├── [`data/`](./project_report/data/) | Quantitative metrics output (`full_analysis_metrics.json`) calibrated from trailing NSE market sessions. |
| ├── [`figures/`](./project_report/figures/) | Vector PDF figures (`fig1_fed_greeks_surface.pdf`, `fig2_fed_skew_payoffs.pdf`, university crest). |
| └── [`sections/`](./project_report/sections/) | Modular LaTeX source sections (Sec 01 through Sec 14) calibrated to exactly 15 pages. |
| [`ITC_VaR_and_Black_Scholes_Hedging_Report.pdf`](./ITC_VaR_and_Black_Scholes_Hedging_Report.pdf) | *Legacy Joint 9-Page Paper (MSQF 533 & MSQF 542)* on VaR and Black–Scholes. |
| [`syllabus.md`](./syllabus.md) | Verbatim course syllabus, course objectives, course outcomes (CO1–CO5), unit breakdowns (Units I–V), reference bibliography, and CO-PO mapping matrix. |
| [`MSQF_542_Financial_Engineering_Derivatives_Unit1.pdf`](./MSQF_542_Financial_Engineering_Derivatives_Unit1.pdf) | Unit 1 lecture slides: Financial engineering concept, scope, tools, process, and financial analysis. |
| [`Unit_2_Derivatives_and_Market_Instruments-2-23.pdf`](./Unit_2_Derivatives_and_Market_Instruments-2-23.pdf) | Unit 2 course material: Financial derivatives definitions, types, Indian and international OTC markets. |
| [`MSQF_542_Financial_Engineering_Derivatives_UNIT 3.pdf`](./MSQF_542_Financial_Engineering_Derivatives_UNIT%203.pdf) | Unit 3 lecture deck: Forward and futures contracts, mechanics, hedging, MTM, and clearing house structures. |
| [`financial derivatives_module1.pptx`](./financial%20derivatives_module1.pptx) | Class presentation slides covering derivatives fundamentals and market instruments. |
| [`Derivatives_Trading_FAQs.pdf`](./Derivatives_Trading_FAQs.pdf) | Practical handbook and market FAQs on derivatives trading on Indian exchanges (NSE / BSE). |
| [`Hull J.C.-Options, Futures and Other Derivatives_9th edition.pdf`](./Hull%20J.C.-Options,%20Futures%20and%20Other%20Derivatives_9th%20edition.pdf) | Core textbook reference by John C. Hull. |

---

## 📑 Curriculum Coverage: Units I – V

1. **Unit I: Introduction to Financial Engineering**
   - Meaning, scope, need, and tools of financial engineering.
   - Financial engineering vs. financial analysis; contributing factors to market growth; the financial engineering innovation process.
2. **Unit II: Financial Derivatives**
   - Meaning, definitions, functions, and economic classification of derivatives.
   - Derivatives markets in India and abroad; Exchange-traded vs. OTC derivatives; emerging instruments in international financial centers.
3. **Unit III: Futures Contracts**
   - Forward vs. futures mechanics; specifications, long and short positions, margin requirements, mark-to-market (MTM), and clearing house operations.
   - Convergence of futures price to spot price; hedging strategies with futures; stock index futures.
4. **Unit IV: Options Contracts & Trading Strategies**
   - Options definitions, American vs. European options, payoff profiles.
   - Option pricing models: Binomial lattice model and Black-Scholes analytical formula.
   - Options trading strategies: Covered calls, protective puts, bull/bear spreads, butterfly spreads, calendar spreads, straddles, strips, straps, and strangles; Put-Call Parity theorem.
5. **Unit V: Swap Contracts**
   - Swaps concepts and typology: Interest Rate Swaps (IRS) and Currency Swaps.
   - Mechanics, comparative advantage pricing, valuation dynamics, and credit/counterparty risk management.

---

## 📈 Empirical Project Report: Black–Scholes Option Pricing and Derivative Hedging of ITC Limited

Located in [`project_report/`](./project_report/), this **dedicated 15-page academic empirical report** investigates continuous-time derivative valuation, dividend-adjusted pricing PDEs, volatility smiles, and structured options risk management for an institutional equity commitment in **ITC Limited (NSE: ITC)** over trailing market sessions, fulfilling MSQF 542 Unit IV and Course Outcomes CO3, CO4, and CO5 under Course Instructor **Dr. Kamalakkannan Adhisekar** (November 2026).

### Key Highlights & Deliverables
1. **Asset Exposure:** $1\text{ NSE F\&O Lot} = 1,725\text{ shares}$ at spot price $S_0 = \text{\rupee}285.00$ ($V_0 = \text{\rupee}4,91,625.00$).
2. **Continuous vs. Discrete Dividend Modeling:** Analyzes ITC's continuous dividend yield $q = 5.09\%$ (\inr 14.50 trailing cash payout per share) under Merton's extended PDE vs. standard Black--Scholes ($q=0$). Proves that ignoring dividend drag introduces severe pricing distortions: ATM 285 Call is overpriced by $+9.76\%$ (+\rupee 0.90/share or \rupee 1,553/lot) while ATM Put is underpriced by $-8.84\%$ (-\rupee 0.77/share or \rupee 1,328/lot).
3. **Closed-Form Greek Sensitivities:** Derives and tabulates all first and second-order Greeks ($\Delta, \Gamma, \mathcal{V}, \Theta, \rho$) across 5 option strikes (275 to 295). Visualizes the dual-panel Greek surface ($\Delta$ S-curve and $\Gamma$ peak at ATM forward $F_0 = \text{\rupee}285.18$).
4. **Implied Volatility (IV) Skew:** Extracts implied volatility from NSE option quotes, revealing an asymmetric "smirk" where Deep OTM Puts trade at a $+402\text{ bps}$ volatility premium ($\IV = 27.42\%$ at Strike 270) over ATM volatility ($23.40\%$), reflecting institutional demand for crash catastrophe insurance.
5. **Multi-Strategy Hedging Performance Comparison:**
   - **ATM Protective Put (285):** Insulates $75.14\%$ of extreme 10d 99% downside risk, capping max loss at \rupee 15,283.50 ($3.11\%$).
   - **Low-Cost Collar (280/295):** Delivers superior downside insulation ($\mathbf{78.96\%}$ tail risk mitigation) at an upfront cash outlay of only $\mathbf{0.88\%}$ (\rupee 4,312.50 per lot), by selling the 295 Call to fund the 280 Put floor.
   - **Covered Call (295):** Generates premium yield of \rupee 7,452.00, but leaves the portfolio vulnerable to major crashes (only $12.12\%$ tail protection).
   - **Bear Put Spread (285/270):** Provides cost-effective intermediate hedging ($42.08\%$ mitigation) with capped payoff protection.
6. **Dynamic Delta Rebalancing & Market Frictions:** Evaluates discrete rebalancing under Indian transaction costs (Securities Transaction Tax / STT, NSE turnover charges, GST, SEBI turnover fees, and bid-ask spreads). Demonstrates that transaction cost drag increases as $\mathcal{O}(1/\sqrt{\Delta t})$, establishing an optimal threshold-based $(\Delta \pm 0.05)$ rebalancing boundary for Indian trading desks.
7. **Strict Greyscale Design:** Formatted in strict monochrome throughout, replicating the official Pondicherry University Department of Statistics cover layout, featuring high-contrast publication figures, and compiling to **exactly 15 pages** with zero warnings.
