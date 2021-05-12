"""
Второй вариант задания А без использования try, def

"""


SEC_IN_MINUTE = 60
MINS_IN_HOUR = 60
SEC_IN_HOUR = SEC_IN_MINUTE*MINS_IN_HOUR
HOURS_IN_DAY = 24
SEC_IN_DAY = SEC_IN_HOUR*HOURS_IN_DAY
DAYS_IN_MONTH = 30                      # all months contain the same number of days
MONTHS_IN_YEAR = 12
SEC_IN_MONTH = SEC_IN_DAY*DAYS_IN_MONTH
DAYS_IN_YEAR = 365
SEC_IN_YEAR = SEC_IN_DAY*DAYS_IN_YEAR    # ignore a leap years


print('Для завершения программы введите "0"')
seconds = int(input('Интервал в секундах: '))
while seconds:
    tmp = seconds // SEC_IN_YEAR
    if tmp:
        print(tmp, 'лет', end=' ')
    tmp = seconds // SEC_IN_MONTH % MONTHS_IN_YEAR
    if tmp:
        print(tmp, 'месяцев', end=' ')
    tmp = seconds // SEC_IN_DAY % DAYS_IN_MONTH
    if tmp:
        print(tmp, 'дней', end=' ')
    tmp = seconds // SEC_IN_HOUR % HOURS_IN_DAY
    if tmp:
        print(tmp, 'часов', end=' ')
    tmp = seconds // SEC_IN_MINUTE % MINS_IN_HOUR
    if tmp:
        print(tmp, 'минут', end=' ')
    tmp = seconds % SEC_IN_MINUTE
    if tmp:
        print(tmp, 'секунд', end=' ')
    print('')
    seconds = int(input('Интервал в секундах: '))
