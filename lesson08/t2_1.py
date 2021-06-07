'''
парсим nginx_log вооружившись регулярными выражениями учитываем особые строки
'''

import re

LOG = 'nginx_logs_part'

def log_parse(src):
    re_list = [r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s',
               r'\[(.*?)\]',
               r'\"([A-Z]{3})',
               r'\s(\/[\w\/]+)',
               r'\s(\d{3})\s',
               r'\s\d{3}\s(\d+)']
    try:
        result = tuple(re.findall(x, src)[0] for x in re_list)
    except IndexError:  # шаблон для особых строк
        re_list[0] = '([0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4})\s'
        result = tuple(re.findall(x, src)[0] for x in re_list)
    return result


if __name__ == '__main__':
    with open(LOG) as f:
        count, line = 1100, f.readline()
        while line and count:
            print(log_parse(line))
            count -= 1
            line = f.readline()

