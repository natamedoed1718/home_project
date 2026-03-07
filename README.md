# Личный кабинет - виджет последних операций
Проект предназначен для отображения последних успешных банковских операций клиента в личном кабинете. Он подготавливает и форматирует данные на бэкенде для удобного отображения в виджете.

## Содержание 
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Тестирование](#тестирование) 
- [Deploy и CI/CD](#deploy-и-ci/cd) 
- [Contributing](#contributing) 
- [To do](#to-do) 
- [Команда проекта](#команда-проекта)

## Технологии
- [GatsbyJS](https://www.gatsbyjs.com/)
- [TypeScript](https://www.typescriptlang.org/)
- ...

## Использование
Проект предоставляет функции для работы с банковскими операциями:
- filter_by_state(data, state='EXECUTED') — фильтрует операции по статусу.

- sort_by_date(data, reverse=True) — сортирует операции по дате.

- mask_account_card(value) — маскирует номера карт и счетов.

- get_date(value) — форматирует дату для отображения.

Пример использования:

```
def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """

    result = []

    for item in data:

        # проверяем, есть ли ключ 'state' и совпадает ли его значение
        if 'state' in item:
            if item['state'] == state:
                result.append(item)
    return result
```
## Разработка

### Требования
Для установки и запуска проекта, необходим [NodeJS](https://nodejs.org/) v8+.

### Установка зависимостей
Для установки зависимостей, выполните команду:
```sh
$ npm i
```
## Тестирование
Какие инструменты тестирования использованы в проекте и как их запускать. Например:

Мой проект покрыт юнит-тестами. Для их запуска выполните команду:
```
pytest tests
```
## Модуль генераторов (`src/generators.py`)

В этом модуле реализованы три полезных генератора для работы с транзакциями и номерами банковских карт:

1. `filter_by_currency(transactions, currency_code)` — фильтрует транзакции по валюте.
2. `transaction_descriptions(transactions)` — возвращает описание каждой транзакции.
3. `card_number_generator(start, end)` — генерирует номера банковских карт в формате `XXXX XXXX XXXX XXXX`.

### filter_by_currency
Фильтрует транзакции по валюте.

**Сигнатура:**

```python
filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator[dict]

Пример использования:

from src.generators import transaction_descriptions

transactions = [
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"}
]

descriptions = transaction_descriptions(transactions)
for d in descriptions:
    print(d)
    
Вывод:

Перевод организации
