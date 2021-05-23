import sys

import utils

if __name__ == '__main__':
    if len(sys.argv) > 1:
        tmp = utils.currency_rate2(sys.argv[1])
        if tmp == None:
            print(tmp)
        else:
            print('{}, {}'.format(tmp['currency'], tmp['date']))
    else:
        print('Укажите обозначение валюты в командной строке')


"""
(venv)
└──╼ $python example5.py usd
73.5803, 2021-05-22
(venv)
└──╼ $python example5.py kzT
0.171534, 2021-05-22

"""
