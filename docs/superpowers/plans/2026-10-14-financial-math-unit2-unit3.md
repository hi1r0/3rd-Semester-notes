# Financial Mathematics Unit II Completion & Unit III Initiation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete Unit II (Chapter 2: Sections 2.7–2.9) and initiate Unit III (Chapter 3: Sections 3.1–3.2 with TikZ classification tree and comprehensive problem sets), update the Formula Reference Sheet with Boxes 13–17, verify compilation, and sync git.

**Architecture:** Extend LaTeX source files (`ch02_valuation_of_financial_instruments.tex`, new `ch03_financial_ratios.tex`, `formula_reference.tex`, and `main.tex`), compile `main.pdf` using `pdflatex`, inspect rendering, and synchronize repository.

**Tech Stack:** LaTeX (`pdflatex`, TikZ, `tcolorbox`, `amsmath`, `booktabs`, `tabularx`), Git, Markdown.

## Global Constraints
- Section-scoped numbering (Rule 3): no manual serial numbers inside `\section`, `\subsection`, or `\subsubsection`.
- TikZ visual symmetry and ample connector spacing ($\ge 0.8\,\text{cm}$) per Rule 4.
- Consolidated Comprehensive Formula Reference Sheet at document end (`formula_reference.tex`) with mandatory structured `Where:` parameter lists per Rule 5.
- Zero LaTeX compilation errors and zero overfull hbox warnings.
- Mandatory Git commit and push to `origin main` with clean working tree per Rule 1.

---

### Task 1: Complete Chapter 2 in `ch02_valuation_of_financial_instruments.tex`

**Files:**
- Modify: `Financial Mathematics/latex/chapters/ch02_valuation_of_financial_instruments.tex`
- Test: Compile `Financial Mathematics/latex/main.tex` with `pdflatex`

- [ ] **Step 1: Append Section 2.7: Bond Valuation & Yield to Call (YTC) [Lecture: 22/09/2026]**
  - Definition of YTC and call price $CP = \text{Par} + \text{Call Penalty}$.
  - Formulabox for Approximate YTC:
    $$\text{Approx YTC} = \frac{C + \frac{CP - P_0}{N_c}}{\frac{CP + P_0}{2}}$$
  - Comparative table between YTM and YTC (holding period, terminal payout, discount vs. premium relationships).
  - Solved Example 2.7.1: 10-year, 5% coupon bond at 10% discount (\$900 vs. \$1,000 par), 4-year call with 3% penalty (\$1,030), calculating Approx YTC (8.55%) vs. Approx YTM (6.32%).
- [ ] **Step 2: Append Section 2.8: Loan Amortization Models [Lecture: 23/09/2026]**
  - Definition and core mechanics of amortization.
  - Formulabox for debt-service installment $A = \frac{P_0 \cdot r}{1 - (1+r)^{-n}}$, interest portion $I_t = B_{t-1} \cdot r$, principal portion $\Delta B_t = A - I_t$, and outstanding balance $B_t = B_{t-1} - \Delta B_t$.
  - Structured card breakdown for the 4 types of amortized loans (Fixed rate, Variable rate, Bullet loans, Negative amortization).
  - Key financial advantages of amortization.
- [ ] **Step 3: Append Section 2.9: Price-Earnings (P/E) Valuation Model & EPS [Lecture: 08/10/2026]**
  - Formulabox for $\text{P/E Ratio} = \text{MPS} / \text{EPS}$ and $\text{EPS} = (\NPAT - \text{Pref Div}) / \text{Equity Shares}$.
  - Valuation utility and earnings multiplier interpretation.
  - Solved Example 2.9.1: Stock price $\inr 100$, $\text{EPS} = \inr 5 \implies \text{P/E} = 20$, with analytical conclusion.
- [ ] **Step 4: Compile and test with `pdflatex`**
  - Run `pdflatex -interaction=nonstopmode main.tex` in `Financial Mathematics/latex`.
  - Confirm 0 errors.
- [ ] **Step 5: Commit Chapter 2 additions**
  - `git add "Financial Mathematics/latex/chapters/ch02_valuation_of_financial_instruments.tex"`
  - `git commit -m "feat(financial-math): complete chapter 2 with YTC, amortization, and P/E valuation models"`

---

### Task 2: Create Chapter 3 (`ch03_financial_ratios.tex`) and Register in `main.tex`

**Files:**
- Create: `Financial Mathematics/latex/chapters/ch03_financial_ratios.tex`
- Modify: `Financial Mathematics/latex/main.tex`
- Test: Compile `Financial Mathematics/latex/main.tex` with `pdflatex`

- [ ] **Step 1: Create `ch03_financial_ratios.tex` with Chapter Heading and Section 3.1**
  - Chapter title: `\chapter{Financial Ratios and Cash Flow Analysis}`.
  - Section 3.1: Fundamentals of Ratio Analysis & Classification [Lecture: 12/10/2026].
  - Ratio definition and 7 core advantages/purposes.
  - TikZ Hierarchy Diagram conforming strictly to Rule 4 (uniform card widths, minimum heights, distinct drop-lines with $\ge 0.8\,\text{cm}$ clearance, color-coded pillars for Profitability, Turnover, and Solvency).
  - Formulabox for Profitability Ratios (Gross Profit Ratio, Operating Profit Ratio, Operating Ratio, Net Profit Ratio).
  - Solved Example 3.1.1 (Illustration 1 from notes): Trading & Operating P&L Account, complete calculations of Gross Profit (30.21%), Operating Profit (14.38%), Operating (85.63%), and Net Profit (7.81%).
