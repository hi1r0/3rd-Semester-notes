---
trigger: always_on
description: Mandatory Git tracking and LaTeX structural conventions for Semester III lecture notes
---

# Git & Document Structuring Invariants

## 1. Mandatory Git Tracking & Commit Habit
- **Always Stage & Commit**: Whenever lecture notes, Word documents, LaTeX source files, or compiled PDFs (`main.pdf`) are updated and verified, you MUST automatically run:
  1. `git status` to inspect all staged/unstaged changes.
  2. `git add <modified_files>` (including `.tex`, `.pdf`, `.docx`, etc.).
  3. `git commit -m "<descriptive message detailing dates and topics added/updated>"`.
- **Clean State Verification**: Ensure the working tree is kept clean and up-to-date with Git after completing every turn.

## 2. LaTeX Example & Content Numbering Alignment
- **Section-Scoped Numbering**: Always configure example, definition, and theorem boxes with `number within=section` (e.g. `\newtcbtheorem[number within=section]{example}{Example}{...}`) so that example numbers directly match the section number (e.g. Section 1.1 has Examples 1.1.1 to 1.1.5, Section 1.3 has Examples 1.3.1 to 1.3.11).
- **Chronological Date Tags**: Always tag lecture dates on examples and sections using margin notes or header tags (e.g. `\lecturedate{DD/MM/YYYY}`).
