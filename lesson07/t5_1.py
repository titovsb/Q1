'''
Задание 4. Собираем статистику по файлам + расширениям
'''

import json
import os

FOLDER = os.curdir

class FileStat:

    def getRange(self, size):
        r = [0, 100, 1000, 10000, 100000]
        for i in r:
            if i >= size:
                return i

    def __init__(self):
        self.stat = dict()

    def countFile(self, fileinfo, filename):
        tmp = self.getRange(fileinfo)
        self.stat.setdefault(tmp, (0,[]))
        if tmp:
            self.stat[tmp] = (self.stat[tmp][0]+1, list(set(self.stat[tmp][1]+[filename])))

    def getInfo(self):
        if 0 in self.stat:
            self.stat.pop(0)
        return self.stat

fs = FileStat()
for root, dirs, files in os.walk(FOLDER):
    for file in files:
        fs.countFile(os.stat(os.path.join(root, file)).st_size, os.path.splitext(file)[1])

name = os.path.split(os.getcwd())[1]+'_summary.json'
with open(name, 'w') as f:
    f.writelines(json.dumps(fs.getInfo()))

with open(name) as f:
    obj2 = json.loads(f.readline())
print(obj2)

'''
с костылями конкретными конечно....((
{'1000': [6, ['.yaml', '.py']], '10000': [3, ['.py']], '100': [2, ['', '.json']]}
'''
