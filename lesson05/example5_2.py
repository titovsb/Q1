"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""

from time import perf_counter
from decimal import getcontext, Decimal

def mygen(s:list) -> list:
    for el in s:
        if s.count(el) == 1:
            yield el


if __name__ == '__main__':
    start = perf_counter()
    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    g = mygen(src)
    print(type(g), g)
    print(list(g))

    getcontext().prec = 3
    finish = perf_counter()
    print(f'{Decimal(finish) - Decimal(start)} сек')



'''
<class 'generator'> <generator object mygen at 0x7fad36b4e580>
[23, 1, 3, 10, 4, 11]
0.000176 сек]
'''
