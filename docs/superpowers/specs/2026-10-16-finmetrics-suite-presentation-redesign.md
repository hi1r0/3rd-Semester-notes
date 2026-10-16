# Design Document: FinMetrics Suite Presentation Visual Overhaul & TikZ Redesign

**Date:** 2026-10-16  
**Topic:** FinMetrics Suite Beamer Presentation Overhaul (De-cluttering, TikZ Visuals & Attribution Updates)  
**Directory Target:** `D:\MSQF\Semester III\Coporate Internship`  

---

## 1. Summary of Changes & User Directives

1. **Title & Institutional Attribution:**
   - Department: **Department of Statistics**, Pondicherry University.
   - Program: **M.Sc. Quantitative Finance (MSQF)**.
   - Event Header: **Corporate Internship** only (removed "Final Defense").
   - Title: **FinMetrics Suite** only (removed long subtitle, open source badge, and GitHub URL).
   - Attribution Card: **Single Centered Executive Card** containing:
     - **Candidate:** N Rohit Vedhanandh
     - **Reg No.:** 25MSQUFPY0002
     - **Program:** M.Sc. Quantitative Finance
     - **Faculty Guidance:** Dr. Kiruthika, Department of Statistics, Pondicherry University
     - Removed: Host Organization, Industry Mentor, and Session fields.

2. **Global Styling & Layout Enhancements:**
   - **Footer:** Completely removed (`\setbeamertemplate{footline}{}`).
   - **Header:** Removed `FinMetrics-PU` pill from top-right corner of `frametitle`.
   - **De-cluttering:** Replaced cramped text blocks with balanced spacing and eliminated all overfull box warnings.

3. **Pure Native TikZ Visuals Across the Deck:**
   - **Slide 2:** TikZ diagram contrasting Gaussian bell curve displacement vs. robust median.
   - **Slide 3:** Refined 4-stage pipeline with improved spacing ($\ge 0.8\,\text{cm}$ clearance) and clean connectors.
   - **Slide 4:** TikZ 5-Pillar segmented visual hierarchy and safe-division guard card.
   - **Slide 5:** Native TikZ Boxplot with annotated quartiles ($Q_1, \text{Median}, Q_3$), whiskers, fences ($\mathcal{F}_{\text{lower}}, \mathcal{F}_{\text{upper}}$), and highlighted outlier points.
   - **Slide 6:** TikZ Isolation Forest diagram illustrating 2D random hyperplanes and shallow tree depth ($h(x) < 4$).
   - **Slide 7:** Native TikZ curve of Sigmoid function $S(x)$ showing percentile anchors ($50, 35, 65$) and asymptotes ($0, 100$).
   - **Slide 8:** TikZ 5-Tier Health Meter (Excellent, Strong, Moderate, Weak, Distressed) alongside the classification table.
   - **Slide 9:** TikZ architecture diagram of Gemini key rotation and 6-tab Excel delivery.
   - **Slide 10:** Cross-sectional performance matrix with empirical findings.
   - **Slide 11:** Uncluttered strategic takeaways and closing banner.

---

## 2. Updated Color Palette (Pure Monochromatic Emerald & Jade)

- `deepemerald`: `#064E3B` (`RGB(6, 78, 59)`) — Primary headings, frame titles, borders.
- `forestgreen`: `#0D5C3A` (`RGB(13, 92, 58)`) — Secondary headers, node backgrounds.
- `jade`: `#059669` (`RGB(5, 150, 105)`) — Badges, outlier highlight markers, active graph lines.
- `lightsage`: `#EBF5EE` (`RGB(235, 245, 238)`) — Container fills.
- `mintborder`: `#A7F3D0` (`RGB(167, 243, 208)`) — Crisp card outlines ($0.7\,\text{pt}$).
- `paperbg`: `#F7FBF9` (`RGB(247, 251, 249)`) — Soft mint slide canvas.
- `darkcharcoal`: `#0F172A` (`RGB(15, 23, 42)`) — High-contrast text.
- `slatygray`: `#475569` (`RGB(71, 85, 105)`) — Muted annotations.
