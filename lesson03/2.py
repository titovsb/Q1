"""
Доработать предыдущую функцию num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы.
"""

def num_translate(num: str) -> str:
    """Возвращает переод цифры от 'one' до 'ten' или None"""
    LATTORUS_DICT = {
    'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
    'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять',
    }
    tmp = num.lower()
    if tmp in LATTORUS_DICT:
        return LATTORUS_DICT[tmp] if num in LATTORUS_DICT else LATTORUS_DICT[tmp].capitalize()

print('Для окончания работы введите "0"')
while True:
    s = input('Число прописью: ')
    if s == '0': break
    print(num_translate(s))
