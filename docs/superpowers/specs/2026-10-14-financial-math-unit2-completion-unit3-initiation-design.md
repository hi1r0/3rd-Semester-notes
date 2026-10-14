# Design Specification: Financial Mathematics Unit II Completion & Unit III Initiation

**Date:** 2026-10-14  
**Topic:** Integration of Lecture Notes from 22/09/2026 to 13/10/2026 (Unit II Conclusion & Unit III Initiation)  
**Target Documents:**
- `Financial Mathematics/latex/main.tex`
- `Financial Mathematics/latex/chapters/ch02_valuation_of_financial_instruments.tex`
- `Financial Mathematics/latex/chapters/ch03_financial_ratios.tex` (New)
- `Financial Mathematics/latex/chapters/formula_reference.tex`
- `Financial Mathematics/latex/README.md`
- `Financial Mathematics/latex/main.pdf`

---

## 1. Problem Statement & Objectives
The MSQF Semester III Financial Mathematics course notes have been updated with new lecture material covering:
1. **Unit II (Chapter 2 Concluding Topics):**
   - **22/09/2026:** Yield to Call (YTC), Call Penalty, Comparison with Yield to Maturity (YTM), and discount/premium yield relationships.
   - **23/09/2026:** Loan Amortization Mechanics, Equal Installment Cash Flow Dynamics, Taxonomy of Amortization Loans, and Strategic Financial Significance.
   - **08/10/2026:** Price-Earnings (P/E) Valuation Model, Earnings Per Share (EPS) Formulations, Multiplier Interpretation, and Numerical Problem.
2. **Unit III (Chapter 3 Initiation: Financial Ratios & Cash Flow Analysis):**
   - **12/10/2026:** Ratio Analysis Fundamentals, 7 Objectives/Advantages, Comprehensive Classification Tree by Purpose/Function (TikZ Diagram conforming to Rule 4), Profitability Ratios Formulations, and Solved Illustration 1 with Trading & P&L Account.
   - **13/10/2026:** Activity / Turnover Ratios, Velocity & Collection/Payment Periods (Inventory, Debtors, Creditors, Working Capital, Fixed Assets, Capital Turnover), and Comprehensive Numerical Problem.
3. **Comprehensive Formula Reference Sheet Integration:**
   - Adding Chapter 2 formula cards (Boxes 13, 14, 15) and a new Chapter 3 section with formula cards (Boxes 16, 17) with mandatory `Where:` parameter lists per Rule 5.

---

## 2. Mathematical Formulations & Content Specifications

### 2.1 Section 2.7: Bond Valuation & Yield to Call (YTC) [Lecture: 22/09/2026]
- **Definition & Context:** YTC measures the annualized rate of return realized by an investor holding a callable bond until its designated call date, where the issuer redeems the bond at a specified call price $CP = \text{Par} + \text{Call Penalty}$.
- **Standard Approximate Formula (Lecture Method):**
  $$\text{Approximate YTC} = \frac{C + \dfrac{CP - P_0}{N_c}}{\dfrac{CP + P_0}{2}}$$
  where:
  - $C$ = Annual coupon payment ($\text{Coupon Rate} \times \text{Par}$)
  - $CP$ = Call price = $\text{Par Value} + \text{Call Penalty}$
  - $P_0$ = Current purchase / market price of the bond
  - $N_c$ = Number of years remaining until the call date
- **Exact Equation (for completeness):**
  $$P_0 = \sum_{t=1}^{N_c} \frac{C}{(1 + \text{YTC})^t} + \frac{CP}{(1 + \text{YTC})^{N_c}}$$
- **Comparative Yield Dynamics (YTM vs. YTC Table):**
  | Parameter | Yield to Maturity (YTM) | Yield to Call (YTC) |
  | :--- | :--- | :--- |
  | **Holding Period** | Held until official maturity date ($N$) | Held until designated call date ($N_c < N$) |
  | **Terminal Payout** | Par Value ($\text{Face Value}$) | Call Price ($CP = \text{Par} + \text{Penalty Fee}$) |
  | **Discount Bond ($P_0 < \text{Par}$)** | Lower yield ($\text{YTM}$) | $\text{YTC} \ge \text{YTM}$ (Earlier capital gain realization) |
  | **Premium Bond ($P_0 > \text{Par}$)** | Higher yield ($\text{YTM}$) | $\text{YTC} \le \text{YTM}$ (Earlier amortization of premium) |
