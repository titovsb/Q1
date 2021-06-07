"""
Создать класс TrafficLight (светофор):
"""

import time

class TrafficLight:
    __color = [('красный', 7), ('желтый', 2), ('зеленый', 3)]
    def running(self):
        for c, t in self.__color:
            print(f'{c}... включен на {t} секунд...')
            time.sleep(t)

'''
красный... включен на 7 секунд...
желтый... включен на 2 секунд...
зеленый... включен на 3 секунд...
'''

a = TrafficLight()
TrafficLight.running(a)
