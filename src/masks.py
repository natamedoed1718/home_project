"""Реализуйте в этом модуле две функции:
Функцию маскировки номера банковской карты
get_mask_card_number
Функцию маскировки номера банковского счета
get_mask_account
"""


def get_mask_card_number(card_number: str) -> str:
    """Функция для получения номера карты и возвращает маску"""

    new_card_number = card_number.replace(" ", "")
    if not new_card_number.isdigit():
        print("Вы ввели не правильный формат номера карты.")
        return ""

    if len(new_card_number) != 16:
        print("Номер карты не должен содержать больше 16 цифр.")
        return ""

    return new_card_number[:4] + " " + new_card_number[4:6] + "** ****" + new_card_number[-4:]


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
