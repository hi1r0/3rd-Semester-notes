"""
Swiss FDI and Multinational Enterprise (MNE) Data Extraction Pipeline (2015-2024)
Source: Swiss National Bank (SNB) Open Data API (data.snb.ch)

This script programmatically downloads, parses, enriches, and normalizes
official Swiss Foreign Direct Investment (FDI) and Multinational Enterprise (MNE)
datasets published by the Swiss National Bank.

Outputs:
1. swiss_fdi_by_country_2015_2024.csv
2. swiss_fdi_by_sector_2015_2024.csv
3. swiss_mne_subsidiaries_abroad_2015_2024.csv
4. swiss_mne_parents_in_switzerland_2015_2024.csv
5. README.md (Data Dictionary and Documentation)
"""

import os
import sys
import csv
import json
import time
import urllib.request
import urllib.error

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
BASE_URL = 'https://data.snb.ch/api/cube'
START_YEAR = 2015
END_YEAR = 2024

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def fetch_json(url, retries=3, delay=1.0):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode('utf-8', errors='ignore'))
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay * (attempt + 1))
            else:
                print(f"[ERROR] Failed to fetch JSON from {url}: {e}", file=sys.stderr)
                raise

def fetch_csv_lines(url, retries=3, delay=1.0):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                content = resp.read().decode('utf-8', errors='ignore')
                return content.splitlines()
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay * (attempt + 1))
            else:
                print(f"[ERROR] Failed to fetch CSV from {url}: {e}", file=sys.stderr)
                raise

def parse_dimension_tree(items, parent_category=None):
    """
    Recursively traverse dimensionItems tree to return:
    id_to_name: dict mapping item ID -> clean English name
    id_to_parent: dict mapping item ID -> parent group/region/sector
    """
    id_to_name = {}
    id_to_parent = {}

    for item in items:
        item_id = item.get('id')
        name = item.get('name', '').replace('\xa0', ' ').strip()
        sub = item.get('dimensionItems', [])

        current_category = parent_category
        if name in ['Europe', 'North America', 'Central and South America', 'Asia', 'Africa', 'Oceania']:
            current_category = name
        elif name in ['Manufacturing', 'Services', 'All sectors']:
            current_category = name

        if item_id:
            id_to_name[item_id] = name
            id_to_parent[item_id] = current_category or 'All / Total'

        if sub:
            sub_names, sub_parents = parse_dimension_tree(sub, current_category)
            id_to_name.update(sub_names)
            id_to_parent.update(sub_parents)

    return id_to_name, id_to_parent

def get_cube_dimensions(cube_id):
    url = f"{BASE_URL}/{cube_id}/dimensions/en"
    dim_data = fetch_json(url)
    dims_map = {}
    for dim in dim_data.get('dimensions', []):
        dim_id = dim.get('id').lower()
        dim_name = dim.get('name', '').replace('\xa0', ' ').strip()
        names, parents = parse_dimension_tree(dim.get('dimensionItems', []))
        dims_map[dim_id] = {
            'name': dim_name,
            'items': names,
            'parents': parents
        }
    return dims_map

def parse_cube_csv(cube_id):
    """
    Download and parse SNB raw CSV for a cube.
    Returns (header_columns_lowercase, data_rows).
    """
    url = f"{BASE_URL}/{cube_id}/data/csv/en"
    lines = fetch_csv_lines(url)
    
    data_lines = []
    header = None
    
    for line in lines:
        line_clean = line.strip().replace('\ufeff', '')
        if not line_clean:
            continue
        parts = [p.strip('"') for p in line_clean.split(';')]
        if not parts:
            continue
        if parts[0].lower() == 'date':
            header = [p.lower() for p in parts]
            continue
        if header and parts[0].isdigit():
            year = int(parts[0])
            if START_YEAR <= year <= END_YEAR:
                data_lines.append(parts)
                
    return header, data_lines

