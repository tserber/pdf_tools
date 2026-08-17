import logging

import pandas as pd

logger = logging.getLogger(__name__)


class ExcelLoader:
    def __init__(self, output_path: str):
        self.output_path = output_path

    def load(self, tables: list[dict]) -> None:
        logger.info("Writing %d table(s) to %s", len(tables), self.output_path)

        with pd.ExcelWriter(self.output_path, engine="openpyxl") as writer:
            for entry in tables:
                df = pd.DataFrame(entry["data"][1:], columns=entry["data"][0])
                sheet_name = f"Page_{entry['page']}_Table_{entry['table']}"[:31]
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                logger.info("Wrote sheet '%s' (%d rows)", sheet_name, len(df))

        logger.info("Finished writing workbook: %s", self.output_path)
