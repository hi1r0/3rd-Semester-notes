# Year-by-Year Annuity & Growing Annuity Formulas Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrate the 5 year-by-year calculation formulas (Ordinary Annuity FV/PV, Annuity Due FV/PV, Finite Growing Annuity PV) into Chapter 1 and the Comprehensive Formula Reference Sheet of the Financial Mathematics lecture notes.

**Architecture:** Enrich LaTeX source files (`ch01_interest_theory.tex` and `formula_reference.tex`) with structured formula boxes and explanatory subsections, compile `main.pdf` using `pdflatex`, and update documentation (`README.md`).

**Tech Stack:** LaTeX (`pdflatex`, `tcolorbox`, `amsmath`, `booktabs`), Git, Markdown.

## Global Constraints
- Section-scoped numbering (Rule 3): no manual serial numbers inside `\section`, `\subsection`, or `\subsubsection`.
- No standalone formula reference section in Chapter 1; single consolidated Comprehensive Formula Reference Sheet at document end (`formula_reference.tex`, Rule 5).
- Mandatory structured `Where:` parameter definitions in all reference sheet formula boxes (Rule 5).
- Zero compilation errors and zero overfull hbox warnings.
- Clean git working tree and commit/push to `origin main` (Rule 1).

---

### Task 1: Update Chapter 1 Theory Sections with Year-by-Year Formulations

**Files:**
- Modify: `Financial Mathematics/latex/chapters/ch01_interest_theory.tex`
- Test: Compile `Financial Mathematics/latex/main.tex` using `pdflatex`

**Interfaces:**
- Consumes: Theory definitions in Section 1.3 of `ch01_interest_theory.tex`.
- Produces: Year-by-year summation formulas and cash flow mechanics in Section 1.3.1 and 1.3.2.

- [ ] **Step 1: Inspect Section 1.3.1 and Section 1.3.2 insertion points in `ch01_interest_theory.tex`**
- [ ] **Step 2: Add Year-by-Year Compound Accumulation subsection in Section 1.3.1 (Future Value)**
  Insert year-by-year formulation for Ordinary Annuity FV and Annuity Due FV:
  $$\FV_{\text{ord}} = \sum_{t=1}^n A \,(1 + r)^{n - t}$$
  $$\FV_{\text{due}} = \sum_{t=0}^{n-1} A \,(1 + r)^{n - t}$$
  with timeline compounding intuition ($t=1 \to n-1$, $t=n \to 0$ vs. $t=0 \to n$, $t=n-1 \to 1$).
- [ ] **Step 3: Add Year-by-Year Discounting Summation in Section 1.3.2 (Present Value)**
  Incorporate summation representations for Ordinary Annuity PV and Annuity Due PV:
  $$\PV_{\text{ord}} = \sum_{t=1}^n \frac{A}{(1 + r)^t} = \frac{A}{(1 + r)^1} + \frac{A}{(1 + r)^2} + \dots + \frac{A}{(1 + r)^n}$$
  $$\PV_{\text{due}} = \sum_{t=0}^{n-1} \frac{A}{(1 + r)^t} = A + \frac{A}{(1 + r)^1} + \frac{A}{(1 + r)^2} + \dots + \frac{A}{(1 + r)^{n-1}}$$
  with cash flow discounting mechanics.
- [ ] **Step 4: Add Two-Step Year-by-Year Summation for Finite Growing Annuity in Section 1.3.2**
  Add:
  $$\PV_{\text{growing}} = \sum_{t=1}^n \frac{C_1 \,(1 + g)^{t-1}}{(1 + r)^t}$$
  detailing Step 1 ($C_t = C_1(1+g)^{t-1}$) and Step 2 ($\PV(C_t) = C_t / (1+r)^t$).
- [ ] **Step 5: Compile `main.tex` and verify zero errors**
  Run: `pdflatex -interaction=nonstopmode main.tex` in `Financial Mathematics/latex`.
