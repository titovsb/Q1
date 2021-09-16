'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение
созданных экземпляров. Проверьте корректность полученного результата.
'''

class Complex:

    def __init__(self, Re, Im):
        self.Re, self.Im = Re, Im

    def __add__(self, other):
        return Complex(self.Re + other.Re, self.Im + other.Im)

    def __mul__(self, other):
        return Complex(self.Re*other.Re + self.Im*other.Im * (-1),
                       self.Re*other.Im + self.Im*other.Re)

    def __str__(self):
        return f'{self.Re}+{self.Im}i'


one = Complex(2, 2)
two = Complex(1, 2)
print(f'{one} + {two} = {one+two}')
three = one*two
print(f'{one} * {two} = {three}')
two *= one
print('Второй способ: ', two)
