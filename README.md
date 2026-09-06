# Health Data Automation - DATASUS

A Python and pandas script that cleans and standardizes a DATASUS export on the number
of blood bags per municipality in the state of Paraná, producing a spreadsheet ready
for analysis.

## Problem

The DATASUS export glues the municipality name to its IBGE code (`410690 CURITIBA`),
wraps it in quotes, uses all caps, and includes rows with no value. In that shape it
cannot be joined with other datasets or presented directly.

## What the script does

**Input:** `raw/municipio.csv` (semicolon-separated)

1. Removes the leading IBGE numeric code from the municipality name
2. Strips quotes and surrounding whitespace
3. Normalizes the text to title case (`Foz Do Iguacu`)
4. Renames the value column to `Quantidade de Bolsas de Sangue`
5. Converts the values to numbers and drops municipalities with no record (total <= 0)

**Output:** `clean/clean_data.xlsx`

## Tech

- Python 3
- pandas
- openpyxl (`.xlsx` writing)

## Structure

```
.
├── raw/
│   ├── extracaohemobanco.py   # cleaning script
│   └── municipio.csv          # raw DATASUS data
└── clean/
    └── clean_data.xlsx        # result
```

## Running

```bash
pip install pandas openpyxl
python raw/extracaohemobanco.py
```

Paths are resolved relative to the script itself, so it runs from any directory.
`clean/clean_data.xlsx` is overwritten on each run.

## About the data

Public data, aggregated by municipality (DATASUS / Paraná blood centers). No personal
information.

## Authorship

Written by Giovanna Ribas dos Reis - individual project.

## Next steps

- Accept the input file name as a parameter instead of hard-coding it
- Detect the year column automatically instead of the fixed `'2026'` value

## Transparency

The code in this project is my own work, not AI-generated.
