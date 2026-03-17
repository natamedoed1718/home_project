from unittest.mock import patch
from src.external_api import convert_to_rub

# Транзакция в рублях - не конвертируем


def test_convert_rub():
    transaction = {"operationAmount": {"amount": "500", "currency": {"code": "RUB"}}}

    result = convert_to_rub(transaction)
    assert result == 500.0


# Транзакция в USD - конвертация через mock


@patch("src.external_api.requests.get")
def test_convert_usd(mock_get):
    # создаём "фейковый" ответ API
    mock_get.return_value.json.return_value = {"rates": {"RUB": 90.0}}  # курс USD - RUB

    transaction = {"operationAmount": {"amount": "10", "currency": {"code": "USD"}}}

    result = convert_to_rub(transaction)

    # 10 USD * 90 = 900 RUB
    assert result == 900.0

    # проверяем, что requests.get вызвался
    mock_get.assert_called_once()


# Транзакция в EUR - конвертация через mock
@patch("src.external_api.requests.get")
def test_convert_eur(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 100.0}}  # курс EUR - RUB

    transaction = {"operationAmount": {"amount": "5", "currency": {"code": "EUR"}}}

    result = convert_to_rub(transaction)

    # 5 EUR * 100 = 500 RUB
    assert result == 500.0
    mock_get.assert_called_once()


# Транзакция с неизвестной валютой - возвращает исходную сумму


def test_convert_unknown_currency():
    transaction = {"operationAmount": {"amount": "123", "currency": {"code": "GBP"}}}

    result = convert_to_rub(transaction)
    assert result == 123.0
