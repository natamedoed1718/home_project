import logging
from typing import Final

LOG_FORMAT: Final[str] = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"


def setup_logger(name: str, log_file: str) -> logging.Logger:
    """Создаёт и настраивает логгер."""

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # чтобы не было дублирования логов
    if logger.handlers:
        return logger

    handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")

    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
