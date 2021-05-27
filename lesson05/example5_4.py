"""
generator
"""

from time import perf_counter
from decimal import getcontext, Decimal

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = perf_counter()
f = (el for el in src if src.count(el) == 1)

print(type(f), f)
print(list(f))

getcontext().prec = 3
finish = perf_counter()
print(f'{Decimal(finish) - Decimal(start)} сек')


'''
<class 'generator'> <generator object <genexpr> at 0x7f7410a10580>
[23, 1, 3, 10, 4, 11]
0.000182 сек
'''
