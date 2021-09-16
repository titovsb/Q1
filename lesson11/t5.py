"""
5. Продолжить работу над первым заданием. Разработайте методы,
которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
"""

LEN_LINE = 60


class Stock:
    errorflag = True  # выставляется в Ложь при неудачном перемещении

    def __init__(self, name="Склад"):
        self.items = dict()
        self.myname = name

    def add_item(self, item, qtty):
        self.items[item.getname] = self.items.get(item.getname, {'item': item, 'qtty': 0})
        self.items[item.getname]['qtty'] = self.items[item.getname]['qtty'] + qtty

    @property
    def get_keys(self):
        return [k for k in self.items]

    def pop_item(self, name, qtty):
        if name in self.items and self.items[name]['qtty'] >= qtty:
            item = self.items[name]['item']
            self.items[name]['qtty'] -= qtty
            if self.items[name]['qtty'] == 0:
                self.items.pop(name)  # если остаток == 0, удалить из списка
            return item
        return None  # явное лучше неявного

    def get_item_by_name(self, name):
        for k in self.items:
            if self.items[k]['item'].getname == name:
                return self.items[k]
        return None

    def __str__(self):
        tmp = f'Остатки на {self.myname}:\n'
        for idx in self.items:
            tmp += f'{self.items[idx]["item"]}, количество: {self.items[idx]["qtty"]}\n'
        return tmp

    @staticmethod
    def move_to(name, qtty, into, to):
        item = into.pop_item(name, qtty)
        if item:
            to.add_item(item, qtty)
            into.errorflag = True
        else:
            into.errorflag = False
        return into.errorflag


class Equipment:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight

    @property
    def getname(self): return self.name

    def __str__(self):
        return f'Название: {self.name}, вес {self.weight}'


class Printer(Equipment):
    def __init__(self, name="Принтер", weight=0, mode=None):
        self.mode = mode
        super().__init__(name, weight)

    def __str__(self):
        return f'{super().__str__()}, mode: {self.mode}'


class Scanner(Equipment):
    def __init__(self, name="Сканер", weight=0, color=None):
        self.color = color
        super().__init__(name, weight)

    def __str__(self):
        return f'{super().__str__()}, color: {self.color}'


class Copier(Equipment):
    def __init__(self, name="Копир", weight=None, vendor=None):
        self.vendor = vendor
        super().__init__(name, weight)

    def __str__(self):
        return f'{super().__str__()}, vendor: {self.vendor}'


if __name__ == '__main__':
    a = Printer('LaserJet 3', 2, 'Лазерный')  # завели карточки товаров
    b = Scanner('EasyScan', 0.5, "Синий")
    c = Copier('HandCopy', 10, 'Canon')
    d = Copier()

    stock = Stock()  # завели склады
    sales = Stock('Отдел продаж')

    stock.add_item(a, 10)  # приняли на склад товары
    stock.add_item(b, 4)
    stock.add_item(c, 2)
    stock.add_item(d, 1)
    print('Начальное состояние'.center(LEN_LINE, '*'))

    print(stock)
    print(sales)

    if stock.move_to('LaserJet 3', 2, stock, sales):  # перенесли с одного склада на другой
        print('Перемещение прошло успешно'.center(LEN_LINE, '+'))
    else:
        print('Неудачное перемещение'.center(LEN_LINE, '-'))

    print(stock)
    print(sales)

    if stock.move_to('EasyScan', 4, stock, sales):  # перенесли весь запас товара на другой склад
        print('Перемещение прошло успешно'.center(LEN_LINE, '+'))
    else:
        print('Неудачное перемещение'.center(LEN_LINE, '-'))

    print(stock)
    print(sales)

    if stock.move_to('Копир', 10, stock, sales):  # пробуем перенести больше чем есть на складе
        print('Перемещение прошло успешно'.center(LEN_LINE, '+'))
    else:
        print('Неудачное перемещение'.center(LEN_LINE, '-'))

    print(stock)
    print(sales)
else:
    pass
