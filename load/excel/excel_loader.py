import logging

import pandas as pd

logger = logging.getLogger(__name__)


def load_tables_to_excel(tables: list[dict], output_path: str) -> None:
    logger.info("Writing %d table(s) to %s", len(tables), output_path)

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        for entry in tables:
            df = pd.DataFrame(entry["data"][1:], columns=entry["data"][0])
            sheet_name = f"Page_{entry['page']}_Table_{entry['table']}"[:31]
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            logger.info("Wrote sheet '%s' (%d rows)", sheet_name, len(df))

    logger.info("Finished writing workbook: %s", output_path)
