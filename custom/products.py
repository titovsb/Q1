# Задачка "Товары"
"""
Реализовать структуру "Товары" = [(idx, {key:val})]. Структура программная, данные запросить.
Вывести аналитику в виде: {key: [*val]} по каждому из key списка Товары.
"""

LIST_OF_PROPERTIES = ['название', "цена", "количество", "ед."]

# products = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 1000, 'количество': 7, 'ед': 'шт.'})
#             ]

products = []
exitcode = True

while True:
    if input('Новый продукт? (д/н): ').upper() != "Д":
        break
    my_dict = {}
    for idx in LIST_OF_PROPERTIES:
        my_dict[idx] = input(f'{idx.title()}: ')
    if len(products):
        products.append((max(x[0] for x in products)+1, my_dict))
    else:
        products.append((1, my_dict))

analytics = {}
for record in products:
    _, prod_dict = [*record]
    for key, value in prod_dict.items():
        if key in analytics.keys():
            tmp = analytics[key]
            tmp.append(value)
            analytics[key] = list(set(tmp))
        else:
            analytics[key] = [value]
print(analytics)

"""
Новый продукт? (д/н): д
название: Соль
цена: 10
количество: 100
ед.: шт.
Новый продукт? (д/н): д
название: Сахар
цена: 150
количество: 80
ед.: шт.
Новый продукт? (д/н): н
{'название': ['Соль', 'Сахар'], 'цена': ['150', '10'], 'количество': ['80', '100'], 'ед.': ['шт.']}
"""
