import pytest


@pytest.fixture
def card_16():
    return "1234567812345678"


@pytest.fixture
def account_20():
    return "12345678901234567890"


@pytest.fixture
def card_input():
    return "Visa Platinum 1234567812345678"


@pytest.fixture
def account_input():
    return "Счет 12345678901234567890"