def safe_float_str(val_str):
    if not val_str or val_str.strip() in ['', '.', '...', '-']:
        return ""
    try:
        val = float(val_str.strip())
        return f"{val:.1f}" if val != int(val) else str(int(val))
    except ValueError:
        return val_str.strip()

# ==============================================================================
# DATASET 1: FDI by Country
# ==============================================================================
def build_fdi_by_country():
    print("\n--- Building Dataset 1: swiss_fdi_by_country_2015_2024.csv ---")
    outward_specs = [
        ('fdiausbla', 'Swiss FDI abroad (Outward)', 'Capital stocks', 'Not applicable (Directional outward)'),
        ('fdiaustlanda', 'Swiss FDI abroad (Outward)', 'Capital transactions (flows)', 'Not applicable (Directional outward)'),
        ('fdiauselanda', 'Swiss FDI abroad (Outward)', 'Investment income', 'Not applicable (Directional outward)'),
    ]
    inward_specs = [
        ('fdichbinvla', 'FDI in Switzerland (Inward)', 'Capital stocks', 'MULTI_INVESTOR'),
        ('fdichtlanda', 'FDI in Switzerland (Inward)', 'Capital transactions (flows)', 'Immediate investor'),
        ('fdicheinvla', 'FDI in Switzerland (Inward)', 'Investment income', 'MULTI_INVESTOR'),
    ]

    rows = []

    # Process Outward
    for cube_id, direction, metric, inv_level in outward_specs:
        print(f"Fetching {cube_id} ({direction} - {metric})...")
        dims = get_cube_dimensions(cube_id)
        country_dim = dims.get('d0', {})
        names = country_dim.get('items', {})
        regions = country_dim.get('parents', {})
        header, raw_rows = parse_cube_csv(cube_id)
        
        c_idx = header.index('d0')
        val_idx = header.index('value')

        for r in raw_rows:
            year = int(r[0])
            c_code = r[c_idx]
            val = safe_float_str(r[val_idx]) if val_idx < len(r) else ""
            c_name = names.get(c_code, c_code)
            region = regions.get(c_code, 'Other')
            
            rows.append({
                'Year': year,
                'Direction': direction,
                'Metric': metric,
                'Investor_Level': inv_level,
                'Country_Code': c_code,
                'Country_Name': c_name,
                'Region_Group': region,
                'Unit': 'CHF Millions',
                'Value': val
            })

    # Process Inward
    for cube_id, direction, metric, inv_mode in inward_specs:
        print(f"Fetching {cube_id} ({direction} - {metric})...")
        dims = get_cube_dimensions(cube_id)
        header, raw_rows = parse_cube_csv(cube_id)
        val_idx = header.index('value')

        if inv_mode == 'MULTI_INVESTOR':
            inv_dim = dims.get('d0', {}).get('items', {})
            c_dim = dims.get('d1', {})
            c_names = c_dim.get('items', {})
            c_regions = c_dim.get('parents', {})
            
            inv_idx = header.index('d0')
            c_idx = header.index('d1')

            for r in raw_rows:
                year = int(r[0])
                inv_code = r[inv_idx]
                inv_level_label = inv_dim.get(inv_code, inv_code)
                c_code = r[c_idx]
                val = safe_float_str(r[val_idx]) if val_idx < len(r) else ""
                c_name = c_names.get(c_code, c_code)
                region = c_regions.get(c_code, 'Other')

                rows.append({
                    'Year': year,
                    'Direction': direction,
                    'Metric': metric,
                    'Investor_Level': inv_level_label,
                    'Country_Code': c_code,
                    'Country_Name': c_name,
                    'Region_Group': region,
                    'Unit': 'CHF Millions',
                    'Value': val
                })
        else:
            c_dim = dims.get('d0', {})
            c_names = c_dim.get('items', {})
            c_regions = c_dim.get('parents', {})
            c_idx = header.index('d0')

            for r in raw_rows:
                year = int(r[0])
                c_code = r[c_idx]
                val = safe_float_str(r[val_idx]) if val_idx < len(r) else ""
                c_name = c_names.get(c_code, c_code)
                region = c_regions.get(c_code, 'Other')

                rows.append({
                    'Year': year,
                    'Direction': direction,
                    'Metric': metric,
                    'Investor_Level': inv_mode,
                    'Country_Code': c_code,
                    'Country_Name': c_name,
                    'Region_Group': region,
                    'Unit': 'CHF Millions',
                    'Value': val
                })

    # Sort rows
    rows.sort(key=lambda x: (x['Year'], x['Direction'], x['Metric'], x['Investor_Level'], x['Country_Name']))
    
    out_path = os.path.join(OUTPUT_DIR, 'swiss_fdi_by_country_2015_2024.csv')
    fieldnames = ['Year', 'Direction', 'Metric', 'Investor_Level', 'Country_Code', 'Country_Name', 'Region_Group', 'Unit', 'Value']
    with open(out_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"-> Saved {len(rows)} records to {out_path}")
    return len(rows)