- **Solved Example 2.7.1:**
  - Given: Par = \$1,000, Market Price $P_0 = \$900$ (10% discount), Coupon = 5% (\$50 p.a.), Maturity = 10 years, Call date = 4 years, Call penalty = 3% (\$30 $\implies CP = \$1,030$).
  - Approx YTC $= \dfrac{50 + \frac{1030 - 900}{4}}{\frac{1030 + 900}{2}} = \dfrac{50 + 32.50}{965} = \dfrac{82.50}{965} \approx 8.55\%$.
  - Approx YTM $= \dfrac{50 + \frac{1000 - 900}{10}}{\frac{1000 + 900}{2}} = \dfrac{50 + 10}{950} = \dfrac{60}{950} \approx 6.32\%$.
  - Conclusion: Since $P_0 < \text{Par}$, $\text{YTC} (8.55\%) > \text{YTM} (6.32\%)$.

### 2.2 Section 2.8: Loan Amortization Models [Lecture: 23/09/2026]
- **Core Concept:** Systematic repayment of principal over time via periodic equal debt-service installments ($A$).
- **Mathematical Dynamics:**
  - Constant periodic installment:
    $$A = \frac{P_0 \cdot r}{1 - (1 + r)^{-n}} = \frac{P_0}{\PVAF(r, n)}$$
  - Interest component at period $t$:
    $$I_t = B_{t-1} \cdot r \quad (\text{strictly decreasing})$$
  - Principal repayment component at period $t$:
    $$\Delta B_t = A - I_t \quad (\text{strictly increasing})$$
  - Outstanding balance at period $t$:
    $$B_t = B_{t-1} - \Delta B_t = B_{t-1}(1 + r) - A \to 0 \text{ at } t = n$$
- **Taxonomy of Amortized Loans:**
  1. *Fixed-Rate Fully Amortized Loans:* Constant interest rate, uniform periodic payments.
  2. *Variable / Adjustable-Rate Loans (ARM):* Periodic interest rate resets to benchmark index.
  3. *Bullet / Balloon Loans:* Periodic installments cover interest only (or partial principal); bulk principal due at termination.
  4. *Negative Amortization Loans:* Periodic payment is less than accrued interest; unpaid interest capitalizes into principal ($B_t > B_{t-1}$).
- **Strategic Importance:** Budgetary cash flow certainty, interest expense minimization, creditworthiness establishment, and prevention of debt spiral compounding.

### 2.3 Section 2.9: Price-Earnings (P/E) Valuation Model & EPS [Lecture: 08/10/2026]
- **Formulas:**
  $$\text{P/E Ratio} = \frac{\text{Market Price per Equity Share (MPS)}}{\text{Earnings per Share (EPS)}}$$
  $$\text{EPS} = \frac{\text{Net Income}}{\text{Total Shares Outstanding}} = \frac{\text{Net Profit after Tax } (\NPAT) - \text{Preference Dividend}}{\text{Number of Equity Shares}}$$
- **Valuation Utility:** Represents the market price multiple paid per rupee of ongoing earnings. Higher P/E signifies strong market growth expectations or lower perceived risk.
- **Solved Example 2.9.1:**
  - Given: Stock Price $= \inr 100$, $\text{EPS} = \inr 5$.
  - $\text{P/E} = \dfrac{100}{5} = 20$.
  - Conclusion: Investors are willing to pay $\inr 20$ for every $\inr 1$ of current annual company earnings.

### 2.4 Chapter 3: Financial Ratios and Cash Flow Analysis (`ch03_financial_ratios.tex`)

