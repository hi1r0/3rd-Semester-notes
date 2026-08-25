# Applied Time Series Analysis and Forecasting - Lecture Notes

**Course:** MSQF 531: Applied Time Series Analysis and Forecasting  
**Degree:** M.Sc. Quantitative Finance (Semester III)  
**Institution:** Department of Statistics, Ramanujan School of Mathematical Sciences, Pondicherry University  
**Student:** N Rohit Vedhanandh (Reg. No.: `25MSQUFPY0002`)  
**Credits:** 4  

---

## Directory Architecture

```
D:\MSQF\Semester III\Time Series\latex\
│
├── main.tex                       # Master root document
├── main.pdf                       # Compiled high-definition publication PDF
│
├── figures/                       # Institutional crests and graphical figures
│   └── pondicherry_university_logo.png
│
├── preamble/                      # Modular LaTeX preamble configurations
│   ├── packages.tex               # Typography, geometry, hyperref, tcolorbox
│   ├── environments.tex           # Custom colored theorem & callout boxes
│   ├── macros.tex                 # Probability, time series operators & statistics
│   ├── titlepage.tex              # Official Pondicherry University title page
│   └── syllabus.tex               # Official course syllabus & CO-PO matrix
│
└── chapters/                      # Course unit chapters
    ├── ch01_intro_time_series.tex # Unit I: Introduction to Time Series
    ├── ch02_smoothing_and_univariate_models.tex (Upcoming)
    ├── ch03_multivariate_and_cointegration.tex (Upcoming)
    ├── ch04_volatility_modeling.tex (Upcoming)
    └── ch05_forecast_evaluation_and_applications.tex (Upcoming)
```

---

## Compilation Instructions

To compile the notes locally using MiKTeX / TeX Live via PowerShell:

```powershell
cd "D:\MSQF\Semester III\Time Series\latex"
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
*(Running twice generates complete table of contents, bookmarks, cross-references, and hyperref links).*
