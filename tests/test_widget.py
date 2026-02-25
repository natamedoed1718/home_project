import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "mask_account_card_value, expected",
    [
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Visa 123", ""),
        ("", ""),
        ("Некорректные данные", ""),
    ],
)
def test_mask_account_card(mask_account_card_value, expected):
    assert mask_account_card(mask_account_card_value) == expected


@pytest.mark.parametrize(
    "date_value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("2024-0a-11", ""),  # не цифры
        ("24-03-11", ""),    # год не 4 цифры
        ("2024-3-11", ""),   # месяц 1 цифра
        ("", ""),
        ("Некорректная дата", ""),
    ],
)
def test_get_date(date_value, expected):
    assert get_date(date_value) == expected
