import argparse
import logging
import sys

from extract.pdf_table_extractor import extract_tables
from load.excel.excel_loader import load_tables_to_excel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract PDF tables into an Excel workbook.")
    parser.add_argument("pdf_path", help="Path to the source PDF file")
    parser.add_argument("output_path", help="Path to the output .xlsx file")
    args = parser.parse_args()

    tables = extract_tables(args.pdf_path)
    if not tables:
        logger.warning("No tables found in %s", args.pdf_path)
        return 1

    load_tables_to_excel(tables, args.output_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
