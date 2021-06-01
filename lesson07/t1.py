'''
Создаем структуру папок
'''

import os.path

project_path = 'my_project'
paths = ['settings', 'mainapp', 'adminapp', 'authapp']

for d in paths:
    os.makedirs(os.path.join(os.curdir, project_path, d), exist_ok=True)
