# Design Specification: Year-by-Year Annuity & Growing Annuity Formulas

**Date:** 2026-10-04  
**Topic:** Year-by-Year Annuity and Growing Annuity Calculation Formulas Integration  
**Target Documents:**
- `Financial Mathematics/latex/chapters/ch01_interest_theory.tex`
- `Financial Mathematics/latex/chapters/formula_reference.tex`
- `Financial Mathematics/latex/README.md`
- `Financial Mathematics/latex/main.pdf`

---

## 1. Problem Statement & Motivation
In standard financial mathematics lectures, annuity and growing annuity values can be calculated in two equivalent ways:
1. **Closed-form analytical factor formulas** (using $\CVAF$, $\PVAF$, or Gordon-style factors).
2. **Year-by-year term accumulation / discounting summation formulas** ($\sum$), which make the underlying cash flow mechanics, compounding exponents ($n-t$), and discounting powers $(1+r)^t$ transparent.

The user provided 5 slides illustrating the year-by-year summation representations for:
1. Ordinary Annuity (Present Value)
2. Ordinary Annuity (Future Value)
3. Annuity Due (Present Value)
4. Annuity Due (Future Value)
5. Finite Growing Annuity (Present Value)

This specification defines how these 5 year-by-year formulations and their step-by-step logic will be added into both **Chapter 1** (theory sections) and the **Comprehensive Formula Reference Sheet** (at the end of `main.pdf`).

---

## 2. Mathematical Formulations

### 2.1 Ordinary Annuity — Present Value
- **Summation & Series Expansion:**
  $$\PV_{\text{ord}} = \sum_{t=1}^n \frac{A}{(1 + r)^t} = \frac{A}{(1 + r)^1} + \frac{A}{(1 + r)^2} + \dots + \frac{A}{(1 + r)^n}$$
- **Computational Logic:**
  Discount each period-end payment $A$ received at $t$ back to time $t = 0$ using the discount factor $(1 + r)^{-t}$, then sum all $n$ discounted cash flows.

### 2.2 Ordinary Annuity — Future Value
- **Summation Formulation:**
  $$\FV_{\text{ord}} = \sum_{t=1}^n A \times (1 + r)^{n - t} = A(1 + r)^{n-1} + A(1 + r)^{n-2} + \dots + A(1 + r)^0$$
- **Computational Logic:**
  Compound each period-end payment forward to the final terminal year $n$.
  - Payment 1 (end of Year 1) compounds for $n - 1$ years: $A(1 + r)^{n - 1}$.
  - Payment $t$ (end of Year $t$) compounds for $n - t$ years: $A(1 + r)^{n - t}$.
  - Payment $n$ (end of Year $n$) compounds for $n - n = 0$ years: $A(1 + r)^0 = A$.

### 2.3 Annuity Due — Present Value
- **Summation & Series Expansion:**
  $$\PV_{\text{due}} = \sum_{t=0}^{n-1} \frac{A}{(1 + r)^t} = A + \frac{A}{(1 + r)^1} + \frac{A}{(1 + r)^2} + \dots + \frac{A}{(1 + r)^{n-1}}$$
- **Computational Logic:**
  Payments occur at the beginning of each period ($t = 0, 1, \dots, n-1$).
  - Payment 1 (start of Year 1, $t = 0$): received immediately, no discounting needed ($A$).
  - Payment $n$ (start of Year $n$, $t = n-1$): discounted for $n - 1$ periods ($\frac{A}{(1 + r)^{n-1}}$).

### 2.4 Annuity Due — Future Value
- **Summation Formulation:**
  $$\FV_{\text{due}} = \sum_{t=0}^{n-1} A \times (1 + r)^{n - t} = A(1 + r)^n + A(1 + r)^{n-1} + \dots + A(1 + r)^1$$
- **Computational Logic:**
  Each payment has one additional year to compound relative to an ordinary annuity:
  - Payment 1 (start of Year 1, $t = 0$): compounds for all $n$ full years: $A(1 + r)^n$.
  - Payment $n$ (start of Year $n$, $t = n-1$): compounds for $n - (n - 1) = 1$ year: $A(1 + r)^1$.
  - Relationship to ordinary annuity: $\FV_{\text{due}} = \FV_{\text{ord}} \times (1 + r)$.

### 2.5 Finite Growing Annuity — Present Value
- **Summation Formulation:**
  $$\PV_{\text{growing}} = \sum_{t=1}^n \frac{C_1 \times (1 + g)^{t-1}}{(1 + r)^t}$$
- **Computational Logic (Two-Step Process):**
  - **Step 1:** Calculate the growing cash flow for year $t$:
    $$C_t = C_1(1 + g)^{t-1}$$
  - **Step 2:** Discount that cash flow back to time $t = 0$:
    $$\PV(C_t) = \frac{C_t}{(1 + r)^t} = \frac{C_1(1 + g)^{t-1}}{(1 + r)^t}$$
  - Sum all $n$ discounted terms for $t = 1, 2, \dots, n$.

