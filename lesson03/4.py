"""
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": "Петр Алексеев"
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Сможете ли вы вернуть отсортированный по ключам словарь?
"""


def thesaurus_adv(*args) -> dict:
    key_surname = sorted(set(x.split(' ')[1][0] for x in args))
    out_thesaurus = dict()
    for sur_id in key_surname:
        out_thesaurus[sur_id] = list(filter(lambda x : x.split(' ')[1][0] == sur_id, args))
        key_name = sorted(set(x[0] for x in out_thesaurus[sur_id]))
        name_thesaurus = dict()
        for name_id in key_name:
            name_thesaurus[name_id] = list(filter(lambda x : x[0] == name_id, out_thesaurus[sur_id]))
        out_thesaurus[sur_id] = name_thesaurus
    return out_thesaurus


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

"""
{   'А': {'П': ['Петр Алексеев']}, 
    'И': {'И': ['Илья Иванов']}, 
    'С': {'А': ['Анна Савельева'], 'И': ['Иван Сергеев', 'Инна Серова']}}
"""
