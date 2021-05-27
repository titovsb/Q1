"""
generator
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

f = (el for el in src if src.count(el) == 1)

print(type(f), f)
print(list(f))


'''
<class 'generator'> <generator object <genexpr> at 0x7fba478fbdd0>
[23, 1, 3, 10, 4, 11]
'''
