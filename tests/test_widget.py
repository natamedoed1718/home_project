import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("", ""),
        ("Некорректные данные", ""),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("", ""),
        ("Некорректная дата", ""),
    ],
)
def test_get_date(value, expected):
    assert get_date(value) == expected
