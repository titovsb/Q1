'''
Берем из строки и записываем в файл
'''
import sys

FILENAME = 'bakery.csv'

if len(sys.argv) == 2:
    with open(FILENAME, 'a', encoding="utf-8") as f:
        print(sys.argv[1], file=f)
else:
    print('Введите значение в командной строке.')

