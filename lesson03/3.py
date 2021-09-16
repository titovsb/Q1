"""
3. Написать функцию thesaurus(), возвращающую объект типа
{"И": ["Иван", "Илья"], "М": ["Мария"], "П": ["Петр"]}
"""

def thesaurus(*args):
    key_chars = sorted(set(x[0] for x in args))
    out_thesaurus = dict()
    for el in key_chars:
        out_thesaurus[el] = list(filter(lambda x : x[0] == el, args))
    return out_thesaurus

print(thesaurus('Сергей', 'Яна', 'Яков', 'Света', 'Петр', 'Мария', 'Михаил'))

"""
Отсортированный по ключам словарь:
{'М': ['Мария'], 'П': ['Петр'], 'С': ['Сергей', 'Света'], 'Я': ['Яна', 'Яков']}
"""