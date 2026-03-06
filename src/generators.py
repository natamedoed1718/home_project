from typing import List, Dict, Iterator


def filter_by_currency(
    transactions: List[Dict],  #List[Dict] — список словарей для входных транзакций
    currency_code: str         #Iterator[Dict] — генератор, возвращающий словарь
) -> Iterator[Dict]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции."""
    # Перебираем все транзакции и достаём валюту из вложенного словаря:
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """ Генератор, который принимает список словарей
     с транзакциями и возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction["description"] #Достаём описание

def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт в формате
       XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    for number in range(start, end + 1):
        card_number = "0" * (16 - len(str(number))) + str(number) #обычное добавление нулей строкой
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"