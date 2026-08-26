# Global Financial Management — LaTeX Notes (MSQF Semester III)

This folder contains the complete modular LaTeX setup for your **Global Financial Management** course notes.

## 📂 Folder Structure

```text
latex/
├── main.tex                       # Master root file to compile
├── figures/
│   └── pondicherry_university_logo.png
├── preamble/
│   ├── packages.tex               # Geometry, AMS-Math, TikZ, tcolorbox, hyperref
│   ├── environments.tex           # Custom Theorem, Definition, Example & Remark boxes
│   ├── macros.tex                 # Shorthands for international finance & FX notations
│   ├── titlepage.tex              # Official Pondicherry University title page
│   └── syllabus.tex               # Official MSQF 535 syllabus & CO-PO matrix
├── chapters/                      # (Place future chapter note files here)
└── README.md                      # Compilation instructions & workflow guide
```

## 🛠️ How to Compile

### 1. Using VS Code (LaTeX Workshop Extension)
1. Open `Global Financial Management/latex/main.tex`.
2. Press `Ctrl + Alt + B` (or click "Build LaTeX project" on the sidebar).
3. Click "View LaTeX PDF" to preview the document side-by-side.

### 2. Using Command Line (`pdflatex` or `latexmk`)
Run from inside the `latex/` directory:
```bash
pdflatex main.tex
pdflatex main.tex  # Second run resolves table of contents & cross-references
```
Or with `latexmk`:
```bash
latexmk -pdf main.tex
```

### 3. Using Overleaf
1. Zip the entire `latex` folder.
2. Upload the zip file directly into a new Overleaf project.
3. Set `main.tex` as the main document and click **Recompile**.

## ➕ Adding New Lectures & Chapters
1. To add a new chapter, create a new file in `chapters/` (e.g. `ch01_international_finance_overview.tex`).
2. Add `\input{chapters/ch01_international_finance_overview.tex}` in `main.tex`.
3. Use the predefined environments:
   - `\begin{definition}{Title}{label} ... \end{definition}`
   - `\begin{theorem}{Title}{label} ... \end{theorem}`
   - `\begin{example}{Problem Title}{label} ... \end{example}`
   - `\begin{formulabox}[Title] ... \end{formulabox}`
   - `\begin{remarkbox}[Title] ... \end{remarkbox}`
