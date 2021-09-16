'''
Cell class
'''

class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):       # возврат новой клетки
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return self.cells - other.cells
        raise ValueError('Уменьшаемое слишком мало')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __floordiv__(self, other):
        return self.cells // other

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def __mod__(self, other):
        return self.cells % other

    def __str__(self):
        return str(self.cells)

    def make_order(self, col):
        rows = self.cells // col
        result = ''
        for i in range(rows):
            result += '*'*col + '\n'
        result += '*' * (self.cells % col)
        print(result)

if __name__ == '__main__':
    print('oper a b c type(c)')
    a = Cell(18)
    b = Cell(3)
    c = a+b
    print('add', a,b,c, type(c))
    c = a-b
    print('sub', a,b,c, type(c))
    c = a/b
    print('truediv', a,b,c, type(c))
    a.make_order(6)
    a.make_order(8)
