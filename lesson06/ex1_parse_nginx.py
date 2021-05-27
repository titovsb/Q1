'''
парсим nginx_logs
'''

from pprint import pprint

FILENAME = 'nginx_logs'

with open(FILENAME) as f:
    result = []
    for idx, line in enumerate(f):
        if idx<5:
            log = line.split(' ')
            result.append((log[0], log[5].strip('"'), log[6]))
        else:
            break
    pprint(result, indent=2)


'''
[ ('93.180.71.3', 'GET', '/downloads/product_1'),
  ('93.180.71.3', 'GET', '/downloads/product_1'),
  ('80.91.33.133', 'GET', '/downloads/product_1'),
  ('217.168.17.5', 'GET', '/downloads/product_1'),
  ('217.168.17.5', 'GET', '/downloads/product_2')]
'''
