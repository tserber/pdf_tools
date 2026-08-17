import argparse
import logging

from extract.pdf_table_extractor import PdfTableExtractor
from load.excel.excel_loader import ExcelLoader
from tools.base import BaseTool

logger = logging.getLogger(__name__)


class PdfToExcelTool(BaseTool):
    name = "pdf-to-excel"
    description = "Extract every table from a PDF and write each one to its own sheet in an Excel workbook."

    def __init__(self, pdf_path: str, output_path: str):
        self.pdf_path = pdf_path
        self.output_path = output_path

    @classmethod
    def add_arguments(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("pdf_path", help="Path to the source PDF file")
        parser.add_argument("output_path", help="Path to the output .xlsx file")

    @classmethod
    def from_args(cls, args: argparse.Namespace) -> "PdfToExcelTool":
        return cls(pdf_path=args.pdf_path, output_path=args.output_path)

    def run(self) -> int:
        tables = PdfTableExtractor(self.pdf_path).extract()
        if not tables:
            logger.warning("No tables found in %s", self.pdf_path)
            return 1

        ExcelLoader(self.output_path).load(tables)
        return 0
