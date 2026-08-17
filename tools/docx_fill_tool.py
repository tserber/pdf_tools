import argparse
import logging

from tools.base import BaseTool
from transform.docx_template_filler import DocxTemplateFiller
from transform.values_loader import ValuesLoader

logger = logging.getLogger(__name__)


class DocxFillTool(BaseTool):
    name = "docx-fill"
    description = "Fill a Word template's {{ placeholders }} with values from a JSON or Excel file."

    def __init__(self, template_path: str, values_path: str, output_path: str):
        self.template_path = template_path
        self.values_path = values_path
        self.output_path = output_path

    @classmethod
    def add_arguments(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("template_path", help="Path to the .docx template with {{ placeholders }}")
        parser.add_argument("values_path", help="Path to a .json or .xlsx file with placeholder values")
        parser.add_argument("output_path", help="Path to write the filled .docx file")

    @classmethod
    def from_args(cls, args: argparse.Namespace) -> "DocxFillTool":
        return cls(
            template_path=args.template_path,
            values_path=args.values_path,
            output_path=args.output_path,
        )

    def run(self) -> int:
        values = ValuesLoader.load(self.values_path)
        DocxTemplateFiller(self.template_path).render(values, self.output_path)
        return 0
