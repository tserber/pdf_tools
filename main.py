import argparse
import logging
import sys

from tools.docx_fill_tool import DocxFillTool
from tools.pdf_to_excel_tool import PdfToExcelTool

TOOLS = {
    PdfToExcelTool.name: PdfToExcelTool,
    DocxFillTool.name: DocxFillTool,
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description="pdf_tools: extract, transform, load command line tools.")
    subparsers = parser.add_subparsers(dest="tool", required=True)

    for tool_name, tool_cls in TOOLS.items():
        tool_parser = subparsers.add_parser(tool_name, help=tool_cls.description)
        tool_cls.add_arguments(tool_parser)

    args = parser.parse_args()
    tool = TOOLS[args.tool].from_args(args)
    return tool.run()


if __name__ == "__main__":
    sys.exit(main())
