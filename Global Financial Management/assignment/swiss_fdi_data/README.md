# Swiss Foreign Direct Investment (FDI) & Multinational Enterprise (MNE) Datasets (2015–2024)

Official statistical time-series for Switzerland's Foreign Direct Investment (FDI) and Multinational Enterprises (MNE) published by the **Swiss National Bank (SNB)**.

- **Data Portal**: [data.snb.ch](https://data.snb.ch)
- **Time Window**: 2015 – 2024 (Annual)
- **Data Principles**: Directional Principle (Standard OECD / IMF BOP6 framework) & Ultimate Beneficial Owner (UBO) breakdowns where specified.
- **Generated On**: 2026-09-21

---

## Datasets Overview

| Filename | Records | Topics Covered | Key Dimensions |
| :--- | :--- | :--- | :--- |
| [`swiss_fdi_by_country_2015_2024.csv`](./swiss_fdi_by_country_2015_2024.csv) | 4,430 | Inward & Outward FDI: Capital Stocks, Capital Transactions (Flows), and Investment Income | Year, Direction, Metric, Investor Level, Country Code, Country Name, Region Group, Unit, Value |
| [`swiss_fdi_by_sector_2015_2024.csv`](./swiss_fdi_by_sector_2015_2024.csv) | 4,230 | Inward & Outward FDI by Industry and Capital Instrument (Equity, Reinvested Earnings, Debt) | Year, Direction, Metric, Capital Component, Sector Code, Sector Name, Sector Group, Unit, Value |
| [`swiss_mne_subsidiaries_abroad_2015_2024.csv`](./swiss_mne_subsidiaries_abroad_2015_2024.csv) | 3,140 | Operational Data on Non-Resident Subsidiaries of Swiss Enterprises (Staff, Turnover, Enterprise Count) | Year, Indicator, Breakdown Type, Category Code, Category Name, Category Group, Unit, Value |
| [`swiss_mne_parents_in_switzerland_2015_2024.csv`](./swiss_mne_parents_in_switzerland_2015_2024.csv) | 390 | Domestic Staff of Swiss Multinational Parent Enterprises in Switzerland | Year, Indicator, Survey Source, Sector Code, Sector Name, Sector Group, Unit, Value |

---

## SNB Source Cube Mapping

| File | SNB Cube ID | SNB Official Title |
| :--- | :--- | :--- |
| **Country** | `fdiausbla` | Swiss direct investment abroad - Capital stocks - by country and country group |
| **Country** | `fdiaustlanda` | Swiss direct investment abroad - Capital transactions - by country and country group |
| **Country** | `fdiauselanda` | Swiss direct investment abroad - Investment income - by country and country group |
| **Country** | `fdichbinvla` | Foreign direct investment in Switzerland - Capital stocks - by investor level and country |
| **Country** | `fdichtlanda` | Foreign direct investment in Switzerland - Capital transactions - by country |
| **Country** | `fdicheinvla` | Foreign direct investment in Switzerland - Investment income - by investor level and country |
| **Sector** | `fdiausbabsa` | Swiss direct investment abroad - Capital stocks - by type of capital and economic activity |
| **Sector** | `fdiaustabsa` | Swiss direct investment abroad - Capital transactions - by type of capital and economic activity |
| **Sector** | `fdiauseabsa` | Swiss direct investment abroad - Investment income - by type of capital and economic activity |
| **Sector** | `fdichbabsa` | Foreign direct investment in Switzerland - Capital stocks - by type of capital and economic activity |
| **Sector** | `fdichtabsa` | Foreign direct investment in Switzerland - Capital transactions - by type of capital and economic activity |
| **Sector** | `fdicheabsa` | Foreign direct investment in Switzerland - Investment income - by type of capital and economic activity |
| **MNE Abroad** | `opanmuauspbs` | Multinational enterprises: Staff abroad - by economic activity |
| **MNE Abroad** | `opanmuauspland` | Multinational enterprises: Staff abroad - by country and country group |
| **MNE Abroad** | `opanmuausumbs` | Multinational enterprises: Turnover abroad - by economic activity |
| **MNE Abroad** | `opanmuausumland` | Multinational enterprises: Turnover abroad - by country and country group |
| **MNE Abroad** | `opanmuausubs` | Multinational enterprises: Number of enterprises abroad - by economic activity |
| **MNE Abroad** | `opanmuausuland` | Multinational enterprises: Number of enterprises abroad - by country and country group |
| **MNE Parent** | `opanmumkpbs` | Multinational enterprises: Resident parent companies - Number of staff by source and economic activity |

---

## Methodological Notes

1. **Valuation and Units**:
   - Financial figures (`Capital stocks`, `Capital transactions / flows`, `Investment income`, and `Turnover`) are denominated in **CHF Millions** (Swiss Francs).
   - Staff headcounts are denominated in **Thousands of persons** (`Persons (in thousands)`).
   - Enterprise counts are numeric whole numbers (`Count`).

2. **Negative Values**:
   - Negative capital flows denote net disinvestments or capital repatriations back to the investor.
   - Negative investment income denotes operating losses or write-downs.

3. **Confidentiality / Missing Values**:
   - When figures cannot be disclosed by the SNB to protect business secrets of individual enterprises (often in smaller partner countries or highly consolidated industry sectors), the `Value` cell is intentionally blank (`""`).

4. **Investor Level (Inward FDI)**:
   - *Immediate investor*: Attributes the investment to the direct country of origin of the funds.
   - *Ultimate beneficial owner (UBO)*: Attributes the investment to the domicile of the ultimate controlling parent corporation.

5. **Reproducibility**:
   - The accompanying script [`fetch_swiss_fdi.py`](./fetch_swiss_fdi.py) can be run at any time to re-query the SNB API and update these datasets.
