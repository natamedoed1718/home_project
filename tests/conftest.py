import pytest
from src.processing import sort_by_date

@pytest.fixture
def card_value():
    return "1234567812345678"


@pytest.fixture
def account_value():
    return "12345678901234567890"


@pytest.fixture
def mask_account_card_value():
    return "Visa Platinum 1234567812345678"


@pytest.fixture
def date_value():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def operations():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]

@pytest.fixture
def same_dates_data():
    """Данные с одинаковыми датами"""
    return [
        {"date": "2024-01-01"},
        {"date": "2024-01-01"},
    ]
def test_sort_by_date_same_dates(same_dates_data):
    """Одинаковые даты"""
    result = sort_by_date(same_dates_data)
    assert len(result) == 2

@pytest.fixture
def invalid_date_transactions():
    """Транзакции с некорректными датами для тестов сортировки."""
    return [
        {"date": "Некорректная дата"},
        {"date": "2024-01-01"},
    ]

def test_sort_by_date_invalid_format(invalid_date_transactions):
    result = sort_by_date(invalid_date_transactions)
    assert len(result) == 2
