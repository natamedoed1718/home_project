from typing import Any, Dict, List

from src.data_loader import load_transactions_from_csv
from src.data_loader import load_transactions_from_csv as load_other
from src.data_loader import load_transactions_from_xlsx
from src.decorators import log
from src.external_api import convert_to_rub
from src.filters import process_bank_operations, process_bank_search
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number, mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

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

# Функция, которая принимает на вход путь до JSON-файла
# и возвращает список словарей с данными о финансовых транзакциях.

transactions = load_transactions("..data/operations.json")

print(transactions)

# Функция, которая принимает на вход транзакцию и возвращает сумму транзакции

transaction = {"operationAmount": {"amount": "10", "currency": {"code": "USD"}}}

result = convert_to_rub(transaction)

print(result)

# принимает на вход список словарей, представляющих транзакции
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
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

# Генератор, который выдает номера банковских карт в формате
# XXXX XXXX XXXX XXXX, где X — цифра номера карты.

for card_number in card_number_generator(1, 5):
    print(card_number)


# пример использования декораторов
@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Сложение чисел"""
    return x + y


result = my_function(1, 2)
print(result)


@log(filename="mylog.txt")  # пример с ошибкой
def divide(a: float, b: float) -> float:
    """Деление числа"""
    return a / b


divide(1, 0)

# logging

load_transactions("data/operations.json")
mask_card_number("1234567812345678")

# cvs

csv_data = load_transactions_from_csv("data/transactions.csv")
print("CSV:", csv_data)

xlsx_data = load_transactions_from_xlsx("data/transactions_excel.xlsx")
print("XLSX:", xlsx_data)


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    print("Выберите пункт:")
    print("1. JSON")
    print("2. CSV")
    print("3. XLSX")

    choice = input("Введите номер: ")

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        data = load_transactions("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        data = load_other("data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        data = load_other("data/transactions_excel.xlsx")
    elif choice == "4":
        print("Подсчет операций по категориям")

        data = load_transactions("data/operations.json")

        categories_input = input("Введите категории через запятую (например: Перевод, Открытие вклада): ")

        categories = [cat.strip() for cat in categories_input.split(",")]

        result = process_bank_operations(data, categories)

        print("\nРезультат:")
        for category, count in result.items():
            print(f"{category}: {count}")

    else:
        print("Неверный выбор")
        return

    # Фильтр по статусу
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").upper()

        if status in valid_statuses:
            break

        print(f'Статус операции "{status}" недоступен.')

    filtered: List[Dict[str, Any]] = [item for item in data if item.get("state", "").upper() == status]

    print(f'Операции отфильтрованы по статусу "{status}"')

    # Сортировка

    sort_choice = input("Отсортировать по дате? Да/Нет: ").lower()

    if sort_choice == "да":
        order = input("По возрастанию или по убыванию?: ").lower()

        reverse = order == "по убыванию"

        filtered.sort(key=lambda x: x.get("date", ""), reverse=reverse)

    # Только рубли
    rub_only = input("Только рубли? Да/Нет: ").lower()

    if rub_only == "да":
        filtered = [
            item for item in filtered if item.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    # Поиск

    search_choice = input("Фильтр по слову в описании? Да/Нет: ").lower()

    if search_choice == "да":
        word = input("Введите слово: ")
        filtered = process_bank_search(filtered, word)

    # Вывод

    if not filtered:
        print("Не найдено ни одной транзакции")
        return

    print(f"Всего операций: {len(filtered)}\n")

    for item in filtered:
        print(item.get("date", ""), item.get("description", ""))
        print("Сумма:", item.get("operationAmount", {}).get("amount"))
        print()


if __name__ == "__main__":
    main()
