'''
Словарь из двух файлов
'''

from itertools import zip_longest
from pprint import pprint
import json

HOBBY_FILE = 'hobby.csv'
USERS_FILE = 'users.csv'
RESULT_FILE = 'hobby_result.json'

with open(USERS_FILE) as u, open(HOBBY_FILE) as h:
    users = map(lambda s: ' '.join(s.strip().split(',')), u.readlines())
    hobby = map(str.strip, h.readlines())
    result = {k: v for k, v in zip_longest(users, hobby, fillvalue=None)}

print('Объединили два файла:')
pprint(result, indent=2)

with open(RESULT_FILE, 'w') as f:
    json.dump(result, f)

print(f"\nСчитали из файла '{RESULT_FILE}':")
with open(RESULT_FILE) as file:
    print(json.load(file))


'''
Объединили два файла:
{ 'Даян Моше Шмуэлевич': None,
  'Иванов Иван Иванович': 'скалолазание,охота',
  'Петров Петр Петрович': 'горные лыжи'}

Считали из файла 'hobby_result.json':
{'Иванов Иван Иванович': 'скалолазание,охота', 'Петров Петр Петрович': 'горные лыжи',
 'Даян Моше Шмуэлевич': None}
'''
