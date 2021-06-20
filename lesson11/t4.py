'''
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
'''


class Stock:
    pass


class Equipment:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight


class Printer(Equipment):
    def __init__(self, name, weight=0, mode=None):
        self.mode = mode
        super().__init__(name, weight)


class Scanner(Equipment):
    def __init__(self, name, weight=0, color=None):
        self.color = color
        super().__init__(name, weight)


class Copier(Equipment):
    def __init__(self, name, weight=None, vendor=None):
        self.vendor = vendor
        super().__init__(name, weight)


if __name__ == '__main__':
    a = Printer('LaserJet 3', 2, 'Лазерный')
    b = Scanner('EasyScan', 0.5, "Синий")
    c = Copier('HandCopy', 10, 'Canon')
    print(type(a), a, a.name, a.mode)
    print(type(b), b, b.name, b.color)
    print(type(c), c, c.name, c.vendor)
else:
    pass