#### 2.4.1 Section 3.1: Fundamentals of Ratio Analysis & Classification [Lecture: 12/10/2026]
- **Definition & Objectives:** Relational metric between financial variables. 7 Key Objectives: (1) Forecasting, (2) Managerial Control, (3) Communication, (4) Operational Efficiency, (5) Investment Decision-Making, (6) Financial Solvency, (7) Inter-Firm Comparison.
- **TikZ Diagram (Rule 4 Compliant):**
  - Hierarchy diagram with uniform node widths (`text width=3.8cm`), calibrated minimum height, bold navy connectors with $\ge 0.8\,\text{cm}$ clearance.
  - Three primary pillars: **Profitability Ratios**, **Turnover Ratios**, and **Solvency Ratios** (Short-term & Long-term).
- **Profitability Ratios Formulations:**
  $$\text{Gross Profit Ratio} = \frac{\text{Gross Profit}}{\text{Net Sales}} \times 100 = \frac{\text{Net Sales} - \COGS}{\text{Net Sales}} \times 100$$
  $$\text{Operating Profit Ratio} = \frac{\text{Operating Profit}}{\text{Net Sales}} \times 100 = \frac{\text{Gross Profit} - \text{Operating Expenses}}{\text{Net Sales}} \times 100$$
  $$\text{Operating Ratio} = \frac{\COGS + \text{Operating Expenses}}{\text{Net Sales}} \times 100 \implies \text{Operating Ratio} + \text{Operating Profit Ratio} = 100\%$$
  $$\text{Net Profit Ratio} = \frac{\text{Net Profit after Tax}}{\text{Net Sales}} \times 100$$
- **Solved Example 3.1.1 (Illustration 1 from notes):**
  - Multi-column Trading & Operating P&L Account:
    - Net Sales $= 1,00,000 - 4,000 = 96,000$.
    - $\COGS = 11,000 + 70,000 - 14,000 = 67,000$.
    - $\text{Gross Profit} = 96,000 - 67,000 = \inr 29,000$.
    - Operating Expenses $= 3,000 + 6,000 + 200 + 1,000 + 2,000 + 1,800 + 700 + 500 = \inr 15,200$.
    - $\text{Operating Profit} = 29,000 - 15,200 = \inr 13,800$.
    - Non-operating items: Dividend (+1,200), Profit on asset sale (+600), Loss on shares (-300), Tax provision (-7,000) $\implies \text{Net Profit} = 13,800 + 1,500 - 7,000 = \inr 8,300$ (or $\inr 7,500$ based on net profit line).
    - Calculated Ratios:
      1. Gross Profit Ratio $= \dfrac{29,000}{96,000} \times 100 = \mathbf{30.21\%}$
      2. Operating Profit Ratio $= \dfrac{13,800}{96,000} \times 100 = \mathbf{14.38\%}$
      3. Operating Ratio $= \dfrac{67,000 + 15,200}{96,000} \times 100 = \mathbf{85.63\%}$ (Verification: $14.38\% + 85.63\% = 100.01\% \approx 100\%$)
      4. Net Profit Ratio $= \dfrac{7,500}{96,000} \times 100 = \mathbf{7.81\%}$

#### 2.4.2 Section 3.2: Turnover / Activity Ratios & Operational Velocity [Lecture: 13/10/2026]
- **Conceptual Role:** Measurement of capital circulation speed, expressed in **number of times**.
- **Formulas & Velocity Equivalents:**
  - **Inventory Turnover Ratio (ITR):** $\dfrac{\COGS}{\text{Average Inventory}}$ or $\dfrac{\text{Net Sales}}{\text{Average Inventory}}$
    - Inventory Holding Period $= \dfrac{365}{\text{ITR}} \text{ days}$ or $\dfrac{12}{\text{ITR}} \text{ months}$
  - **Debtors Turnover Ratio (DTR):** $\dfrac{\text{Net Credit Sales}}{\text{Average Accounts Receivable}}$
    - Debtors Collection Period $= \dfrac{365}{\text{DTR}} \text{ days}$ or $\dfrac{12}{\text{DTR}} \text{ months}$
  - **Creditors Turnover Ratio (CTR):** $\dfrac{\text{Net Credit Purchases}}{\text{Average Accounts Payable}}$
    - Creditors Payment Period $= \dfrac{365}{\text{CTR}} \text{ days}$ or $\dfrac{12}{\text{CTR}} \text{ months}$
  - **Working Capital Turnover Ratio:** $\dfrac{\text{Net Sales (or Cost of Sales)}}{\text{Net Working Capital}}$
  - **Fixed Assets Turnover Ratio:** $\dfrac{\text{Cost of Sales (or Net Sales)}}{\text{Net Fixed Assets}}$
  - **Capital Turnover Ratio:** $\dfrac{\text{Cost of Sales (or Net Sales)}}{\text{Capital Employed}}$
