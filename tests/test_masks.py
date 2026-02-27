import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_value, expected",
    [
        # Стандартный 16-значный номер
        ("1234567812345678", "1234 56** **** 5678"),
        # С пробелами
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
        # Короткий номер (8 цифр)
        ("12345678", ""),
        # Нестандартная длина (длинный номер)
        ("12345678123456781234", ""),
        # Пустая строка
        ("", ""),
        # Строка без цифр
        ("Нет номера карты", ""),
    ],
)
def test_get_mask_card_number(card_value, expected):
    assert get_mask_card_number(card_value) == expected


@pytest.mark.parametrize(
    "account_value, expected",
    [
        # Стандартный 20-значный номер
        ("12345678901234567890", "**7890"),
        # С пробелами
        ("12345 678 9 0123 4567890", "**7890"),
        # Короткий номер 5 цифр
        ("12345", ""),
        # Длинный номер
        ("1234567890123456789012345", ""),
        # Пустая строка
        ("", ""),
        # Строка без цифр
        ("Нет номера счета", ""),
    ],
)
def test_get_mask_account(account_value, expected):
    assert get_mask_account(account_value) == expected
