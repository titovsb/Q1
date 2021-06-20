'''
3. Создайте собственный класс-исключение, который должен проверять содержимое
списка на наличие только чисел. Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и
отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
'''

class CheckListException(Exception):
    def __init__(self, item=None, msg='Попытка добавить в список НЕ число'):
        self.msg = msg
        self.item = item
        super().__init__(self.msg)

    def __str__(self):
        return f'Аргумент "{self.item}" не является числом' if self.item else f'{self.msg}'

print("Вводите числа, для завершения 'stop'")
mylist = list()
while True:
    try:
        el = input(": ")
        if el.lower() == 'stop':
            break
        elif not el.isnumeric():
            raise CheckListException(el)
        mylist.append(int(el))
    except CheckListException as e:
        print(e)
print(mylist)
