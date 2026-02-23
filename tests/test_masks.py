import pytest
from src.masks import get_mask_card_number


@pytest.fixture
def valid_masked_card():
    return "1234 56** **** 5678"


@pytest.mark.parametrize(
    "input_value, expected",
    [
        # Стандартный 16-значный номер
        ("1234567812345678", "1234 56** **** 5678"),
        # С пробелами
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
        # С дефисами
        ("1234-5678-1234-5678", "1234 56** **** 5678"),
        # Короткий номер (8 цифр)
        ("12345678", "1234 56** 5678"),
        # Нестандартная длина (длинный номер)
        ("12345678123456781234", "1234 56** **** 1234"),
        # Пустая строка
        ("", ""),
        # Строка без цифр
        ("Нет номера карты", ""),
    ],
)
def test_get_mask_card_number(input_value, expected):
    assert get_mask_card_number(input_value) == expected
