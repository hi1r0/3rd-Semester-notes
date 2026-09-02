---
trigger: always_on
description: Mandatory Git tracking, Markdown synchronization, and LaTeX structural conventions for Semester III lecture notes
---

# Git & Document Structuring Invariants

## 1. Mandatory Git Tracking & Push Habit
- **Always Stage, Commit & Push**: Whenever lecture notes, Word documents, LaTeX source files, compiled PDFs (`main.pdf`), or Markdown documentation are updated and verified:
  1. `git status` to inspect all staged/unstaged changes.
  2. `git add <modified_files>` (including `.tex`, `.pdf`, `.docx`, `.md`, etc.).
  3. `git commit -m "<descriptive message detailing dates and topics added/updated>"`.
  4. `git push origin main` to synchronize changes with the remote GitHub repository.
- **Clean State Verification**: Ensure the working tree is clean and up-to-date with Git after completing every turn.

## 2. Markdown Documentation Synchronization (`README.md`)
- **Keep Documentation Fresh**: Whenever new lecture dates, solved problem sets, or chapters are added or restructured:
  - Update the relevant subject `README.md` (e.g. `Financial Mathematics/latex/README.md` or `Financial Mathematics/README.md`) with the latest chapter overview, date ranges, and list of covered topics.
  - Update the root `README.md` if new subjects, modules, or repository structures are modified.

## 3. LaTeX Example, Section & Content Numbering Alignment
- **No Double-Numbering in Section Headings**: Never include manual serial numbers inside `\section{...}`, `\subsection{...}`, or `\subsubsection{...}` (e.g., write `\subsection{Allocation and Interest Mechanism of SDRs}`, **never** `\subsection{3. Allocation and Interest Mechanism of SDRs}`). LaTeX automatically prepends the hierarchical section counter (e.g., `1.6.3`), which creates duplicate numbers if manual numbers are present.
- **Section-Scoped Numbering**: Always configure example, definition, and theorem boxes with `number within=section` (e.g. `\newtcbtheorem[number within=section]{example}{Example}{...}`) so that example numbers directly match the section number (e.g. Section 1.1 has Examples 1.1.1 to 1.1.5, Section 1.3 has Examples 1.3.1 to 1.3.11).
- **Chronological Date Tags**: Always tag lecture dates on examples and sections using margin notes or header tags (e.g. `\lecturedate{DD/MM/YYYY}`).
- **Natural Flow & Orphan Prevention**: Maintain continuous document flow without arbitrary `\newpage` commands; only introduce manual page breaks where necessary to prevent orphaned subsection headers or split comparison tables.
