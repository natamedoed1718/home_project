
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency,transaction_descriptions, card_number_generator

# Проверка маскировки карт и счетов
print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))


# Проверка даты
print(get_date("2024-03-11T02:26:18.671407"))

# Пример данных для фильтрации и сортировки
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]

print(filter_by_state(data))
print(sort_by_date(data))

# принимает на вход список словарей, представляющих транзакции
transactions = [
    {
        "operationAmount": {
            "currency": {"code": "USD"}
        },
        "description": "Перевод организации"
    },
    {
        "operationAmount": {
            "currency": {"code": "USD"}
        },
        "description": "Перевод со счета на счет"
    }
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

# Генератор, который принимает список словарей
# с транзакциями и возвращает описание каждой операции по очереди.
transactions = [
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"},
    {"description": "Перевод со счета на счет"},
    {"description": "Перевод с карты на карту"},
    {"description": "Перевод организации"},
]

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

#Генератор, который выдает номера банковских карт в формате
#XXXX XXXX XXXX XXXX, где X — цифра номера карты.

for card_number in card_number_generator(1, 5):
    print(card_number)