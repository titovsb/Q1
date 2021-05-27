"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""


def mygen(s:list) -> list:
    result = []
    for el in s:
        if s.count(el) == 1 and not result.count(el):
            result.append(el)
            yield el


if __name__ == '__main__':

    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

    f = filter(lambda x: src.count(x) == 1, src)

    print(type(f), f)
    print(list(f))


'''
<class 'filter'> <filter object at 0x7f4118fb8fa0>
[23, 1, 3, 10, 4, 11]
'''
