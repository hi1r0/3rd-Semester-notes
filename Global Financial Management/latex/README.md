# Global Financial Management — LaTeX Notes (MSQF Semester III)

This directory contains the modular LaTeX sources, custom TikZ flowcharts, institutional profiles, and compiled notes for the **Global Financial Management** course (M.Sc. Quantitative Finance, Semester III).

---

## 📑 Syllabus & Course Coverage Roadmap

### **Unit I: International Financial Architecture & Balance of Payments**
- **1.1 International Financial Institutions (World Bank Group)**
  - Five constituent arms: IBRD (1944), IDA (1960), IFC (1956), MIGA (1988), ICSID (1966).
  - Structural lending vs. concessional development finance.
  - *Lecture Date:* `18/08/2026`.
- **1.2 Functions of the World Bank**
  - Analytical & Advisory Services (AAA), Knowledge sharing, and Structural Adjustment Facility.
  - *Lecture Date:* `21/08/2026`.
- **1.3 Governance & Bank Related Activities**
  - Shareholding structure (US, UK, France, Japan, Germany), Board of Governors, and lending approvals.
  - *Lecture Date:* `24/08/2026`.
- **1.4 International Monetary Fund (IMF) & Sustainable Development Goals**
  - Establishment (1944), Core Mandate (PIMC, Growth, Prosperity), and 6 statutory objectives.
  - Complete catalogue of the 17 United Nations Sustainable Development Goals (SDGs 1–17).
  - *Lecture Date:* `31/08/2026`.
- **1.5 Balance of Payments (BOP) & IMF Macroeconomic Functions**
  - BOP Definition, Current Account, Capital Account, and Financial Account breakdown.
  - Macroeconomic Disequilibrium: Surplus vs. Deficit dynamics.
  - Causes of BOP deficits and corrective policy toolkits (Monetary/Fiscal discipline, Forex reserves, Currency devaluation).
  - Core Pillars of IMF Intervention: Surveillance, Financial Assistance (Lending), and Capacity Development.
  - *Lecture Date:* `01/09/2026`.
- **1.6 Special Drawing Rights (SDR)**
  - Definition & reserve asset nature (1969, not a currency).
  - Multi-Currency Valuation Basket & relative weights (USD 43.39%, EUR 29.31%, CNY 12.28%, JPY 7.59%, GBP 7.44%).
  - Allocation based on IMF Quota shares and SDR interest rate mechanism (SDRi).
  - *Lecture Date:* `02/09/2026`.
- **1.7 Asian Development Bank (ADB) & Institutional Comparison**
  - Institutional Profile (1966, Manila, MDB, Asia-Pacific, India founding member).
  - Four Financing Channels: Loans, Grants, Technical Assistance, Policy Advisory.
  - India-ADB Partnership Priorities: Urban Infra, Transport, Clean Energy, Water/Sanitation, Skills, Climate Resilience.
  - Institutional Comparison: ADB (Regional development bank) vs. IMF (Global monetary authority).
  - *Lecture Date:* `02/09/2026`.
- **1.8 Internationalisation Process**
  - Definition & conceptual scope.
  - Five Progressive Stages: Domestic, Exporting, Subsidiaries & Joint Ventures, Multinational, Transnational.
  - Six Drivers of International Expansion: Saturated domestic growth, cost reduction, competitive pressures, customer following, attractive global cost structures, emerging market growth potential.
  - Four Foreign Market Entry Strategies & Risk Spectrum: Exporting, Licensing & Franchising, Joint Ventures, Direct Investment (Wholly Owned FDI).
  - Comparative Matrix: Strategic Advantages vs. Operational & Environmental Disadvantages.
  - *Lecture Date:* `03/09/2026`.
- **1.9 Emerging Challenges in International Finance (Completes Unit-I)**
  - Twenty systemic challenges categorized across macroeconomic, regulatory, geopolitical, and operational cash management domains.
  - *Lecture Date:* `07/09/2026`.

### **Unit II: The Foreign Exchange Market**
- **2.1 Structure and Participants of the Foreign Exchange Market**
  - Definition, single base unit quotation convention, and two-tier architecture (Wholesale/Interbank vs. Retail/Merchant).
  - Core Participants: Commercial banks, Central banks, Wholesale FX brokers, Exporters/Importers, Multinational Corporations.
  - *Lecture Date:* `07/09/2026`.
