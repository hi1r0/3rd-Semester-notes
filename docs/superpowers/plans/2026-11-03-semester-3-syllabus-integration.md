# Semester III Syllabus Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extract, author, format, and synchronize the authentic Pondicherry University M.Sc. Quantitative Finance Semester III syllabus across root and subject directories in `D:\MSQF\Semester III`, strictly matching `D:\MSQF\PUSyllabusMscQuantitativeFinance2025-26-02072026.pdf`.

**Architecture:** A multi-layered syllabus ecosystem comprising: (1) a lossless 8-page extracted PDF (`Semester_III_Syllabus.pdf`), (2) a master Markdown document (`SYLLABUS.md`), (3) dedicated per-course `syllabus.md` files, (4) LaTeX monograph syllabus integration in `ML/latex/preamble/syllabus.tex` with clean PDF compilation, (5) folder name sanitation (`Corporate Internship`), and (6) synchronized root `README.md` with git commit/push to `origin/main`.

**Tech Stack:** Python 3 (`pypdf`), LaTeX (`pdflatex`), Markdown, Git / PowerShell.

## Global Constraints

- **Exact Fidelity:** Course codes, titles, credit counts, course objectives, course outcomes (COs), unit descriptions, reference books, and CO-PO matrices must match the university syllabus PDF verbatim.
- **Enrolled Courses:** Covers the 7 courses active in Semester III (MSQF 531, 532, 533, 534, 535, 536 Hard Core + MSQF 542 Soft Core Elective), plus notes the remaining university soft-core electives.
- **Git Invariant:** Follow repository rules: stage modified and created files, commit with descriptive message, and push to `origin/main`. Clean working tree verification.

---

### Task 1: Lossless PDF Extraction for `Semester_III_Syllabus.pdf`

**Files:**
- Create: `scratch/extract_semester_3_syllabus.py`
- Create: `Semester_III_Syllabus.pdf`
- Source: `D:\MSQF\PUSyllabusMscQuantitativeFinance2025-26-02072026.pdf`

**Interfaces:**
- Input: `D:\MSQF\PUSyllabusMscQuantitativeFinance2025-26-02072026.pdf`
- Extracted 1-based Pages: 6 (Curriculum Scheme), 27 (MSQF 531), 28 (MSQF 532), 29 (MSQF 533), 30 (MSQF 534), 31 (MSQF 535), 32 (MSQF 536), 46 (MSQF 542)
- Output: `D:\MSQF\Semester III\Semester_III_Syllabus.pdf` (8 pages)

- [ ] **Step 1: Write extraction and verification script**

```python
# scratch/extract_semester_3_syllabus.py
import pypdf
import os

source_pdf = r"D:\MSQF\PUSyllabusMscQuantitativeFinance2025-26-02072026.pdf"
target_pdf = r"D:\MSQF\Semester III\Semester_III_Syllabus.pdf"

# 1-indexed pages: [6, 27, 28, 29, 30, 31, 32, 46] -> 0-indexed: [5, 26, 27, 28, 29, 30, 31, 45]
page_indices = [5, 26, 27, 28, 29, 30, 31, 45]

reader = pypdf.PdfReader(source_pdf)
writer = pypdf.PdfWriter()

for idx in page_indices:
    writer.add_page(reader.pages[idx])

with open(target_pdf, "wb") as f:
    writer.write(f)

print(f"Successfully generated {target_pdf} with {len(writer.pages)} pages.")
```

- [ ] **Step 2: Run extraction script**

Run: `python scratch/extract_semester_3_syllabus.py`
Expected: "Successfully generated D:\MSQF\Semester III\Semester_III_Syllabus.pdf with 8 pages."

- [ ] **Step 3: Verify extracted PDF integrity and page content**

