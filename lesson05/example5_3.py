"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""

from time import perf_counter
from decimal import getcontext, Decimal

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = perf_counter()
f = filter(lambda x: src.count(x) == 1, src)

print(type(f), f)
print(list(f))

getcontext().prec = 3
finish = perf_counter()
print(f'{Decimal(finish) - Decimal(start)} сек')


'''
<class 'filter'> <filter object at 0x7f09b7667fa0>
[23, 1, 3, 10, 4, 11]
0.000412 сек
'''
