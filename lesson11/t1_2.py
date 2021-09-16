'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

import re

class MyDate:


    def __init__(self, str):
        tmp = re.findall(r'(\d{2})-(\d{2})-(\d{4})', str)
        if self.is_validdate(tmp):
            self.day, self.mon, self.year = \
                    list(map(int, [i for i in tmp[0]]))
        else:
            raise ValueError('Неверный формат даты')

    def __str__(self):
        return f'Дата: {self.day:02d}/{self.mon:02d}/{self.year}'

    @classmethod
    def date_to_int(cls):
        pass

    @staticmethod
    def is_validdate(data_to_check):
        if data_to_check:
            dd, mm, _ = list(map(int, [i for i in data_to_check[0]]))
            if 0 < dd <= 31 and 0 < mm <= 12:
                return True
        return False

a = MyDate('01-04-1900')
print(a, type(a))
a = MyDate('01-44-1900')
print(a, type(a))
