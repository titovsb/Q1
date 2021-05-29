'''
парсим nginx_logs
'''

from pprint import pprint

FILENAME = 'nginx_logs'

with open(FILENAME) as f:
    result = []
    for line in f:
        log = line.split(' ')
        result.append((log[0], log[5].strip('"'), log[6]))
print(len(result), result[:2])


'''
51462 [('93.180.71.3', 'GET', '/downloads/product_1'), ('93.180.71.3', 'GET', '/downloads/product_1')]
'''
