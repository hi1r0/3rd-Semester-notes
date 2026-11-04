# International Finance (MBAS120) Syllabus Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Standardize and integrate the International Finance (MBAS120) syllabus into `D:\MSQF\Semester III\International Finance\`, preserve the official PDF, author `syllabus.md` and `README.md`, synchronize root documentation (`README.md` and `SYLLABUS.md`), delete the temporary source file, and push changes to `origin/main`.

**Architecture:** (1) Safe copy and verification of `International_Finance_Syllabus.pdf` before deletion of source file, (2) authoring formatted Markdown syllabus (`syllabus.md`) and subject overview (`README.md`) matching the existing build style, (3) updating master root `README.md` and `SYLLABUS.md`, and (4) automated git tracking and remote push.

**Tech Stack:** Python 3 (`pypdf`), Markdown, Git / PowerShell.

## Global Constraints

- **Exact Fidelity:** Course code MBAS120, Title "INTERNATIONAL FINANCE", Elective (3 Credits, L T P C = 3 0 0 3), 45 total lecture hours (5 units × 9 hours), complete textbooks, references, online links, COs, and PO/PSO mapping table must match the PDF verbatim.
- **Safe Data Cleanup:** Verify copy integrity before deleting `D:\MSQF\International Finance Syllabus .pdf`.
- **Git Habit:** Stage changes, commit with descriptive messages, and push to `origin/main`.

---

### Task 1: Safe PDF Preservation & Source Cleanup

**Files:**
- Create: `D:\MSQF\Semester III\International Finance\International_Finance_Syllabus.pdf`
- Delete: `D:\MSQF\International Finance Syllabus .pdf`

- [ ] **Step 1: Copy source PDF to target folder**

Run PowerShell command:
```powershell
Copy-Item -Path "D:\MSQF\International Finance Syllabus .pdf" -Destination "D:\MSQF\Semester III\International Finance\International_Finance_Syllabus.pdf"
```

- [ ] **Step 2: Verify preserved PDF integrity**

```python
# scratch/verify_if_pdf.py
import pypdf, os

target = r"D:\MSQF\Semester III\International Finance\International_Finance_Syllabus.pdf"
assert os.path.exists(target), "Target PDF does not exist"
reader = pypdf.PdfReader(target)
assert len(reader.pages) == 3, f"Expected 3 pages, got {len(reader.pages)}"

page1 = reader.pages[0].extract_text()
assert "MBAS120" in page1
assert "INTERNATIONAL FINANCE" in page1
assert "UNIT: 1" in page1
print("Target PDF verified with 3 valid pages and expected content.")
```
Run: `python scratch/verify_if_pdf.py`
Expected: "Target PDF verified with 3 valid pages and expected content."

- [ ] **Step 3: Delete source PDF**

Run PowerShell command:
```powershell
Remove-Item -Path "D:\MSQF\International Finance Syllabus .pdf" -Force
```
Verify: `Test-Path "D:\MSQF\International Finance Syllabus .pdf"` returns `False`.

- [ ] **Step 4: Commit preserved PDF**

```bash
git add "International Finance/International_Finance_Syllabus.pdf"
git commit -m "feat(International Finance): preserve authentic 3-page syllabus PDF"
```

---

### Task 2: Author Subject-Level Documentation (`syllabus.md` & `README.md`)

**Files:**
- Create: `D:\MSQF\Semester III\International Finance\syllabus.md`
- Create: `D:\MSQF\Semester III\International Finance\README.md`

- [ ] **Step 1: Write `International Finance/syllabus.md`**

Author verbatim markdown syllabus matching the established format:
- Metadata header (MBAS120, Elective, 3 Credits, L T P C = 3 0 0 3, 45 lecture hours).
- Course Objectives & Methodology.
- Course Outcomes (CO1 to CO5).
- Unit-wise Syllabus (Units 1 to 5, 9 hours each).
- Text Book(s) (1 to 3), Reference Book(s) (1 to 5), Related Online Contents (1 to 5).
- Mapping of COs with POs (PO1–PO5, PSO1, PSO2).

- [ ] **Step 2: Write `International Finance/README.md`**

Author standardized subject README matching the existing course READMEs:
- Metadata and links to `syllabus.md`, `International_Finance_Syllabus.pdf`, and master curriculum.
- Directory contents table indexing `syllabus.md`, `International_Finance_Syllabus.pdf`, `IF Unit  2.pptx`, and `Unit_III_Foreign_Exchange_Exposure_Risk.pptx`.
- Comprehensive Unit 1–5 course coverage summary.

- [ ] **Step 3: Verify subject-level files**

```powershell
Get-ChildItem -Path @("International Finance/syllabus.md", "International Finance/README.md") | Select-Object Name, Length
```
Expected: Both files exist and have non-zero length (> 2000 bytes).

- [ ] **Step 4: Commit subject documentation**

```bash
git add "International Finance/syllabus.md" "International Finance/README.md"
git commit -m "docs(International Finance): add standardized syllabus.md and course README.md"
```

---

### Task 3: Master Documentation Synchronization & Verification

**Files:**
- Modify: `D:\MSQF\Semester III\SYLLABUS.md`
- Modify: `D:\MSQF\Semester III\README.md`

- [ ] **Step 1: Update `SYLLABUS.md`**

Add section for `MBAS120: International Finance (Elective, 3 Credits)` including its course objectives, outcomes, unit breakdown, bibliography, and CO-PO matrix.

- [ ] **Step 2: Update `README.md`**

Update:
- Repository structure tree to include `International Finance/` (`syllabus.md`, `International_Finance_Syllabus.pdf`, PPTX slide decks).
- Subjects Covered section to add `International Finance (MBAS120 — Elective, 3 Credits)`.

- [ ] **Step 3: Run comprehensive verification**

Run test script checking presence of MBAS120 across all target markdown files and verifying link validity.

- [ ] **Step 4: Commit documentation updates**

```bash
git add SYLLABUS.md README.md
git commit -m "docs: synchronize master README.md and SYLLABUS.md with International Finance (MBAS120)"
```

---

### Task 4: Git Synchronization & Remote Push

- [ ] **Step 1: Verify git status**

Run: `git status`
Expected: Working tree clean, branch ahead by commits.

- [ ] **Step 2: Push commits to remote**

Run: `git push origin main`
Expected: Clean push to `origin/main`.

- [ ] **Step 3: Clean state verification**

Run: `git status`
Expected: "Your branch is up to date with 'origin/main'. nothing to commit, working tree clean".
