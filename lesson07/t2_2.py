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
