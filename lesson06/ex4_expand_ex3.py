'''
Задание 3 но типа с большими данными
'''

HOBBY_FILE = 'hobby.csv'
USERS_FILE = 'users.csv'
RESULT_FILE = 'users_hobby.txt'

with open(USERS_FILE) as u, open(HOBBY_FILE) as h, open(RESULT_FILE,'w') as r:
    for user in u.readlines():
        user = user.strip()
        hobby = h.readline().strip()
        print(f'{user}: {hobby if hobby else "None"}', file=r)

'''
users_hobby.txt ->
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи
Даян,Моше,Шмуэлевич: None
'''
