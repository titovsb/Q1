"""
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится
нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму,
так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание:
использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех
чисел из этого списка, сумма цифр которых делится нацело на 7.
Внимание: новый список не создавать!!!

Результат работы:
19668581477
18820444868
"""

def divided_by_digit(num, digit):
    """
    Возвращаем True если сумма цифр числа num делится нацело на digit, в противном случае False
    """
    temp_list = list(map(lambda x: int(x), set(str(num))))
    if not (sum(temp_list) % digit):
        return True
    else:
        return False

START_RANGE = 1
FINISH_RANGE = 1000

# создаем список из кубов нечетных чисел
source_list = list(map(lambda x: pow(x, 3), range(START_RANGE, FINISH_RANGE, 2)))

# печатаем сумму чисел которые удовлетворяют условию функции divided_by_zero
print(sum(list(filter(lambda x: divided_by_digit(x, 7), source_list))))

# изменяем исходный список без создания нового
for ind, val in enumerate(source_list):
    source_list[ind] = source_list[ind] + 17

# печатаем сумму чисел которые удовлетворяют условию функции divided_by_zero
print(sum(list(filter(lambda x: divided_by_digit(x, 7), source_list))))