- **2.2 Foreign Exchange Quotation Mechanics and Settlement Horizons**
  - Spot rate ($T+2$) vs. Forward rate ($T>2$) delivery horizons.
  - Direct Quotation (Home Currency quote) vs. Indirect Quotation (Foreign Currency quote).
  - Bid-Ask Spread and Percentage Spread formulas with solved numerical calculation.
  - Cross Rates and four settlement horizons: Ready/Cash ($T+0$), TOM ($T+1$), SPOT ($T+2$), Forward ($T>2$).
  - *Lecture Date:* `15/09/2026`.
- **2.3 International Payment and Financial Telecommunication Systems**
  - SWIFT: Cooperative society, Brussels, 250 founding banks, 25,000+ members, BIC routing, Mumbai regional processing hub, core advantages.
  - CHIPS: Computerized electronic clearing system, New York Clearing House Association (1971), paperless USD clearing and multilateral netting.
  - TikZ Flowchart: Dual-tier cross-border settlement architecture (Bank of India $\leftrightarrow$ SWIFT $\leftrightarrow$ Amex Bank $\leftrightarrow$ CHIPS $\leftrightarrow$ Fedwire $\leftrightarrow$ Citi Bank $\leftrightarrow$ Canara Bank).
  - *Lecture Date:* `16/09/2026`.
- **2.4 Market Terminologies, Margins, and Transaction Classifications**
  - Market makers, two-way quotations, forward margins/swap points, forward premium vs. discount, base rate.
  - Golden Rules of Banker's Perspective: Banker's point of view and Foreign currency as the underlying asset.
  - Four-part transaction classification problem (DD on London, TT on New York, Travellers Cheques, Inward DD).
  - Covered Interest Rate Parity (CIP): Exact vs. linear interest differential approximation ($10,000\,\text{USD}$, $8\%$ vs. $5\%$).
  - *Lecture Dates:* `17/09/2026` & `18/09/2026`.
- **2.5 Indian Merchant Rates: Buying Rates and Mechanics**
  - Two Types of Buying Rates: TT Buying Rate vs. Bill Buying Rate.
  - TT Buying Rate application scenarios, exchange margin deduction, and FEDAI rounding off to nearest multiple of $0.0025$.
  - Solved TT Buying Rate Problem: Mail Transfer USD 5,000 with October forward margin and $0.08\%$ exchange margin.
  - Bill Buying Rate mechanics, transit period forward margin treatment (Ascending = Premium, Descending = Discount).
  - Solved Bill Buying Rate Problem: Sight Letter of Credit USD 100,000 with 25-day transit and $0.15\%$ exchange margin.
  - Recovery of interest on commercial bills purchased formula.
  - *Lecture Dates:* `18/09/2026` & `21/09/2026`.
- **2.6 Indian Merchant Rates: Selling Rates and Mechanics**
  - TT Selling Rate vs. Bill Selling Rate definitions and transaction scope.
  - TT Selling Rate calculation format (Interbank Spot Ask + Exchange Margin).
  - Solved TT Selling Rate Problem: Demand Draft on London EUR 25,000 with $0.15\%$ exchange margin.
  - *Lecture Date:* `21/09/2026`.

### **Consolidated Formula Reference Sheet (Rule 5)**
- Placed at document end (`chapters/formula_reference.tex`).
- Chapter-by-chapter grouping of mathematical identities, valuation models, and FEDAI merchant quotation algorithms with explicit structured `Where:` parameter definitions.

---

## 📂 Folder Structure

```text
latex/
├── main.tex                                           # Master root file to compile
├── preamble/
│   ├── packages.tex                                   # Geometry, AMS-Math, TikZ, tcolorbox, hyperref, enumitem, marginnote
│   ├── environments.tex                               # Section-scoped Theorem, Definition, Example & Formulaboxes
│   ├── macros.tex                                     # Shorthands for international finance & FX notations
│   ├── titlepage.tex                                  # Official Pondicherry University title page
│   └── syllabus.tex                                   # Official MSQF 535 syllabus & CO-PO matrix
├── chapters/
│   ├── ch01_international_finance_overview.tex        # Chapter 1: International Finance & BOP (Lectures: 18/08 – 07/09/2026)
│   ├── ch02_foreign_exchange_market.tex               # Chapter 2: The Foreign Exchange Market (Lectures: 07/09 – 21/09/2026)
│   └── formula_reference.tex                          # Consolidated Multi-Chapter Formula Reference Sheet (Rule 5)
├── figures/                                           # Department & University logos
└── README.md                                          # Documentation & compilation instructions
```

---

## 🛠️ How to Compile

Run from inside `Global Financial Management/latex`:
```bash
pdflatex main.tex
pdflatex main.tex  # Second run resolves TOC and cross-references
```
The compiled output is generated as **`main.pdf`**.
