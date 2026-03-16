import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")

URL = "https://apilayer.com/exchangerates_data-api"


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях.
    """

    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        headers = {"apikey": API_KEY}

        params = {
            "base": currency,
            "symbols": "RUB",
        }

        response = requests.get(URL, headers=headers, params=params, timeout=10)
        data = response.json()

        rate = data["rates"]["RUB"]  # rates- словарь с курсами валют

        return amount * rate

    return amount
