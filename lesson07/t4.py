'''
Задание 4. Собираем статистику по файлам
'''

import collections
import os

FOLDER = os.curdir

class FileStat:

    def getRange(self, size):
        r = [0, 100, 1000, 10000, 100000]
        for i in r:
            if i>=size:
                return i

    def __init__(self):
        self.stat = collections.defaultdict(int)

    def countFile(self, fileinfo):
        tmp_range = self.getRange(fileinfo)
        if tmp_range:
            self.stat[tmp_range] += 1

    def getInfo(self):
        return dict(self.stat)

fs = FileStat()
for root, dirs, files in os.walk(FOLDER):
    for file in files:
        fs.countFile(os.stat(os.path.join(root, file)).st_size)
print(fs.getInfo())

'''
Всего 9 файлов с какими-то длинами, из 20bytes маленький один и несколько файлов 0 длины.
что соответствует заданию.

{1000: 6, 10000: 2, 100: 1}
'''
