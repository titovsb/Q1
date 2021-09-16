import yaml
import os.path
from pprint import pprint

def my_walk(home='', **kwargs):
    for k, v in kwargs.items():
        home = os.path.join(home, '' if home else k) # учитываем начало перебора
        print('Создали каталог', home)
        os.makedirs(home, exist_ok=True)
        for i in v:
            if isinstance(i, dict):
                path = os.path.join(home, list(i.keys())[0])
                my_walk(path,**i)
            else:
                with open(os.path.join(home, i), "w") as f:
                    print(f'Новый файл: {i} в каталоге {home}')


with open('config.yaml') as f:
    lines = yaml.safe_load(f)

my_walk(**lines)

'''
Создали каталог my_project
Создали каталог my_project/settings/
Новый файл: __init__.py в каталоге my_project/settings/
Новый файл: dev.py в каталоге my_project/settings/
Новый файл: prod.py в каталоге my_project/settings/
Создали каталог my_project/mainapp/
Новый файл: __init__.py в каталоге my_project/mainapp/
Новый файл: models.py в каталоге my_project/mainapp/
Новый файл: views.py в каталоге my_project/mainapp/
Создали каталог my_project/mainapp/templates/
Создали каталог my_project/mainapp/templates/mainapp/
Новый файл: base.html в каталоге my_project/mainapp/templates/mainapp/
Новый файл: index.html в каталоге my_project/mainapp/templates/mainapp/
Создали каталог my_project/authapp/
Новый файл: __init__.py в каталоге my_project/authapp/
Новый файл: models.py в каталоге my_project/authapp/
Новый файл: views.py в каталоге my_project/authapp/
Создали каталог my_project/authapp/templates/
Создали каталог my_project/authapp/templates/authapp/
Новый файл: base.html в каталоге my_project/authapp/templates/authapp/
Новый файл: index.html в каталоге my_project/authapp/templates/authapp/
'''