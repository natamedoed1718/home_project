import pytest
from src.masks import  get_mask_card_number
from src.masks import get_mask_account

@pytest.mark.parametrize(
    "input_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
        ("12345678", "1234 56** 5678"),
        ("", ""),
        ("Нет номера карты", ""),
    ],
)
def test_mask_card_number(input_number, expected):
    assert get_mask_card_number(input_number) == expected


def test_long_card_number():
    result = get_mask_card_number("12345678123456781234")
    assert isinstance(result, str)


def test_none_input():
    with pytest.raises(TypeError):
        get_mask_card_number(None)



@pytest.mark.parametrize(
    "input_account, expected",
    [
        # Стандартный 20-значный счет
        ("12345678901234567890", "**7890"),

        # С пробелами
        ("1234 5678 9012 3456 7890", "**7890"),

        # С дефисами
        ("1234-5678-9012-3456-7890", "**7890"),

        # Ровно 4 цифры
        ("1234", "**1234"),

        # Меньше 4 цифр (граничные случаи)
        ("123", "**123"),
        ("12", "**12"),
        ("1", "**1"),

        # Пустая строка
        ("", ""),

        # Только пробелы
        ("     ", ""),

        # Текст без цифр
        ("Нет счета", ""),

        # Смешанные символы
        ("Счет № 12345678901234567890", "**7890"),
    ],
)
def test_get_mask_account(input_account, expected):
    assert get_mask_account(input_account) == expected


def test_none_input():
    """None должен вызывать ошибку"""
    with pytest.raises(TypeError):
        get_mask_account(None)


def test_idempotency():
    """
    Повторное применение функции
    не должно изменять уже замаскированный результат
    """
    masked = get_mask_account("12345678901234567890")
    assert get_mask_account(masked) == masked


def test_preserves_last_four_digits():
    """Проверяем, что последние 4 цифры сохраняются"""
    result = get_mask_account("1111222233334444")
    assert result.endswith("4444")


