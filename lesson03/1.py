"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c
английского на русский язык.
"""

def num_translate(num: str) -> str:
    """Возвращает переод цифры от 'one' до 'ten' или None"""
    LATTORUS_DICT = {
    'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
    'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять',
    'ten': 'десять',
    }
    if num in LATTORUS_DICT:
        return LATTORUS_DICT[num]

print('Для окончания работы введите Enter')
while True:
    s = input('Число прописью: ')
    if s == '': break
    print(num_translate(s))
