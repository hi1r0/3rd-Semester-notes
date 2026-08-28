# Financial Mathematics — LaTeX Notes (MSQF Semester III)

This directory contains the modular LaTeX sources, custom styling, problem sets, and compiled notes for the **Financial Mathematics** course (M.Sc. Quantitative Finance, Semester III).

---

## 📑 Syllabus & Course Coverage Roadmap

### **Unit I: Theory of Interest & Time Value of Money**
- **1.1 Time Value of Money & Simple Interest Fundamentals**
  - Definitions of Principal, Simple Interest (SI), Accrued Amount, and Exact/Ordinary time conversion fractions.
  - Additivity and inverse principal schedules.
  - *Solved Examples:* `1.1.1` to `1.1.5` (*Lectures: 13/08/2026, 17/08/2026*).
- **1.2 Compound Interest & Exponential Growth Dynamics**
  - Compounding principles, depreciation (reducing balance), sub-annual conversion, and demographic decay models.
  - *Solved Examples:* `1.2.1` to `1.2.4` (*Lectures: 17/08/2026, 18/08/2026*).
- **1.3 Methods of Analysis**
  - **1.3.1 Compounding:**
    - Multiple compounding conversion periods ($m = 1, 2, 4, 12$).
    - Effective Rate of Interest ($\ERI = (1 + R/m)^m - 1$).
    - Doubling Period formulations: Continuous limit ($\ln 2 \approx 0.693$), Rule of 72, and Rule of 69 ($T = 0.35 + 69/R$).
    - Uneven series of payments & Compound Value Annuity Factor ($\CVAF$).
    - *Solved Examples:* `1.3.1` to `1.3.6` (*Lectures: 18/08/2026, 24/08/2026, 25/08/2026, 27/08/2026*).
  - **1.3.2 Discounting & Present Value Techniques:**
    - Present Value of a Lump Sum & Series of Cash Flows.
    - Construction of Present Value Factor ($\text{PVF}$) schedules.
    - Present Value of Ordinary Annuities ($\PVAF$) and Annuities Due.
    - Constant Perpetuities ($C/R$) & Growing Perpetuities ($C_1/(R-G)$).
    - Finite Growing Annuity streams & Sinking Fund ($\text{S.F.}$) reserve accumulations.
    - *Solved Examples:* `1.3.7` to `1.3.11` (*Lectures: 18/08/2026, 27/08/2026, 28/08/2026*).

---

## 📂 Folder Structure

```text
latex/
├── main.tex                       # Master root file to compile
├── preamble/
│   ├── packages.tex               # Geometry, AMS-Math, TikZ, tcolorbox, hyperref, enumitem
│   ├── environments.tex           # Section-scoped Theorem, Definition, Example & Formulaboxes
│   ├── macros.tex                 # Shorthands for finance/actuarial/quant notations
│   ├── syllabus.tex               # Pondicherry University syllabus page
│   └── titlepage.tex              # Formal cover page
├── chapters/
│   └── ch01_interest_theory.tex   # Chapter 1: Interest Theory (Lectures: 13/08 – 28/08/2026)
├── figures/                       # Department & University logos
└── README.md                      # Documentation & compilation instructions
```

---

## 🛠️ How to Compile

Run from inside `Financial Mathematics/latex`:
```bash
pdflatex main.tex
pdflatex main.tex  # Second run resolves TOC and cross-references
```
The compiled output is generated as **`main.pdf`**.
