from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(card_or_account: str)-> str:
    """
    Функция принимает строку с типом и номером карты или счета
    и возвращает строку с замаскированным номером
    """

    # номер в строке всегда последний
    number = card_or_account.split() [-1]
    # т.к. между названием и номером есть пробел, то +1
    # с конца считаем количество символов номера и дальше текст
    name = card_or_account[:-(len(number) +1)]

    if "Счет" in card_or_account:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"

def get_date(date_str:str)->str:
    """
    Функция, которая принимает на вход строку
    с датой в одном формате
    и возвращает в другом формате
    """

    # берем первые 10 символов
    date_part = date_str[:10]

    # разделяем на год, месяц, день
    year, month, day = date_part.split("-")

    # собираем в нужном формате
    return f"{day}.{month}.{year}"