# ==============================================================================
# DATASET 2: FDI by Sector
# ==============================================================================
def build_fdi_by_sector():
    print("\n--- Building Dataset 2: swiss_fdi_by_sector_2015_2024.csv ---")
    sector_specs = [
        ('fdiausbabsa', 'Swiss FDI abroad (Outward)', 'Capital stocks'),
        ('fdiaustabsa', 'Swiss FDI abroad (Outward)', 'Capital transactions (flows)'),
        ('fdiauseabsa', 'Swiss FDI abroad (Outward)', 'Investment income'),
        ('fdichbabsa', 'FDI in Switzerland (Inward)', 'Capital stocks'),
        ('fdichtabsa', 'FDI in Switzerland (Inward)', 'Capital transactions (flows)'),
        ('fdicheabsa', 'FDI in Switzerland (Inward)', 'Investment income'),
    ]

    rows = []

    for cube_id, direction, metric in sector_specs:
        print(f"Fetching {cube_id} ({direction} - {metric})...")
        dims = get_cube_dimensions(cube_id)
        comp_dim = dims.get('d0', {}).get('items', {})
        sec_dim = dims.get('d1', {})
        sec_names = sec_dim.get('items', {})
        sec_parents = sec_dim.get('parents', {})

        header, raw_rows = parse_cube_csv(cube_id)
        comp_idx = header.index('d0')
        sec_idx = header.index('d1')
        val_idx = header.index('value')

        for r in raw_rows:
            year = int(r[0])
            comp_code = r[comp_idx]
            comp_name = comp_dim.get(comp_code, comp_code)
            sec_code = r[sec_idx]
            sec_name = sec_names.get(sec_code, sec_code)
            parent_sec = sec_parents.get(sec_code, 'All')
            val = safe_float_str(r[val_idx]) if val_idx < len(r) else ""

            rows.append({
                'Year': year,
                'Direction': direction,
                'Metric': metric,
                'Capital_Component': comp_name,
                'Sector_Code': sec_code,
                'Sector_Name': sec_name,
                'Sector_Group': parent_sec,
                'Unit': 'CHF Millions',
                'Value': val
            })

    rows.sort(key=lambda x: (x['Year'], x['Direction'], x['Metric'], x['Capital_Component'], x['Sector_Name']))
    
    out_path = os.path.join(OUTPUT_DIR, 'swiss_fdi_by_sector_2015_2024.csv')
    fieldnames = ['Year', 'Direction', 'Metric', 'Capital_Component', 'Sector_Code', 'Sector_Name', 'Sector_Group', 'Unit', 'Value']
    with open(out_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"-> Saved {len(rows)} records to {out_path}")
    return len(rows)

