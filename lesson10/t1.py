'''
Matrix class
'''

import numpy

class Matrix:
    def __init__(self, m1):
        self.m1 = m1

    @property
    def _shape(self):
        return numpy.shape(self.m1)

    @property
    def rows(self): return self._shape[0]

    @property
    def cols(self): return self._shape[1]

    def __add__(self, other):
        if  self._shape == other._shape:
            z = Matrix(self.m1)         # создаем новый объект, который затем возвращаем
            for row in range(self.rows):
                for col in range(self.cols):
                    z.m1[row][col] += other.m1[row][col]
        else:
            raise IndexError('Матрицы должны быть одноразмерны.')
        return z

    def __str__(self):
        result = ''
        for row in range(self.rows):
            result += ' '.join(map(str, self.m1[row])) + '\n'
        return result


if __name__ == '__main__':

    print('матрица 3х3')
    a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    print(a)
    print(b)
    a += b
    print(a)

    print('матрица 2х3')
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Matrix([[1, 1, 1], [1, 1, 1]])
    print(a)
    print(b)
    a += b
    print(a)

    print('матрица 3х2')
    a = Matrix([[1, 2], [3, 4], [5, 6]])
    b = Matrix([[1, 1], [1, 1], [1, 1]])
    print(a)
    print(b)
    a += b
    print(a)
