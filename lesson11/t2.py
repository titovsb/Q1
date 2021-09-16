'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
'''

class MyZeroDiv(Exception):
    def __init__(self, msg='Пользовательское недопустимое деление на 0'):
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.msg}'

first = 25
try:
    second = int(input(f'Введите число на которое разделить {first}: '))
    if second == 0:
        raise MyZeroDiv
    print(first / second)
except MyZeroDiv as e:
    print(e)
except ValueError as e:
    print(e)

"""
Введите число на которое разделить 25: 4
6.25
Process finished with exit code 0

Введите число на которое разделить 25: 0
Пользовательское недопустимое деление на 0
Process finished with exit code 0

Введите число на которое разделить 25: asd
invalid literal for int() with base 10: 'asd'
Process finished with exit code 0
"""
