import json
import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


class ValuesLoader:
    @staticmethod
    def load(values_path: str) -> dict:
        suffix = Path(values_path).suffix.lower()
        logger.info("Loading placeholder values from: %s", values_path)

        if suffix == ".json":
            values = ValuesLoader._load_json(values_path)
        elif suffix in (".xlsx", ".xls"):
            values = ValuesLoader._load_excel(values_path)
        else:
            raise ValueError(f"Unsupported values file type: {suffix}")

        logger.info("Loaded %d placeholder value(s)", len(values))
        return values

    @staticmethod
    def _load_json(values_path: str) -> dict:
        with open(values_path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def _load_excel(values_path: str) -> dict:
        df = pd.read_excel(values_path)
        df.columns = [str(column).strip().lower() for column in df.columns]

        if "placeholder" not in df.columns or "value" not in df.columns:
            raise ValueError("Excel values file must have 'placeholder' and 'value' columns")

        return dict(zip(df["placeholder"], df["value"]))
