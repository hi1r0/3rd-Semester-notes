# Specification: International Finance (MBAS120) Syllabus Integration and Standardization

- **Date:** 2026-11-04
- **Author:** Antigravity (Pair Programming with User)
- **Status:** Approved via `/grill-me` Design Interview
- **Source Document:** `D:\MSQF\International Finance Syllabus .pdf`
- **Target Location:** `D:\MSQF\Semester III\International Finance\`

---

## 1. Executive Summary & Objectives

The user requested processing the official 3-page syllabus for **International Finance** (`D:\MSQF\International Finance Syllabus .pdf`), standardizing its structure and documentation to match the exact format of the previous build (`Financial Mathematics`, `Financial Engineering & Derivatives`, `Global Financial Management`, etc.), and deleting the source PDF file after safe preservation.

Course Metadata from Source:
- **Course Code:** MBAS120
- **Course Title:** INTERNATIONAL FINANCE
- **Nature of Course:** Elective (Core / Elective: Elective)
- **Structure (L T P C):** 3 0 0 3 (3 Lecture Hours, 0 Tutorial, 0 Practical, 3 Credits)
- **Total Lecture Hours:** 45 Hours (5 Units × 9 Hours)

---

## 2. Architecture & Deliverables

### A. Safe Document Preservation & Source Cleanup
1. **Preserve Official PDF:** Copy `D:\MSQF\International Finance Syllabus .pdf` to `D:\MSQF\Semester III\International Finance\International_Finance_Syllabus.pdf`.
2. **Integrity Verification:** Inspect using `pypdf` to verify exact 3-page structure and textual presence of `MBAS120`, `INTERNATIONAL FINANCE`, `UNIT: 1` through `UNIT: 5`, and CO-PO matrix.
3. **Safe Cleanup:** Delete the root source file `D:\MSQF\International Finance Syllabus .pdf` as explicitly commanded by the user.

### B. Subject-Level Documentation in `International Finance/`
1. **`International Finance/syllabus.md`:**
   - Standardized Markdown syllabus matching the established typography and layout of `Financial Mathematics/syllabus.md` and `Financial Engineering & Derivatives/syllabus.md`.
   - Complete verbatim transcription:
     - Header block (Code, Title, Credits, Structure, Local Directory, Master PDF reference).
     - Course Objectives & Classroom Methodology.
     - Course Outcomes (CO1 to CO5).
     - Unit-wise Syllabus (Units 1 to 5, 9 hours each).
     - Complete bibliography (Textbooks 1–3, Reference Books 1–5, Online Contents 1–5).
     - Mapping of COs with POs (PO1–PO5, PSO1, PSO2).
2. **`International Finance/README.md`:**
   - Standardized subject README matching the style of other Semester III courses.
   - Comprehensive directory table indexing `syllabus.md`, `International_Finance_Syllabus.pdf`, `IF Unit  2.pptx`, and `Unit_III_Foreign_Exchange_Exposure_Risk.pptx`.
   - Core syllabus overview outlining the 5 units.

### C. Master Documentation Synchronization
1. **Root `README.md`:**
   - Add `International Finance/` to the Repository Structure tree with its files.
   - Add a dedicated subsection for `International Finance (MBAS120 — Elective, 3 Credits)` in the "Subjects Covered" section.
2. **Root `SYLLABUS.md`:**
   - Add an integrated syllabus section for `MBAS120: International Finance (Elective, 3 Credits)` covering objectives, outcomes, units, reference texts, and CO-PO matrix.

### D. Git Tracking & Remote Push
- Stage all modified and created files (`International Finance/*`, `README.md`, `SYLLABUS.md`, spec and plan files).
- Commit with a descriptive message following repository conventions.
- Push to `origin/main` and verify clean working tree.

---

## 3. Verification & Acceptance Criteria

1. **Preservation Check:** `International Finance/International_Finance_Syllabus.pdf` exists and has exactly 3 valid pages.
2. **Source Deletion Check:** `D:\MSQF\International Finance Syllabus .pdf` no longer exists.
3. **Text Completeness:** `International Finance/syllabus.md` and `SYLLABUS.md` contain all 5 units, 5 COs, textbook references, and CO-PO matrices without omissions.
4. **Link Integrity:** All relative markdown links resolve correctly.
5. **Clean Working Tree:** `git status` reports working tree clean and up-to-date with `origin/main`.
