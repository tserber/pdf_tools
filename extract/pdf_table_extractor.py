import logging

import pdfplumber

logger = logging.getLogger(__name__)


def extract_tables(pdf_path: str) -> list[dict]:
    logger.info("Opening PDF: %s", pdf_path)
    extracted = []

    with pdfplumber.open(pdf_path) as pdf:
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

    logger.info("Extracted %d table(s) total from %s", len(extracted), pdf_path)
    return extracted
