import json
from typing import Any, Dict, List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает список транзакций из JSON файла."""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)  # Читаем JSON
            # «Это список или нет?»
            if isinstance(data, list):
                return data
            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
