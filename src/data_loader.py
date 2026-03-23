from typing import Any, Dict, List, cast
import pandas as pd


def load_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    try:
        df = pd.read_csv(file_path)

        if df.empty:
            return []

        return cast(List[Dict[str, Any]], df.to_dict(orient="records"))

    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []


def load_transactions_from_xlsx(file_path: str) -> List[Dict[str, Any]]:
    """Читает транзакции из XLSX файла."""
    try:
        df = pd.read_excel(file_path)

        if df.empty:
            return []

        return cast(List[Dict[str, Any]], df.to_dict(orient="records"))

    except (FileNotFoundError, ValueError):
        return []
