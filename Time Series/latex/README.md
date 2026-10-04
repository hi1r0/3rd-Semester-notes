# Applied Time Series Analysis and Forecasting — LaTeX Notes (MSQF Semester III)

This directory contains the modular LaTeX sources, custom styling, mathematical macros, and compiled lecture notes for **Applied Time Series Analysis and Forecasting** (M.Sc. Quantitative Finance, Semester III).

---

## 📑 Syllabus & Course Coverage Roadmap

### **Unit I: Introduction to Time Series & Forecasting Foundations**

- **1.1 Time Series Definition & Decomposition Models**
  - Definition of a chronological time series ($Y$).
  - Four fundamental components:
    - **Trend ($T$):** Long-term progression or secular direction.
    - **Seasonality ($S$):** Short-term periodic fluctuations repeating at regular intervals.
    - **Cyclical ($C$):** Wavelike oscillations over business/economic cycles.
    - **Irregular ($I$):** Random, unpredictable variations or white noise.
  - Classical Decomposition Models:
    - **Additive Model:** $Y = T + S + C + I$.
    - **Multiplicative Model:** $Y = T \times S \times C \times I$.
    - **Logarithmic Linearization:** $\ln(Y) = \ln(T) + \ln(S) + \ln(C) + \ln(I)$.
  - *Lecture Date:* `10/08/2026`.

- **1.2 Time Series Analysis & Forecasting Fundamentals**
  - Qualitative vs. Quantitative data classification.
  - Three observation structural types:
    - Time Series Data ($y_t$).
    - Cross-Sectional Data ($y_i$).
    - Panel Data ($y_{it}$).
  - Operational and strategic benefits of temporal analysis.
  - *Lecture Date:* `13/08/2026`.

- **1.3 Data Notations, Analytical Uses & Forecasting Taxonomy**
  - Mathematical representations of univariate time series ($y_t$), cross-sectional cuts ($y_i$), and longitudinal panels ($y_{it}$).
  - Univariate time series sales realization example.
  - Three primary analytical purposes: Descriptive, Spatial, and Explorative.
  - Six key application areas: Economic indices, sales volume, operational performance, portfolio optimization, demand planning, and yield analysis.
  - Forecasting approaches: Quantitative, Qualitative / Judgmental, and Combination (Consensus).
  - Planning horizons: Short Term (ST: $<3$ months), Medium Term (MT: 3 months to 1 year), Long Term (LT: $5+$ years).
  - Comprehensive Taxonomy Flowchart of Forecasting Methodologies (`figures/forecasting_methods_flowchart.pdf`).
  - Mathematical trend models for annual data:
    - Linear Trend: $Y_t = \beta_0 + \beta_1 t + \varepsilon_t$.
    - Quadratic / Curvilinear Trend: $Y_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \varepsilon_t$.
    - Exponential Trend: $Y_t = \beta_0 e^{\beta_1 t} \cdot \varepsilon_t \iff \ln(Y_t) = \ln(\beta_0) + \beta_1 t + \ln(\varepsilon_t)$.
    - Autoregressive Trend Model ($\AR(p)$): $Y_t = c + \sum_{j=1}^p \phi_j Y_{t-j} + \varepsilon_t$.
  - *Lecture Date:* `17/08/2026`.

### **Upcoming Course Units**
- **Unit II: Smoothing & Univariate Time Series Models** (Moving Averages, Exponential Smoothing, ARMA/ARIMA processes).
- **Unit III: Multivariate Time Series & Cointegration** (VAR, VECM, Granger causality, Johansen cointegration).
- **Unit IV: Volatility Modeling** (ARCH, GARCH, EGARCH, GJR-GARCH for financial asset returns).
- **Unit V: Forecast Evaluation & Applications** (MAE, RMSE, MAPE, Diebold-Mariano tests, financial forecasting).

---

## 📂 Folder Structure

```text
latex/
├── main.tex                                       # Master root LaTeX document
├── main.pdf                                       # High-definition compiled notes PDF
├── preamble/
│   ├── packages.tex                               # Typography, geometry, hyperref, tcolorbox
│   ├── environments.tex                           # Custom colored theorem & callout boxes
│   ├── macros.tex                                 # Probability, time series operators & statistics
│   ├── titlepage.tex                              # Official Pondicherry University title page
│   └── syllabus.tex                               # Official course syllabus & CO-PO matrix
├── chapters/
│   ├── ch01_intro_time_series.tex                 # Unit I: Introduction to Time Series (Lectures: 10/08 – 17/08/2026)
│   ├── ch02_smoothing_and_univariate_models.tex   # Unit II: Smoothing & Univariate Models (Upcoming)
│   ├── ch03_multivariate_and_cointegration.tex     # Unit III: Multivariate & Cointegration (Upcoming)
│   ├── ch04_volatility_modeling.tex               # Unit IV: Volatility Modeling (Upcoming)
│   └── ch05_forecast_evaluation_and_applications.tex # Unit V: Forecast Evaluation (Upcoming)
├── figures/
│   ├── forecasting_methods_flowchart.pdf          # Full-page landscape forecasting taxonomy
│   └── pondicherry_university_logo.png            # Official institutional emblem
└── README.md                                      # Documentation & compilation instructions
```

---

## 📊 Companion Course Materials

- **Practical Spreadsheets (Parent Directory):**
  - [`../moving_average.xlsx`](../moving_average.xlsx): Spreadsheet models for simple, centered, and weighted moving averages.
  - [`../assignment.xlsx`](../assignment.xlsx): Empirical problem sets and data analysis workbook.
- **Lecture Notes Archive:**
  - [`../notes/`](../notes/): Scanned/handwritten lecture materials including `timeseries (18-09-2026).pdf`, `timeseries (25-09-2026).pdf`, and `Nikhitha timeseries (25-09-2026).pdf`.

---

## 🛠️ How to Compile

To compile the notes locally using MiKTeX or TeX Live:

```bash
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex  # Second run resolves TOC, bookmarks, and cross-references
```

The compiled document will be updated as **`main.pdf`**.
