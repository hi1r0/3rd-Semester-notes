# Financial Mathematics — LaTeX Notes (MSQF Semester III)

This folder contains the complete modular LaTeX setup for your **Financial Mathematics** course notes.

## 📂 Folder Structure

```text
latex/
├── main.tex                       # Master root file to compile
├── preamble/
│   ├── packages.tex               # Geometry, AMS-Math, TikZ, tcolorbox, hyperref
│   ├── environments.tex           # Custom Theorem, Definition, Example & Remark boxes
│   └── macros.tex                 # Shorthands for finance/actuarial/quant notations
├── chapters/
│   └── ch01_interest_theory.tex   # Chapter 1: Theory of Simple Interest & solved examples
└── README.md                      # Compilation instructions & workflow guide
```

## 🛠️ How to Compile

### 1. Using VS Code (LaTeX Workshop Extension)
1. Open `Financial Mathematics/latex/main.tex`.
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
1. To add a new chapter, create a new file in `chapters/` (e.g. `ch02_compound_interest.tex`).
2. Add `\input{chapters/ch02_compound_interest.tex}` in [main.tex](file:///d:/MSQF/Semester%20III/Financial%20Mathematics/latex/main.tex).
3. Use the predefined environments:
   - `\begin{definition}{Title}{label} ... \end{definition}`
   - `\begin{theorem}{Title}{label} ... \end{theorem}`
   - `\begin{example}{Problem Title}{label} ... \end{example}`
   - `\begin{formulabox}[Title] ... \end{formulabox}`
   - `\begin{remarkbox}[Title] ... \end{remarkbox}`
