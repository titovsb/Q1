'''
парсим файл своего дикого формата
'''

from pprint import pprint
import os

settings = {}
with open('config1.yaml') as f:
    lines = dict(map(str.split, f.readlines()))

basedir = lines.pop('base')
for k, v in lines.items():
    os.makedirs(os.path.join(os.curdir, basedir, k), exist_ok=True)
    print(f'Создан каталог: {k}')
    for i in v.split(','):
        with open(os.path.join(os.curdir, basedir, k, i), "w") as f:
            print(f'Создан файл: {i} в каталоге {k}')

'''
Создан каталог: settings
Создан файл: __init__.py в каталоге settings
Создан файл: dev.py в каталоге settings
Создан файл: prod.py в каталоге settings
Создан каталог: mainapp
Создан файл: __init__.py в каталоге mainapp
Создан файл: models.py в каталоге mainapp
Создан файл: views.py в каталоге mainapp
Создан каталог: mainapp/templates/mainapp
Создан файл: base.html в каталоге mainapp/templates/mainapp
Создан файл: index.html в каталоге mainapp/templates/mainapp
Создан каталог: authapp
Создан файл: __init__.py в каталоге authapp
Создан файл: models.py в каталоге authapp
Создан файл: views.py в каталоге authapp
Создан каталог: authapp/templates/authapp
Создан файл: base.html в каталоге authapp/templates/authapp
Создан файл: index.html в каталоге authapp/templates/authapp
'''



