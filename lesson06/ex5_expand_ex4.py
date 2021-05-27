'''
Используем аргументы командной строки
'''
import sys
import argparse

HOBBY_FILE = 'hobby.csv'
USERS_FILE = 'users.csv'
RESULT_FILE = 'users_hobby.txt'


ap = argparse.ArgumentParser()
ap.add_argument('-u', '--users', required=True, help="Файл со списком пользователей")
ap.add_argument('-b', '--hobby', required=True, help="Файл со списком хобби")
ap.add_argument('-r', '--result', required=False,
                help=f"Выходной файл, по умолчанию '{RESULT_FILE}'", default=RESULT_FILE)
args = vars(ap.parse_args())

with open(args['users']) as u, open(args['hobby']) as h, open(args['result'],'w') as r:
    for user in u.readlines():
        user = user.strip()
        hobby = h.readline().strip()
        print(f'{user}: {hobby if hobby else "None"}', file=r)

with open(args['result']) as f:
    print(f.read())


'''
$python ex5_expand_ex4.py -u users.csv -b hobby.csv
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи
Даян,Моше,Шмуэлевич: None

$python ex5_expand_ex4.py -h
usage: ex5_expand_ex4.py [-h] -u USERS -b HOBBY [-r RESULT]

optional arguments:
  -h, --help            show this help message and exit
  -u USERS, --users USERS
                        Файл со списком пользователей
  -b HOBBY, --hobby HOBBY
                        Файл со списком хобби
  -r RESULT, --result RESULT
                        Выходной файл, по умолчанию 'users_hobby.txt'

'''
