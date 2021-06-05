"""
парсим nginx_log одним сложным regex
"""

import re

LOG = 'nginx_logs'
RE_LIST = r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b).+\[(.*?)\].+' \
          '\"([A-Z]{3})\s(\/[\S\/]+).+\s(\d{3})\s(\d+)'

with open(LOG) as f:
    count, line = 11, f.readline()
    while line and count:
        print(re.findall(RE_LIST, line)[0])
        count -= 1
        line = f.readline()
