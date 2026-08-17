# pdf_tools
Pdf tools, extract, transform, load

A small collection of ETL command-line tools built around PDFs. Every tool is
a class registered in the `TOOLS` dict at the top of `main.py`; run one by
name through the shared CLI.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py <tool-name> [tool arguments]
```

## Tools

### pdf-to-excel

Extracts every table from a PDF and writes each one to its own sheet in an
Excel workbook (`Page_<n>_Table_<m>`), preserving text as UTF-8 throughout.
It's built from two composable classes — `PdfTableExtractor` (extract) and
`ExcelLoader` (load) — orchestrated by `PdfToExcelTool`.

```bash
python main.py pdf-to-excel path/to/input.pdf path/to/output.xlsx
```

Additional tools get their own subsection here, following the same pattern:
a short paragraph describing what the tool does, followed by its CLI
invocation.

## PyCharm

Open the project in PyCharm and use either:

- **Run configuration (one click)**: the dropdown next to the run/debug
  toolbar buttons already has an **Extract PDF Tables** configuration.
  Open **Run > Edit Configurations > Extract PDF Tables** once to set the
  `Parameters` field to `pdf-to-excel <input.pdf> <output.xlsx>` with your
  own paths, then click the green ▶ run button any time after.
- **Gutter icon**: open `main.py` and click the green ▶ next to
  `if __name__ == "__main__":`. PyCharm will prompt for the missing script
  parameters (or edit the auto-created run configuration the same way as above).

## Project structure

```
pdf_tools/
├── extract/
│   └── pdf_table_extractor.py   PdfTableExtractor — extract phase
├── load/
│   └── excel/
│       └── excel_loader.py      ExcelLoader — load phase
├── tools/
│   ├── base.py                  BaseTool — shared tool interface
│   └── pdf_to_excel_tool.py     PdfToExcelTool — orchestrates a tool end-to-end
└── main.py                      TOOLS registry + CLI dispatcher
```

Adding a new tool means adding a new class under `tools/` that implements
`BaseTool`, and one line registering it in the `TOOLS` dict in `main.py` —
no changes needed anywhere else.
