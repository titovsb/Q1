"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
и возвращающую словарь, в котором ключи — первые буквы имен, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы. Например:
> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
"""

def thesaurus(*args):
    for el in args:
        print(el)

name_list = ['Сергей', 'Яна', 'Яков', 'Света', 'Петр', 'Мария']

my_thesaurus = thesaurus(*name_list)
