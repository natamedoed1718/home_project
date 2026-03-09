from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """
    Функция принимает строку с типом и номером карты или счета
    и возвращает строку с замаскированным номером
    """

    if not card_or_account:
        return ""

    parts = card_or_account.split()

    number = parts[-1]
    name = " ".join(parts[:-1])

    if "Счет" in card_or_account:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    if not masked_number:
        return ""

    return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Функция, которая принимает на вход строку
    с датой в одном формате
    и возвращает в другом формате
    """

    # Проверяем, что строка не пустая
    if not date_str:
        return ""

    # Берём только первые 10 символов
    date_part = date_str[:10]
    # Разделяем строку по символу "-"
    parts = date_part.split("-")

    # Проверяем, что частей ровно три
    if len(parts) != 3:
        return ""

    year, month, day = parts

    # Проверяем, что все части состоят только из цифр
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return ""

    # Проверяем корректную длину частей
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return ""

    return f"{day}.{month}.{year}"
pass
