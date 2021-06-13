'''
Второй вариант: абстрактный класс, наследники, @properties, @method.setter
'''

from abc import ABC, abstractmethod

class Clothes(ABC):

    @property
    @abstractmethod
    def volume(self):
        pass

    @property
    @abstractmethod
    def main_prop(self):
        pass

    @main_prop.setter
    @abstractmethod
    def main_prop(self, value):
        pass


class Suit(Clothes):        # Костюм
    def __init__(self, xH=0, name='Костюм'):
        self.__H = xH
        self.name = name
    @property
    def volume(self):
        return round(2*self.__H + 0.3, 2)

    @property
    def main_prop(self):
        return self.__H

    @main_prop.setter
    def main_prop(self, value):
        if isinstance(value, int) and value > 0:
            self.__H = value
        else:
            raise ValueError('Значение должно быть целым и больше 0')

class Coat(Clothes):        # Пальто
    def __init__(self, xV, name='Пальто'):
        self.__V = xV
        self.name = name
    @property
    def volume(self):
        return round(self.__V/6.5 + 0.5, 2)

    @property
    def main_prop(self):
        return self.__V

    @main_prop.setter
    def main_prop(self, value):
        if isinstance(value, int) and value > 0:
            self.__V = value
        else:
            raise ValueError('Значение должно быть целым и больше 0')


kostume = Suit(1)
palto = Coat(1, name='Пальтище')
print(f'На один {kostume.name} {kostume.volume}, на одно {palto.name} {palto.volume}')

palto.main_prop = 3
print(f'На {palto.name} {palto.main_prop} свойства {palto.volume}')

palto.main_prop = -2
print(f'На {palto.name} {palto.main_prop} свойства {palto.volume}')



