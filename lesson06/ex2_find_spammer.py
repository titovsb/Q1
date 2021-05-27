'''
ищем спаммера
'''

FILENAME = 'nginx_logs'

with open(FILENAME) as f:
    ips = {}
    for line in f:
        ip = line.split(' ')[0]
        ips.setdefault(ip, 0)
        ips[ip] += 1
    motivator = max(ips, key=ips.get)
    print(motivator, ips[motivator])

'''
216.46.173.126 2350
'''