- [ ] **Step 6: Commit changes to git**
  `git add Financial Mathematics/latex/chapters/ch01_interest_theory.tex`
  `git commit -m "feat(financial-math): add year-by-year annuity summation formulas to chapter 1"`

---

### Task 2: Update Comprehensive Formula Reference Sheet (Boxes 5 & 6)

**Files:**
- Modify: `Financial Mathematics/latex/chapters/formula_reference.tex`
- Test: Compile `Financial Mathematics/latex/main.tex` using `pdflatex`

**Interfaces:**
- Consumes: Year-by-year summation formulas defined in Task 1.
- Produces: Enhanced Boxes 5 & 6 in `formula_reference.tex` with grouped closed-form and year-by-year sections.

- [ ] **Step 1: Update Box 5 (Annuity Cash Flows)**
  Restructure Box 5 into two clearly formatted subsections:
  1. `\textbf{Closed-Form Factor Formulas:}` (Ordinary FV, Annuity Due FV, Lump Sum PV, Ordinary PV, Annuity Due PV).
  2. `\textbf{Year-by-Year Summation Formulas:}` (Ordinary FV $\sum_{t=1}^n$, Annuity Due FV $\sum_{t=0}^{n-1}$, Ordinary PV $\sum_{t=1}^n$, Annuity Due PV $\sum_{t=0}^{n-1}$).
  3. Structured `\textbf{Where:}` parameter block.
- [ ] **Step 2: Update Box 6 (Perpetuities, Growing Annuity, Sinking Funds)**
  Restructure Box 6 with:
  1. `\textbf{Closed-Form Formulas:}` (Constant Perpetuity, Growing Perpetuity, Finite Growing Annuity, Sinking Funds).
  2. `\textbf{Year-by-Year Summation Formulation:}` (Finite Growing Annuity $\sum_{t=1}^n \frac{C_1(1+g)^{t-1}}{(1+r)^t}$).
  3. Structured `\textbf{Where:}` parameter block.
- [ ] **Step 3: Compile `main.tex` and verify formatting**
  Run: `pdflatex -interaction=nonstopmode main.tex` in `Financial Mathematics/latex`.
  Verify that formulas fit comfortably within tcolorbox borders without overflow.
- [ ] **Step 4: Commit changes to git**
  `git add Financial Mathematics/latex/chapters/formula_reference.tex`
  `git commit -m "feat(financial-math): add year-by-year summation formulas to reference sheet"`

---

### Task 3: Full Compilation Verification, Documentation Update & Remote Push

**Files:**
- Modify: `Financial Mathematics/latex/README.md`
- Compile: `Financial Mathematics/latex/main.pdf`
- Test: Inspect rendered PDF pages for visual balance and orphan prevention.

**Interfaces:**
- Consumes: Updated Chapter 1 and Formula Reference Sheet.
- Produces: Clean compiled `main.pdf`, updated `README.md`, synchronized git repository.

- [ ] **Step 1: Execute two-pass full compilation of `main.tex`**
  Run:
  `pdflatex -interaction=nonstopmode main.tex`
  `pdflatex -interaction=nonstopmode main.tex`
  Confirm 0 errors and 0 overfull hboxes.
- [ ] **Step 2: Render affected PDF pages to images and inspect visually**
  Use `pdftoppm` to inspect the modified pages in Chapter 1 and the Reference Sheet.
- [ ] **Step 3: Update `Financial Mathematics/latex/README.md`**
  Document the addition of the 5 year-by-year summation formulas under Chapter 1 and the Comprehensive Formula Reference Sheet overview.
- [ ] **Step 4: Stage all modified files, commit and push to remote**
  Run:
  `git add -A`
  `git commit -m "feat(financial-math): incorporate year-by-year annuity formulas in ch01 and formula reference"`
  `git push origin main`
- [ ] **Step 5: Verify clean git status**
  Run `git status` to ensure tree is completely clean.
