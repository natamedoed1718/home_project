from src.logger_config import setup_logger


def get_mask_card_number(card_number: str) -> str:
    """Функция для получения номера карты и возвращает маску"""

    new_card_number = card_number.replace(" ", "")
    if not new_card_number.isdigit():
        print("Вы ввели не правильный формат номера карты.")
        return ""

    if len(new_card_number) != 16:
        print("Номер карты не должен содержать больше 16 цифр.")
        return ""

    return new_card_number[:4] + " " + new_card_number[4:6] + "** **** " + new_card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер банковского счета."""
    new_account_number = account_number.replace(" ", "")
    if not new_account_number.isdigit():
        print("Вы ввели не правильный формат номера счета.")
        return ""
    if len(new_account_number) != 20:
        print("Номер счета не должен содержать больше 20 цифр.")
        return ""

    return f"**{account_number[-4:]}"


logger = setup_logger("masks", "logs/masks.log")


def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""

    logger.info("Начало маскирования карты")

    if len(card_number) < 16:
        logger.error("Некорректный номер карты")
        return ""

    masked: str = f"{card_number[:4]} **** **** {card_number[-4:]}"
    logger.info("Маскирование завершено")

    return masked


def get_mask_account_log(account_number: str) -> str:
    """Функция маскирует номер банковского счета."""
    new_account_number = account_number.replace(" ", "")

    if not new_account_number.isdigit():
        logger.error("Неправильный формат номера счета: %s", account_number)
        return ""

    if len(new_account_number) != 20:
        logger.error("Номер счета не 20 цифр: %s", account_number)
        return ""

    masked_account = f"**{account_number[-4:]}"
    logger.info("Маскирование прошло успешно: %s → %s", account_number, masked_account)
    return masked_account
