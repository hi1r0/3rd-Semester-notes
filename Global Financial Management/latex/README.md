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
│   └── ch01_international_finance_overview.tex        # Chapter 1: International Finance & BOP (Lectures: 18/08 – 02/09/2026)
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
