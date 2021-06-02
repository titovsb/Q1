'''
Задание 3. Копируем структуру папок в новое место
'''

import os

SRC_FOLDER = 'my_project'
DST_FOLDER = 'templates'

dirs = os.walk(SRC_FOLDER)
for x,y,_ in dirs:
    for i in y:
        newpath = os.path.join(os.curdir, DST_FOLDER, os.sep.join(x.split(os.sep)[1:]), i)
        os.makedirs(newpath, exist_ok=True)