- **Solved Example 3.2.1 (Comprehensive Turnover Problem):**
  - Given: Total Sales 5,00,000, Cash Sales 40,000, Sales Return 20,000, Debtors 80,000, Bills Receivable 20,000, Purchases 3,00,000, Cash Purchases 50,000, Purchase Returns 10,000, Creditors 60,000, Bills Payable 20,000, Opening Stock 50,000, Closing Stock 40,000, Gross Profit 1,00,000, Fixed Assets 10,00,000.
  - Intermediate Line Items:
    - Net Sales $= 5,00,000 - 20,000 = \inr 4,80,000$
    - Cost of Sales $= 4,80,000 - 1,00,000 = \inr 3,80,000$
    - Average Stock $= \dfrac{50,000 + 40,000}{2} = \inr 45,000$
    - Net Credit Sales $= 5,00,000 - 40,000 - 20,000 = \inr 4,40,000$
    - Average Receivables $= 80,000 + 20,000 = \inr 1,00,000$
    - Net Credit Purchases $= 3,00,000 - 10,000 - 50,000 = \inr 2,40,000$
    - Average Payables $= 60,000 + 20,000 = \inr 80,000$
  - Ratio Outputs:
    1. **Stock Turnover Ratio:** $\dfrac{3,80,000}{45,000} = \mathbf{8.44 \text{ times}}$
    2. **Fixed Asset Turnover Ratio:**
       - Based on Cost of Sales: $\dfrac{3,80,000}{10,00,000} = \mathbf{0.38 \text{ times}}$
       - Based on Net Sales: $\dfrac{4,80,000}{10,00,000} = \mathbf{0.48 \text{ times}}$
    3. **Debtors Turnover Ratio:** $\dfrac{4,40,000}{1,00,000} = \mathbf{4.40 \text{ times}}$
       - Debtors Collection Period $= \dfrac{12}{4.40} = \mathbf{2.73 \text{ months}} \quad \text{or} \quad \dfrac{365}{4.40} = \mathbf{83 \text{ days}}$
    4. **Creditors Turnover Ratio:** $\dfrac{2,40,000}{80,000} = \mathbf{3.00 \text{ times}}$
       - Creditors Payment Period $= \dfrac{12}{3.00} = \mathbf{4.00 \text{ months}} \quad \text{or} \quad \dfrac{365}{3.00} = \mathbf{122 \text{ days}}$

---

## 3. Comprehensive Formula Reference Sheet Plan (`formula_reference.tex`)
- Chapter 2:
  - **Box 13:** Yield to Call (YTC) and Bond Yield Pricing ($\text{YTC} \ge \text{YTM}$ discount vs. $\text{YTC} \le \text{YTM}$ premium).
  - **Box 14:** Loan Amortization Schedule Dynamics ($A$, $I_t$, $\Delta B_t$, $B_t$).
  - **Box 15:** Price-Earnings (P/E) Ratio and Earnings Per Share (EPS) Models.
- Chapter 3:
  - `\section*{Chapter 3: Financial Ratios and Cash Flow Analysis}`
  - **Box 16:** Profitability Ratios (Gross Profit, Operating Profit, Operating Ratio, Net Profit).
  - **Box 17:** Turnover / Activity Ratios and Operational Velocity Periods (Inventory, Debtors, Creditors, Working Capital, Fixed Assets, Capital).
- All boxes strictly comply with Rule 5 (structured `Where:` definitions, formula-only presentation).

---

## 4. Quality & Formatting Invariants
- LaTeX compilation with `pdflatex` must produce 0 errors and 0 overfull hbox warnings.
- Section-scoped numbering for definitions, examples, and theorem boxes.
- TikZ card symmetry and ample connector spacing ($\ge 0.8\,\text{cm}$) per Rule 4.
- Git tracking: Stage, commit with descriptive message, and push to `origin main` (Rule 1).
