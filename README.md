# pdf_tools
Pdf tools, extract, transform, load

## What it does

Extracts every table from a PDF and writes each one to its own sheet in an
Excel workbook (`Page_<n>_Table_<m>`).

- `extract/pdf_table_extractor.py` — pulls tables out of a PDF with `pdfplumber`.
- `load/excel/excel_loader.py` — writes extracted tables into an `.xlsx` file with `openpyxl`.
- `main.py` — CLI entry point wiring the two together.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

### Command line

```bash
python main.py path/to/input.pdf path/to/output.xlsx
```

### PyCharm

Open the project in PyCharm and use either:

- **Run configuration (one click)**: the dropdown next to the run/debug
  toolbar buttons already has an **Extract PDF Tables** configuration.
  Open **Run > Edit Configurations > Extract PDF Tables** once to set the
  `Parameters` field to your own `<input.pdf> <output.xlsx>` paths, then
  click the green ▶ run button any time after.
- **Gutter icon**: open `main.py` and click the green ▶ next to
  `if __name__ == "__main__":`. PyCharm will prompt for the missing script
  parameters (or edit the auto-created run configuration the same way as above).
