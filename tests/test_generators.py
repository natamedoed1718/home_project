import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency_code, expected_ids",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
        ("EUR", []),  # нет транзакций
    ],
)
def test_filter_by_currency(transactions, currency_code, expected_ids):
    result = list(filter_by_currency(transactions, currency_code))
    assert [t["id"] for t in result] == expected_ids


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions_full(transactions):
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    result = list(transaction_descriptions(transactions))
    assert result == expected


def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (0, 0, ["0000 0000 0000 0000"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator_range(start, end, expected):
    assert (
        list(card_number_generator(start, end)) == expected
    )  # Вызываем генератор и превращаем его в список для сравнения.


def test_card_number_generator_format():
    gen = card_number_generator(1, 5)  # Генератор создаёт номера карт от 1 до 5
    for card_number in gen:  # Проходимся по каждому номеру в генераторе
        # Проверяем длину и пробелы
        assert len(card_number) == 19  # 16 цифр + 3 пробела
        assert all(len(part) == 4 for part in card_number.split(" "))