---

## 3. Structural Integration Plan

### 3.1 Chapter 1 (`ch01_interest_theory.tex`)
1. **Section 1.3.1 (Compounding & Annuity Future Value):**
   - Update `formulabox[Compound Value of an Annuity]` or append a complementary sub-box / paragraph detailing the **Year-by-Year Compound Accumulation Method** for both Ordinary Annuity and Annuity Due.
   - Include payment horizon logic and timeline intuition.
2. **Section 1.3.2 (Discounting & Annuity Present Value):**
   - In `formulabox[Present Value of Annuities (Ordinary Annuity vs. Annuity Due)]`, introduce the **Year-by-Year Discounting Summation Formulation** alongside the closed-form $\PVAF$ factors.
   - Show the expanded series representation for both Ordinary Annuity and Annuity Due ($t=0$ undiscounted term).
3. **Section 1.3.2 (Finite Growing Annuity):**
   - In `formulabox[Present Value of a Growing Annuity]`, append the **Two-Step Year-by-Year Summation Model** with explicit Step 1 ($C_t = C_1(1+g)^{t-1}$) and Step 2 ($\PV = C_t/(1+r)^t$).

### 3.2 Comprehensive Formula Reference Sheet (`formula_reference.tex`)
Follow the user's selected layout: **Grouped sections within each box** (closed-form factor formulas first, then a dedicated Year-by-Year Summation subsection below them).

1. **Box 5 (`5. Annuity Cash Flows: Future Value and Present Value`):**
   - **Subsection A: Closed-Form Factor Formulas:**
     - Ordinary Annuity $\FV = A \cdot \CVAF(R, n) = A \left[\frac{(1+r)^n - 1}{r}\right]$
     - Annuity Due $\FV_{\text{due}} = \FV_{\text{ord}} \times (1 + r) = A \left[\frac{(1+r)^n - 1}{r}\right](1 + r)$
     - Lump Sum $\PV = \frac{A}{(1+r)^n} = A \cdot \PVF(r, n)$
     - Ordinary Annuity $\PV = A \cdot \PVAF(R, n) = A \left[\frac{1 - (1+r)^{-n}}{r}\right]$
     - Annuity Due $\PV_{\text{due}} = \PV_{\text{ord}} \times (1 + r) = A \left[\frac{1 - (1+r)^{-n}}{r}\right](1 + r)$
   - **Subsection B: Year-by-Year Summation Formulas:**
     - Ordinary Annuity $\FV = \sum_{t=1}^n A \,(1 + r)^{n - t}$
     - Annuity Due $\FV = \sum_{t=0}^{n-1} A \,(1 + r)^{n - t}$
     - Ordinary Annuity $\PV = \sum_{t=1}^n \frac{A}{(1 + r)^t} = \frac{A}{(1+r)^1} + \dots + \frac{A}{(1+r)^n}$
     - Annuity Due $\PV = \sum_{t=0}^{n-1} \frac{A}{(1 + r)^t} = A + \frac{A}{(1+r)^1} + \dots + \frac{A}{(1+r)^{n-1}}$
   - **Where:** definitions updated for all variables ($A$, $r$, $n$, $t$, $\CVAF$, $\PVF$, $\PVAF$).

2. **Box 6 (`6. Perpetuities, Finite Growing Annuity, and Sinking Funds`):**
   - **Subsection A: Closed-Form Formulas:**
     - Constant Perpetuity $\PV = \frac{C}{r}$
     - Growing Perpetuity $\PV = \frac{C_1}{r - g} \quad (r > g)$
     - Finite Growing Annuity $\PV = \frac{C_1}{r - g}\left[1 - \left(\frac{1+g}{1+r}\right)^n\right] \quad (r \ne g)$
     - Sinking Fund Deposits (Ordinary & Due)
   - **Subsection B: Year-by-Year Summation Formulation:**
     - Finite Growing Annuity $\PV = \sum_{t=1}^n \frac{C_1 (1 + g)^{t-1}}{(1 + r)^t}$
   - **Where:** definitions updated ($C_1$, $g$, $r$, $n$, $t$, etc.).

---

## 4. Verification & Invariants
- Maintain strict LaTeX formatting: clean compilation with `pdflatex`, 0 errors, 0 overfull hboxes.
- Comply with all git and formatting rules (Rule 3: no double-numbering, Rule 5: combined formula reference sheet with mandatory `Where:` parameter definitions).
- Synchronize `Financial Mathematics/latex/README.md`.
- Commit and push to `origin main` ensuring a clean git working tree.
