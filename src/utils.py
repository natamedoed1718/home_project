import json
from typing import Any, Dict, List

from src.logger_config import setup_logger


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


logger = setup_logger("utils", "logs/utils.log")


def load_transactions_log(file_path: str) -> List[Dict[str, Any]]:
    """Загружает список транзакций из JSON файла."""

    logger.info("Начало загрузки транзакций")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data: Any = json.load(file)

            if isinstance(data, list):
                logger.info("Транзакции успешно загружены")
                return data

            logger.warning("JSON не является списком")
            return []

    except FileNotFoundError:
        logger.error("Файл не найден")
        return []

    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON")
        return []