# ==============================================================================
# DATASET 3: MNE Subsidiaries Abroad
# ==============================================================================
def build_mne_subsidiaries_abroad():
    print("\n--- Building Dataset 3: swiss_mne_subsidiaries_abroad_2015_2024.csv ---")
    mne_specs = [
        ('opanmuauspbs', 'Number of staff', 'By Economic Activity', 'Persons (in thousands)'),
        ('opanmuauspland', 'Number of staff', 'By Country', 'Persons (in thousands)'),
        ('opanmuausumbs', 'Turnover', 'By Economic Activity', 'CHF Millions'),
        ('opanmuausumland', 'Turnover', 'By Country', 'CHF Millions'),
        ('opanmuausubs', 'Number of enterprises', 'By Economic Activity', 'Count'),
        ('opanmuausuland', 'Number of enterprises', 'By Country', 'Count'),
    ]

    rows = []

    for cube_id, indicator, breakdown_type, unit in mne_specs:
        print(f"Fetching {cube_id} ({indicator} - {breakdown_type})...")
        dims = get_cube_dimensions(cube_id)
        cat_dim = dims.get('d0', {})
        cat_names = cat_dim.get('items', {})
        cat_parents = cat_dim.get('parents', {})

        header, raw_rows = parse_cube_csv(cube_id)
        cat_idx = header.index('d0')
        val_idx = header.index('value')

        for r in raw_rows:
            year = int(r[0])
            cat_code = r[cat_idx]
            cat_name = cat_names.get(cat_code, cat_code)
            parent_group = cat_parents.get(cat_code, 'All')
            val = safe_float_str(r[val_idx]) if val_idx < len(r) else ""

            rows.append({
                'Year': year,
                'Indicator': indicator,
                'Breakdown_Type': breakdown_type,
                'Category_Code': cat_code,
                'Category_Name': cat_name,
                'Category_Group': parent_group,
                'Unit': unit,
                'Value': val
            })

    rows.sort(key=lambda x: (x['Year'], x['Indicator'], x['Breakdown_Type'], x['Category_Name']))

    out_path = os.path.join(OUTPUT_DIR, 'swiss_mne_subsidiaries_abroad_2015_2024.csv')
    fieldnames = ['Year', 'Indicator', 'Breakdown_Type', 'Category_Code', 'Category_Name', 'Category_Group', 'Unit', 'Value']
    with open(out_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"-> Saved {len(rows)} records to {out_path}")
    return len(rows)

# ==============================================================================
# DATASET 4: MNE Parent Operations in Switzerland
# ==============================================================================
def build_mne_parents_in_switzerland():
    print("\n--- Building Dataset 4: swiss_mne_parents_in_switzerland_2015_2024.csv ---")
    cube_id = 'opanmumkpbs'
    print(f"Fetching {cube_id} (Staff of Swiss Parent Companies in Switzerland)...")
    dims = get_cube_dimensions(cube_id)
    source_dim = dims.get('d0', {}).get('items', {})
    sec_dim = dims.get('d1', {})
    sec_names = sec_dim.get('items', {})
    sec_parents = sec_dim.get('parents', {})

    header, raw_rows = parse_cube_csv(cube_id)
    src_idx = header.index('d0')
    sec_idx = header.index('d1')
    val_idx = header.index('value')

    rows = []
    for r in raw_rows:
        year = int(r[0])
        src_code = r[src_idx]
        src_name = source_dim.get(src_code, src_code)
        sec_code = r[sec_idx]
        sec_name = sec_names.get(sec_code, sec_code)
        parent_group = sec_parents.get(sec_code, 'All')
        val = safe_float_str(r[val_idx]) if val_idx < len(r) else ""

        rows.append({
            'Year': year,
            'Indicator': 'Number of staff',
            'Survey_Source': src_name,
            'Sector_Code': sec_code,
            'Sector_Name': sec_name,
            'Sector_Group': parent_group,
            'Unit': 'Persons (in thousands)',
            'Value': val
        })

    rows.sort(key=lambda x: (x['Year'], x['Survey_Source'], x['Sector_Name']))

    out_path = os.path.join(OUTPUT_DIR, 'swiss_mne_parents_in_switzerland_2015_2024.csv')
    fieldnames = ['Year', 'Indicator', 'Survey_Source', 'Sector_Code', 'Sector_Name', 'Sector_Group', 'Unit', 'Value']
    with open(out_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"-> Saved {len(rows)} records to {out_path}")
    return len(rows)

