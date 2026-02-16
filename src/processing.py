def filter_by_state(data, state="EXECUTED"):
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
       state соответствует указанному значению.
    """

    # пустой список для результата
    result=[]

    # проходим по каждому словарю в списке
    for item in data:

        # проверяем, есть ли ключ 'state' и совпадает ли его значение
        if 'state' in item:
            if item['state'] == state:
                result.append(item)
    return result













def sort_by_date():
 pass