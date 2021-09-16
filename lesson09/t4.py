'''
Car class
'''

class Car:
    _MAX_SPEED = 60
    def __init__(self, name, set_speed=0, color='белый', direction='север'):
        self.name, self.set_speed, self.color = name, set_speed, color
        self.direction = direction
        self.is_police = False
        self.speed = 0

    def go(self, direction=None):
        if direction:
            self.direction = direction
        self.speed = self.set_speed
        print(f'{self.name} поехала на {self.direction}...')

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась...')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} повернула на {direction}...')

    def show_speed(self):       # все же будем не показывать, а возвращать
        return ', '.join([self.name, str(self.speed)])

class TownCar(Car):
    _MSG = 'Превышение скорости.'
    def show_speed(self):
        result = super().show_speed()
        return result if self.speed < super()._MAX_SPEED else '. '.join([result, _MSG])

class SportCar(Car):
    pass

class WorkCar(Car):
    _MSG = 'Превышение скорости.'
    def show_speed(self):
        result = super().show_speed()
        return result if self.speed < super()._MAX_SPEED else '. '.join([result, self._MSG])

class PoliceCar(Car):
    _MSG2 = 'Ему можно превышать.'
    def __init__(self, name, speed=0, color='белый', direction='север'):
        super().__init__(name, speed, color, direction)
        self.is_police = True
    def show_speed(self):
        result = super().show_speed()
        return result if self.speed < super()._MAX_SPEED else '. '.join([result, self._MSG2])

if __name__ == '__main__':

    bmw = SportCar('BMW', 90, 'синий', direction='юг')
    mini = TownCar('MINI', 50, 'красный')
    solaris = WorkCar('SOLARIS', 120)
    guard = PoliceCar('POLICE', 200, direction='запад', color='спеццвет')

    # машины на дороге, но пока не едут
    print(bmw.show_speed())
    print(mini.show_speed())
    print(solaris.show_speed())
    print(guard.show_speed())

    # поехали с заданной скоростью
    SportCar.go(bmw)
    TownCar.go(mini)
    solaris.go()
    guard.go(direction='край света')    # заодно поменяли направление

    # смотрим что на спидометре
    print(bmw.show_speed())
    print(mini.show_speed())
    print(solaris.show_speed())
    print(guard.show_speed())


'''
BMW, 0
MINI, 0
SOLARIS, 0
POLICE, 0
BMW поехала на юг...
MINI поехала на север...
SOLARIS поехала на север...
POLICE поехала на край света...
BMW, 90
MINI, 50
SOLARIS, 120. Превышение скорости.
POLICE, 200. Ему можно превышать.
'''
