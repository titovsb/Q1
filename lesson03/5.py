"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов,
НЕ ВИЖУ ЦЕЛЕСООБРАЗНЫМ ДЕЛАТЬ ФУНКЦИИ ОСУЩЕСТВЛЯЮШИЕ САМОСТОЯТЕЛЬНЫЙ ВЫВОД НА ЭКРАН В ВИДЕ СПИСКА,
И ВОЗВРАЩАЮЩИЕ None. ПОЭТОМУ ВСЕ РЕАЛИЗАЦИИ ФУНКЦИЙ ВОЗВРАЩАЮТ ЗНАЧЕНИЕ В ПЕРЕМЕННУЮ.
"""

import random


def get_jokes(num=1, repeat=True) -> list:
    """
    Возвращает num шуток из 3 списков слов. Исключает повторы, если repeat=False
    :param num: int
    :param repeat: bool
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    idx = num
    jokes = list()
    while idx and len(nouns):        # цикл по счетчику или если список не пуст
        cur_noun = random.choice(nouns)
        cur_adv = random.choice(adverbs)
        cur_adj = random.choice(adjectives)
        jokes.append(' '.join([cur_noun, cur_adv, cur_adj]))
        if not repeat:
            nouns.remove(cur_noun)
            adverbs.remove(cur_adv)
            adjectives.remove(cur_adj)
        idx -= 1
    return jokes


print(get_jokes())
print(get_jokes(num=2))
print(get_jokes(10, repeat=False))

"""
['автомобиль вчера мягкий']
['город сегодня утопичный', 'лес сегодня веселый']
['автомобиль сегодня зеленый', 'лес позавчера утопичный', 'дом вчера яркий', 'огонь завтра веселый', 'город ночью мягкий']
"""


