# Задачка "Товары"
"""
Реализовать структуру "Товары" = [(idx, {key:val})]. Структура программная, данные запросить.
Вывести аналитику в виде: {key: [*val]} по каждому из key списка Товары.
"""

LIST_OF_PROPERTIES = ['название', "цена", "количество", "ед."]

products = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 1000, 'количество': 7, 'ед': 'шт.'})
            ]

def fill_input():
    pass

def parse_product(k, v, analytics_list):
    if k in analytics_list.keys():
        tmp = analytics_list[k]
        tmp.append(v)
        analytics_list[k] = list(set(tmp))
    else:
        analytics_list[k] = [v]
    return analytics_list


analytics = {}
for record in products:
    _, record = [*record]
    for key, value in record.items():
        parse_product(key, value, analytics)

print(analytics)