```python
# scratch/verify_extracted_pdf.py
import pypdf

target_pdf = r"D:\MSQF\Semester III\Semester_III_Syllabus.pdf"
reader = pypdf.PdfReader(target_pdf)
assert len(reader.pages) == 8, f"Expected 8 pages, got {len(reader.pages)}"

expected_markers = [
    "CHOICE BASED CREDIT SYSTEM",
    "MSQF 531",
    "MSQF 532",
    "MSQF 533",
    "MSQF 534",
    "MSQF 535",
    "MSQF 536",
    "MSQF 542"
]

for i, marker in enumerate(expected_markers):
    text = reader.pages[i].extract_text()
    assert marker in text, f"Page {i+1} missing expected marker '{marker}'"
    print(f"Page {i+1} verified: contains '{marker}'")

print("ALL 8 PAGES VERIFIED SUCCESSFULLY.")
```

Run: `python scratch/verify_extracted_pdf.py`
Expected: "ALL 8 PAGES VERIFIED SUCCESSFULLY."

- [ ] **Step 4: Commit extracted PDF**

```bash
git add Semester_III_Syllabus.pdf scratch/extract_semester_3_syllabus.py
git commit -m "feat: extract official 8-page Semester III syllabus PDF directly from university curriculum"
```

---

### Task 2: Author Root Master Markdown `SYLLABUS.md`

**Files:**
- Create: `D:\MSQF\Semester III\SYLLABUS.md`

**Interfaces:**
- Contains complete, verbatim transcripts of:
  - Table of Semester III Course Structure & Credits (6 Hard Core + 2 Soft Core = 29/32 credits)
  - MSQF 531: Applied Time Series Analysis and Forecasting (4 credits)
  - MSQF 532: Financial Mathematics (4 credits)
  - MSQF 533: Financial Risk Management (4 credits)
  - MSQF 534: Corporate Internship (6 credits)
  - MSQF 535: Global Financial Management (4 credits)
  - MSQF 536: Machine Learning Techniques (4 credits)
  - MSQF 542: Financial Engineering and Derivatives (3 credits)
  - Appendix: Master List of Soft Core Courses offered under the CBCS regulations.

- [ ] **Step 1: Write `SYLLABUS.md`**

Write `D:\MSQF\Semester III\SYLLABUS.md` using `write_file` with the exact text of objectives, outcomes, unit content, reference books, and CO-PO matrices for all 7 courses.

- [ ] **Step 2: Verify content completeness**

Verify with python script checking:
- Heading for all 7 course codes (`MSQF 531` through `MSQF 536`, `MSQF 542`)
- Units I through V present for all lecture courses
- CO1 through CO5 present for all courses
- Reference books listed with exact titles.

- [ ] **Step 3: Commit `SYLLABUS.md`**

```bash
git add SYLLABUS.md
git commit -m "docs: create comprehensive verbatim Semester III syllabus markdown reference"
```

---

### Task 3: Directory Sanitization & Subject-Level Markdown Syllabi

**Files:**
- Rename: `D:\MSQF\Semester III\Coporate Internship` -> `D:\MSQF\Semester III\Corporate Internship`
- Create:
  - `Time Series/syllabus.md`
  - `Financial Mathematics/syllabus.md`
  - `Financial Risk Management/syllabus.md`
  - `Corporate Internship/syllabus.md`
  - `Global Financial Management/syllabus.md`
  - `ML/syllabus.md`
  - `Financial Engineering & Derivatives/syllabus.md`

- [ ] **Step 1: Rename `Coporate Internship` to `Corporate Internship`**

Run: `git mv "Coporate Internship" "Corporate Internship"`
Expected: Clean git rename tracking.

- [ ] **Step 2: Create individual `syllabus.md` files in each subject directory**

Generate each subject's standalone `syllabus.md` containing its specific verbatim syllabus, objectives, outcomes, unit breakdowns, reference books, and CO-PO matrix.

- [ ] **Step 3: Verify all 7 files exist and are populated**

