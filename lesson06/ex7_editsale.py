'''
Читаем и изменяем файл. Для создания нового исходника запустите bakery_create.py
'''

import argparse


def substitute_val(newval:str, oldval:str) -> str:
    if not (len(newval) > len(oldval)):
        return f'{newval!s:>{len(oldval)}}'
    else:
        return ''


ap = argparse.ArgumentParser()
ap.add_argument('-n', '--number', required=True, help="Номер строки")
ap.add_argument('-v', '--value', required=True, help="Новое значение")
args = vars(ap.parse_args())

FILENAME = 'bakery.csv'

with open(FILENAME, 'r+') as f:
    pos, el, idx = f.tell(), f.readline(), 1    # последовательность важна!!
    while el:
        if idx == int(args['number']):
            tmp = substitute_val(args["value"], el.strip())
            if tmp:
                f.seek(pos)
                f.write(tmp+'\n')
                print('Successful.')
                break
            else:
                print('New value too long.')
                break
        idx += 1
        pos = f.tell()
        el = f.readline()

'''
содержимое backery.csv:
1111,1
2222,2
3333,3
4444,4

$python ex7_editsale.py -n 3 -v 2.2
Successful.
1111,1
2222,2
   2.2
4444,4

$python ex7_editsale.py -n 1 -v aaaaaa
Successful.
aaaaaa
2222,2
   2.2
4444,4

$python ex7_editsale.py -n 2 -v 1234567890
New value too long.
'''
