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

## 4. TikZ Visual Symmetry & Connector Spacing Invariants
- **Uniform Box Dimensions (Symmetry) Across Parallel Cards**: 
  - Whenever multiple cards are arranged side-by-side in a row or along a spectrum (e.g., pipeline stages, entry modes, institutional comparisons), all cards MUST share identical geometry: uniform `text width` and an identical `minimum height` calibrated to the tallest card.
  - Symmetrical content formatting: Standardize title lines (e.g. exactly 2 lines per title) and bullet volume across adjacent cards so vertical distribution is visually balanced.
- **Ample Spacing for Transition Arrows**:
  - Inter-node transition arrows must never have cramped or squished arrowheads touching both box borders. Maintain a minimum clear inter-card clearance of $0.6\,\text{cm}$ to $1.0\,\text{cm}$ between card boundaries.
  - Where horizontal space is restricted across 5+ stages, use a connected top chevron process header or elevated numbered step badges with clean drop-lines rather than tiny squashed horizontal arrows.
- **Connector Stem Length & Arrowhead Clearance**:
  - Any directional connector (vertical drop stem, horizontal link, or branch line) MUST have a minimum clear distance of $0.6\,\text{cm}$ to $1.0\,\text{cm}$ between connected node boundaries. This guarantees that the shaft of the arrow is distinct and prominent before the arrowhead begins.
  - Never allow an arrowhead to span the entire gap between two elements (which creates a cramped "stubby" appearance).
  - High-Contrast Arrow Styling: Connectors should use bold stroke widths ($\ge 1.2\,\text{pt}$ to $1.5\,\text{pt}$) and either match the accent color of the destination card or use the primary palette tone (`navyblue`) rather than washed-out faint grays.
- **Balanced Banner Connectors**:
  - Avoid solitary asymmetric downward arrows from a wide multi-column top banner pointing into only the first child card. Top banners should either serve as independent title blocks or provide symmetrical branch lines into all child pillars.

## 5. Mandatory Standalone Formula Sheet Page on New Notes Upload
- **Dedicated Final Page**: At the end of every new lecture notes upload or completed chapter, always conclude with a dedicated standalone page (`\newpage`) reserved exclusively for the **Consolidated Formula Reference / Formula Section Alone**.
- **Formula-Only Content**: This section must strictly present mathematical formulas, equation numbers, variable definitions, and validity conditions grouped by subtopics (e.g., in a high-density summary box or multi-row table), with NO narrative commentary, background prose, or worked examples.
- **Strict Page Budget**: Carefully calibrate vertical spacing and equation density so that the formula sheet sits cleanly on its designated final page without awkward orphan spillover onto an extra blank or near-empty page.


