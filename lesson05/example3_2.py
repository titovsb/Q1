"""
Задача 3.
"""


def mygen(t:list, k:list) -> tuple:
    for i in range(len(t)):
        yield (t[i], None if i >= len(k) else k[i])

if __name__ == "__main__":

    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]

    a = mygen(tutors, klasses)          # учителей меньше  чем классов
    print(type(a), *a)

    a = mygen(tutors, klasses[:2])      # учителей больше, дополняем None
    print(type(a), *a)

    a = mygen(tutors[:2], klasses)      # новый генератор для ручного перебора
    print(next(a))
    print(next(a))
    print(next(a))

'''
<class 'generator'> ('Иван', '9А') ('Анастасия', '7В') ('Петр', '9Б') ('Сергей', '9В') ('Дмитрий', '8Б') ('Борис', '10А') ('Елена', '10Б')
<class 'generator'> ('Иван', '9А') ('Анастасия', '7В') ('Петр', None) ('Сергей', None) ('Дмитрий', None) ('Борис', None) ('Елена', None)
('Иван', '9А')
('Анастасия', '7В')
StopIteration
'''
