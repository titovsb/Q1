'''
Дорога
'''

from pprint import pprint

class Road:
    __massa = 1.5      # 1500 т/куб.м.

    def __init__(self, length=0, width=0, tickness=0.05):
        self._len = length
        self._wid = width
        self._tick = tickness

    def get_volume(self):
        return self._len*self._wid*self._tick*self.__massa

    def get_param(self):
        k = [('length','m'), ('width','m'), ('tickness','m'), ('massa','t'), ('volume','m3')]
        v = [self._len, self._wid, self._tick, self.__massa, self.get_volume()]
        return {k[0]: (v, k[1]) for k, v in zip(k, v)}


if __name__ == '__main__':
    a = Road()
    pprint(a.get_param(), indent=2)
    b = Road(100, width=6)
    pprint(Road.get_param(b), indent=2)


'''
{ 'length': (0, 'm'),
  'massa': (1.5, 't'),
  'tickness': (0.05, 'm'),
  'volume': (0.0, 'm3'),
  'width': (0, 'm')}
  
{ 'length': (100, 'm'),
  'massa': (1.5, 't'),
  'tickness': (0.05, 'm'),
  'volume': (45.0, 'm3'),
  'width': (6, 'm')}
'''