# ==============================================================================
# DOCUMENTATION: README.md
# ==============================================================================
def write_documentation(stats):
    doc_path = os.path.join(OUTPUT_DIR, 'README.md')
    print(f"\n--- Writing Documentation: {doc_path} ---")
    content = f"""# Swiss Foreign Direct Investment (FDI) & Multinational Enterprise (MNE) Datasets (2015–2024)

Official statistical time-series for Switzerland's Foreign Direct Investment (FDI) and Multinational Enterprises (MNE) published by the **Swiss National Bank (SNB)**.

- **Data Portal**: [data.snb.ch](https://data.snb.ch)
- **Time Window**: 2015 – 2024 (Annual)
- **Data Principles**: Directional Principle (Standard OECD / IMF BOP6 framework) & Ultimate Beneficial Owner (UBO) breakdowns where specified.
- **Generated On**: 2026-09-21

---

## Datasets Overview

| Filename | Records | Topics Covered | Key Dimensions |
| :--- | :--- | :--- | :--- |
| [`swiss_fdi_by_country_2015_2024.csv`](./swiss_fdi_by_country_2015_2024.csv) | {stats.get('country', 0):,} | Inward & Outward FDI: Capital Stocks, Capital Transactions (Flows), and Investment Income | Year, Direction, Metric, Investor Level, Country Code, Country Name, Region Group, Unit, Value |
| [`swiss_fdi_by_sector_2015_2024.csv`](./swiss_fdi_by_sector_2015_2024.csv) | {stats.get('sector', 0):,} | Inward & Outward FDI by Industry and Capital Instrument (Equity, Reinvested Earnings, Debt) | Year, Direction, Metric, Capital Component, Sector Code, Sector Name, Sector Group, Unit, Value |
| [`swiss_mne_subsidiaries_abroad_2015_2024.csv`](./swiss_mne_subsidiaries_abroad_2015_2024.csv) | {stats.get('mne_abroad', 0):,} | Operational Data on Non-Resident Subsidiaries of Swiss Enterprises (Staff, Turnover, Enterprise Count) | Year, Indicator, Breakdown Type, Category Code, Category Name, Category Group, Unit, Value |
| [`swiss_mne_parents_in_switzerland_2015_2024.csv`](./swiss_mne_parents_in_switzerland_2015_2024.csv) | {stats.get('mne_parent', 0):,} | Domestic Staff of Swiss Multinational Parent Enterprises in Switzerland | Year, Indicator, Survey Source, Sector Code, Sector Name, Sector Group, Unit, Value |

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
"""
    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"-> Saved documentation to {doc_path}")

def main():
    print("=" * 70)
    print("SWISS FDI & MNE DATA EXTRACTION PIPELINE (2015-2024)")
    print(f"Target Directory: {OUTPUT_DIR}")
    print("=" * 70)

    stats = {}
    stats['country'] = build_fdi_by_country()
    stats['sector'] = build_fdi_by_sector()
    stats['mne_abroad'] = build_mne_subsidiaries_abroad()
    stats['mne_parent'] = build_mne_parents_in_switzerland()
    write_documentation(stats)

    print("\n" + "=" * 70)
    print("ALL DATASETS SUCCESSFULLY EXTRACTED, TRANSFORMED AND SAVED!")
    print(f"Country breakdown:          {stats['country']:,} rows")
    print(f"Sector breakdown:           {stats['sector']:,} rows")
    print(f"MNE subsidiaries abroad:    {stats['mne_abroad']:,} rows")
    print(f"MNE parent Swiss companies: {stats['mne_parent']:,} rows")
    print("=" * 70)

if __name__ == '__main__':
    main()
