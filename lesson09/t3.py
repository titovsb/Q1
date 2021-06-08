'''
Worker class
'''

class Worker:
    def __init__(self, name, surname, position, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.set_income(wage, bonus)

    def set_income(self, wage, bonus):
        self._income = {'wage': wage, 'bonus': bonus}

    def get_fullname(self):  # будем наследовать отсюда
        return ' '.join([self.name, self.surname, self.position])

class Position(Worker):
    def get_fullname(self):
        return super().get_fullname()

    def get_total_income(self):
        return sum(self._income.values())

if __name__ == '__main__':

    a = Position('Иванов','Иван','директор')
    print(a.get_fullname(), a.get_total_income())
    a.set_income(10, 5)
    print(a.get_fullname(), a.get_total_income())

    b = Position('Петрова','Оксана', 'секретарь', 11, bonus=22)
    print(Position.get_fullname(b), Position.get_total_income(b))


'''
Иванов Иван директор 0
Иванов Иван директор 15
Петрова Оксана секретарь 33
'''
