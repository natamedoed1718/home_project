from typing import Any


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """

    # пустой список для результата
    result = []

    # проходим по каждому словарю в списке
    for item in data:

        # проверяем, есть ли ключ 'state' и совпадает ли его значение
        if 'state' in item:
            if item['state'] == state:
                result.append(item)
    return result


def sort_by_date(data: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date).
    """

    return sorted(data, key=lambda item: item['date'], reverse=reverse)