```powershell
Get-ChildItem -Path @(
    "Time Series/syllabus.md",
    "Financial Mathematics/syllabus.md",
    "Financial Risk Management/syllabus.md",
    "Corporate Internship/syllabus.md",
    "Global Financial Management/syllabus.md",
    "ML/syllabus.md",
    "Financial Engineering & Derivatives/syllabus.md"
) | Select-Object Name, Length, FullName
```
Expected: All 7 files exist with length > 1000 bytes.

- [ ] **Step 4: Commit subject-level syllabus files and folder rename**

```bash
git add "Corporate Internship" "Time Series/syllabus.md" "Financial Mathematics/syllabus.md" "Financial Risk Management/syllabus.md" "Global Financial Management/syllabus.md" "ML/syllabus.md" "Financial Engineering & Derivatives/syllabus.md"
git commit -m "docs: rename Corporate Internship folder and add subject-level syllabus.md files across all 7 courses"
```

---

### Task 4: LaTeX Integration for `ML/latex` & Preamble Verbatim Alignment

**Files:**
- Create: `ML/latex/preamble/syllabus.tex`
- Modify: `ML/latex/main.tex`
- Modify: `Financial Mathematics/latex/preamble/syllabus.tex` (fix `DDDM` -> `DDM`)
- Verify: `Financial Risk Management/latex/preamble/syllabus.tex`, `Global Financial Management/latex/preamble/syllabus.tex`, `Time Series/latex/preamble/syllabus.tex`
- Output: `ML/latex/main.pdf`

- [ ] **Step 1: Create `ML/latex/preamble/syllabus.tex`**

Format MSQF 536 Machine Learning Techniques syllabus to fit cleanly on a single page matching the established monochrome style (table, course objectives, CO1–CO5, Units I–V, Books for Reference, CO-PO matrix).

- [ ] **Step 2: Update `ML/latex/main.tex`**

Add `\input{preamble/syllabus.tex}` directly after the title page block in `ML/latex/main.tex`.

- [ ] **Step 3: Fix minor typo in `Financial Mathematics/latex/preamble/syllabus.tex`**

Replace `dividend discount model (DDDM)` with `dividend discount model (DDM)` to match the official syllabus text verbatim.

- [ ] **Step 4: Compile `ML/latex/main.tex` with pdflatex**

Run:
```bash
cd "D:\MSQF\Semester III\ML\latex"
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
Expected: Exit code 0, `main.pdf` compiled cleanly with TOC updated.

- [ ] **Step 5: Commit LaTeX additions and updated compiled PDF**

```bash
git add "ML/latex/preamble/syllabus.tex" "ML/latex/main.tex" "ML/latex/main.pdf" "Financial Mathematics/latex/preamble/syllabus.tex"
git commit -m "feat(ML/latex): integrate official MSQF 536 syllabus page and compile updated main.pdf"
```

---

### Task 5: Root `README.md` Synchronization, Git Tracking & Remote Push

**Files:**
- Modify: `D:\MSQF\Semester III\README.md`

- [ ] **Step 1: Update `README.md`**

Update repository structure tree:
- Add `Semester_III_Syllabus.pdf`
- Add `SYLLABUS.md`
- Fix `Corporate Internship/` folder name
- Document all 7 courses and syllabus access links.

- [ ] **Step 2: Verify git status**

Run: `git status`
Expected: Working tree clean, everything staged or committed.

- [ ] **Step 3: Commit README.md and push to remote**

```bash
git add README.md
git commit -m "docs: synchronize master README.md with Semester III syllabus and updated directory structure"
git push origin main
```
Expected: Pushed cleanly to `origin/main`.

---

## Plan Self-Review Check
- [x] Spec coverage: Tasks 1-5 cover all requirements from `2026-11-03-semester-3-syllabus-integration-design.md`.
- [x] No placeholders: Complete code blocks and commands specified.
- [x] Consistency: File paths and course codes match across all tasks.
