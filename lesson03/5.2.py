"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из ТРЕХ случайных слов,
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
    jokes = list()
    while num and len(nouns):        # цикл по счетчику или если список не пуст
        if repeat:
            jokes.append(' '.join([random.choice(nouns),
                                   random.choice(adverbs),
                                   random.choice(adjectives)
                                ]))
        else:
            jokes.append(' '.join([nouns.pop(random.randrange(len(nouns))),
                                   adverbs.pop(random.randrange(len(adverbs))),
                                   adjectives.pop(random.randrange(len(adjectives)))
                                ]))
        num -= 1
    return jokes


print(get_jokes())
print(get_jokes(num=2))
print(get_jokes(10, repeat=False))

"""
['дом ночью зеленый']
['лес завтра утопичный', 'лес вчера утопичный']
['огонь позавчера зеленый', 'город вчера мягкий', 'дом завтра веселый', 'автомобиль ночью утопичный', 'лес сегодня яркий']
"""


