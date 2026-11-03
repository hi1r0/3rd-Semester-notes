# Specification: Semester III Syllabus Integration and Exact Alignment

- **Date:** 2026-11-03
- **Author:** Antigravity (Pair Programming with User)
- **Status:** Approved via `/grill-me` Design Interview
- **Source Document:** `D:\MSQF\PUSyllabusMscQuantitativeFinance2025-26-02072026.pdf` (Pondicherry University M.Sc. Quantitative Finance Syllabus 2025–26 onwards)
- **Target Root:** `D:\MSQF\Semester III`

---

## 1. Executive Summary & Goals

The user requested an exact, authentic extraction and preservation of the Pondicherry University M.Sc. Quantitative Finance Semester III syllabus within `D:\MSQF\Semester III`. Based on the portal registration records and the CBCS curriculum, Semester III comprises 6 Hard Core courses (26 credits) and 1 Soft Core elective course (3 credits), totaling 7 active courses:

1. **MSQF 531:** Applied Time Series Analysis and Forecasting (Hard Core, 4 credits) [PDF p. 27]
2. **MSQF 532:** Financial Mathematics (Hard Core, 4 credits) [PDF p. 28]
3. **MSQF 533:** Financial Risk Management (Hard Core, 4 credits) [PDF p. 29]
4. **MSQF 534:** Corporate Internship (Hard Core, 6 credits) [PDF p. 30]
5. **MSQF 535:** Global Financial Management (Hard Core, 4 credits) [PDF p. 31]
6. **MSQF 536:** Machine Learning Techniques (Hard Core, 4 credits) [PDF p. 32]
7. **MSQF 542:** Financial Engineering and Derivatives (Soft Core Elective, 3 credits) [PDF p. 46]

This design establishes a multi-tiered syllabus architecture:
- A lossless, direct-extracted official standalone PDF (`Semester_III_Syllabus.pdf`) preserving original typography and formatting.
- A comprehensive master Markdown reference (`SYLLABUS.md`) at the repository root.
- Granular subject-level Markdown documents (`syllabus.md`) inside each course folder.
- Synchronized LaTeX preambles (`preamble/syllabus.tex`) for courses with active LaTeX monograph systems (`ML`, `Financial Mathematics`, `Financial Risk Management`, `Global Financial Management`, `Time Series`), with full compilation to `main.pdf`.
- Clean repository alignment (renaming misspelled directory `Coporate Internship` to `Corporate Internship`) and updating root `README.md`.
- Full Git tracking and synchronization to remote repository (`origin/main`).

---

## 2. Architecture & Deliverables

### A. Master Standalone PDF (`Semester_III_Syllabus.pdf`)
- Extracted losslessly via `pypdf` from `D:\MSQF\PUSyllabusMscQuantitativeFinance2025-26-02072026.pdf`.
- Page sequence (8 pages total):
  - Page 1: University CBCS Curriculum Structure & Course Matrix (Original PDF Page 6)
  - Page 2: MSQF 531 Applied Time Series Analysis and Forecasting (Original PDF Page 27)
  - Page 3: MSQF 532 Financial Mathematics (Original PDF Page 28)
  - Page 4: MSQF 533 Financial Risk Management (Original PDF Page 29)
  - Page 5: MSQF 534 Corporate Internship (Original PDF Page 30)
  - Page 6: MSQF 535 Global Financial Management (Original PDF Page 31)
  - Page 7: MSQF 536 Machine Learning Techniques (Original PDF Page 32)
  - Page 8: MSQF 542 Financial Engineering and Derivatives (Original PDF Page 46)

### B. Master Markdown Reference (`SYLLABUS.md`)
- Located at root: `D:\MSQF\Semester III\SYLLABUS.md`.
- Structured with:
  1. CBCS Credit Architecture table for Semester III.
  2. Verbatim course blocks for each of the 7 courses containing:
     - Course Code, Course Title, Nature of Course, Credit Weight
     - Course Objectives (verbatim bullet points)
     - Course Outcomes (CO1 to CO5)
     - Detailed Unit Breakdown (Units I through V / Internship Guidelines)
     - Books for Reference (complete bibliographies with editions and ISBNs)
     - CO-PO Mapping Matrix (exact credit/outcome weight tables)
  3. Appendix: Complete List of Soft Core Electives offered under the M.Sc. Quantitative Finance regulation.

### C. Subject-Level Markdown Files (`<Subject>/syllabus.md`)
Individual standalone syllabus files for fast subject-specific lookup:
- `Time Series/syllabus.md`
- `Financial Mathematics/syllabus.md`
- `Financial Risk Management/syllabus.md`
- `Corporate Internship/syllabus.md`
- `Global Financial Management/syllabus.md`
- `ML/syllabus.md`
- `Financial Engineering & Derivatives/syllabus.md`

### D. LaTeX Syllabus Integration & PDF Compilation
1. **Machine Learning (`ML/latex`):**
   - Create `ML/latex/preamble/syllabus.tex` matching the established monochrome style (as in `Financial Mathematics` and `Financial Risk Management`).
   - Wire `\input{preamble/syllabus.tex}` into `ML/latex/main.tex` right after the title page.
   - Recompile `ML/latex/main.tex` using `pdflatex` (2 passes) to generate updated 60-page `ML/latex/main.pdf`.
2. **Text Verification of Existing Syllabus Files:**
   - Audit `Financial Mathematics/latex/preamble/syllabus.tex` (correct minor discrepancy `DDDM` -> `DDM`).
   - Audit `Financial Risk Management/latex/preamble/syllabus.tex`, `Global Financial Management/latex/preamble/syllabus.tex`, and `Time Series/latex/preamble/syllabus.tex` against the source PDF to guarantee verbatim correspondence.

### E. Directory Sanitation
- Rename `D:\MSQF\Semester III\Coporate Internship` to `D:\MSQF\Semester III\Corporate Internship` to fix the typo.

### F. Documentation Synchronization & Git Push
- Update `D:\MSQF\Semester III\README.md` to index `SYLLABUS.md`, `Semester_III_Syllabus.pdf`, and link the updated course directories.
- Run `git status`, `git add`, `git commit -m "..."`, and `git push origin main` in compliance with repository invariants.

---

## 3. Verification & Acceptance Criteria

1. **Exact Extraction Verification:** Verify that `Semester_III_Syllabus.pdf` contains all 8 target pages and opens cleanly without corruption.
2. **Text Fidelity Check:** Validate that all course titles, unit titles, descriptions, and textbook references in `SYLLABUS.md` match the source PDF verbatim.
3. **LaTeX Build Validation:** `ML/latex/main.pdf` compiles with return code 0, and the syllabus page appears immediately following the title page.
4. **Git Verification:** Working tree is clean and `git status` reports up-to-date with `origin/main`.
