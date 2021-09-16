'''
Создаем файл из 4 строчек для опытов.
'''

FILENAME = 'bakery.csv'

s = ['1111,1\n','2222,2\n','3333,3\n','4444,4\n']
with open(FILENAME, 'w') as f:
    f.writelines(s)

with open(FILENAME) as f:
    s2 = f.readline()
    while s2:
        print(s2, end='')
        s2 = f.readline()
