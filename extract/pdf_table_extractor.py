import logging

import pdfplumber

logger = logging.getLogger(__name__)


class PdfTableExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def extract(self) -> list[dict]:
        logger.info("Opening PDF: %s", self.pdf_path)
        extracted = []

        with pdfplumber.open(self.pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                tables = page.extract_tables()
                logger.info("Page %d: found %d table(s)", page_num, len(tables))

                for table_num, table in enumerate(tables, start=1):
                    if not table:
                        continue
                    extracted.append({
                        "page": page_num,
                        "table": table_num,
                        "data": table,
                    })

        logger.info("Extracted %d table(s) total from %s", len(extracted), self.pdf_path)
        return extracted
