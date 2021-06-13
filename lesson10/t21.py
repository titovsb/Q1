'''
class Clothes as abstract
'''

from abc import ABC, abstractmethod

class Clothes(ABC):

    @property
    @abstractmethod
    def volume(self):
        pass


class Suit(Clothes):        # Костюм
    def __init__(self, xH=0, name='Костюм'):
        self.__H = xH
        self.name = name

    @property
    def volume(self):
        return round(2*self.__H + 0.3, 2)


class Coat(Clothes):        # Пальто
    def __init__(self, xV=0, name='Пальто'):
        self.__V = xV
        self.name = name

    @property
    def volume(self):
        return round(self.__V/6.5 + 0.5, 2)


kostume = Suit(1)
palto = Coat(1, name="Пальтище")

print(f'На один {kostume.name} {kostume.volume}, на одно {palto.name} {palto.volume}')