- [ ] **Step 2: Add Section 3.2: Turnover / Activity Ratios & Operational Velocity [Lecture: 13/10/2026]**
  - Conceptual definition of operational velocity and rotation frequency.
  - Formulabox for Activity Ratios: Inventory turnover & holding period, Debtors turnover & collection period, Creditors turnover & payment period, Working capital turnover, Fixed assets turnover, Capital turnover.
  - Solved Example 3.2.1: Comprehensive Problem from notes (sales, purchases, returns, receivables, payables, stock, fixed assets) with step-by-step intermediate figures and all four turnover metrics and collection/payment days.
- [ ] **Step 3: Register `ch03_financial_ratios.tex` in `main.tex`**
  - Add `\input{chapters/ch03_financial_ratios.tex}` right after Chapter 2 and before `formula_reference.tex`.
- [ ] **Step 4: Compile and test with `pdflatex`**
  - Run `pdflatex -interaction=nonstopmode main.tex` in `Financial Mathematics/latex`.
  - Confirm 0 errors and inspect TikZ tree rendering.
- [ ] **Step 5: Commit Chapter 3 initiation**
  - `git add "Financial Mathematics/latex/chapters/ch03_financial_ratios.tex" "Financial Mathematics/latex/main.tex"`
  - `git commit -m "feat(financial-math): add chapter 3 on financial ratios with TikZ classification tree and solved examples"`

---

### Task 3: Update Comprehensive Formula Reference Sheet (`formula_reference.tex`)

**Files:**
- Modify: `Financial Mathematics/latex/chapters/formula_reference.tex`
- Test: Compile `Financial Mathematics/latex/main.tex` with `pdflatex`

- [ ] **Step 1: Add Chapter 2 Formula Cards (Boxes 13, 14, 15)**
  - Box 13: Yield to Call (YTC) & Bond Yield Conditions ($\text{YTC} \ge \text{YTM}$ discount vs. $\text{YTC} \le \text{YTM}$ premium).
  - Box 14: Loan Amortization Schedule Dynamics ($A, I_t, \Delta B_t, B_t$).
  - Box 15: Price-Earnings (P/E) Ratio & Earnings Per Share (EPS).
  - Structured `Where:` blocks for all parameters.
- [ ] **Step 2: Add Chapter 3 Formula Section & Cards (Boxes 16, 17)**
  - `\newpage\section*{Chapter 3: Financial Ratios and Cash Flow Analysis}`
  - Box 16: Profitability Ratios (Gross Profit, Operating Profit, Operating Ratio, Net Profit).
  - Box 17: Turnover / Activity Ratios and Operational Velocity Periods (Inventory, Debtors, Creditors, Working Capital, Fixed Assets, Capital).
  - Structured `Where:` blocks for all parameters.
- [ ] **Step 3: Optimize page breaks across formula reference sheet**
  - Verify that each box fits cleanly without awkward splitting or orphaned lines.
- [ ] **Step 4: Compile and test with `pdflatex`**
  - Run `pdflatex -interaction=nonstopmode main.tex` in `Financial Mathematics/latex`.
  - Confirm 0 errors and 0 overfull hboxes.
- [ ] **Step 5: Commit Formula Reference additions**
  - `git add "Financial Mathematics/latex/chapters/formula_reference.tex"`
  - `git commit -m "feat(financial-math): add boxes 13-17 to comprehensive formula reference sheet"`

---

### Task 4: Quality Audit, Documentation, Compilation Verification & Remote Push

**Files:**
- Modify: `Financial Mathematics/latex/README.md`
- Compile: `Financial Mathematics/latex/main.pdf`
- Cleanup: Temporary extraction scripts/files.

- [ ] **Step 1: Execute double-pass compilation of `main.tex`**
  - Run `pdflatex -interaction=nonstopmode main.tex` twice.
  - Verify 0 errors, 0 overfull hbox warnings.
- [ ] **Step 2: Render PDF pages to images and verify layout**
  - Use `pdftoppm` to inspect Chapter 2 additions, Chapter 3 TikZ tree, and formula reference sheet pages.
- [ ] **Step 3: Update `Financial Mathematics/latex/README.md`**
  - Document Sections 2.7–2.9 in Chapter 2, new Chapter 3 (Unit III) Sections 3.1–3.2, and Formula Reference Boxes 13–17.
- [ ] **Step 4: Cleanup temporary scratch files**
  - Remove `scratch_extract.txt`, `scratch_detailed_docx.txt`, and temporary files.
- [ ] **Step 5: Stage, commit, and push to remote `origin main`**
  - `git add -A`
  - `git commit -m "feat(financial-math): complete unit 2, initiate unit 3 ratio analysis, update formula reference and README"`
  - `git push origin main`
- [ ] **Step 6: Verify clean git status and output completion**
