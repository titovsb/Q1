'''
BAKERY. В примере предполагается, что данные вводятся корректно.
'''

import sys

FILENAME = 'bakery.csv'

with open(FILENAME, 'r', encoding="utf-8") as f:
    if len(sys.argv) == 1:
        for i in f.readlines():
            print(i.strip())
    elif len(sys.argv) == 2:
        for idx, i in enumerate(f.readlines()):
            if idx > int(sys.argv[1])-2:
                print(i.strip())
    elif len(sys.argv) == 3:
        for idx, i in enumerate(f.readlines()):
            if idx > int(sys.argv[1])-2 and idx < int(sys.argv[2]):
                print(i.strip())
