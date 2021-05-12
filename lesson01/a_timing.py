"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.

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


def format_seconds(seconds):
    time_dict = {}
    time_dict['years'] = seconds // SEC_IN_YEAR
    time_dict['months'] = seconds // SEC_IN_MONTH % MONTHS_IN_YEAR
    time_dict['days'] = seconds // SEC_IN_DAY % DAYS_IN_MONTH
    time_dict['hours'] = seconds // SEC_IN_HOUR % HOURS_IN_DAY
    time_dict['minutes'] = seconds // SEC_IN_MINUTE % MINS_IN_HOUR
    time_dict['seconds'] = seconds % SEC_IN_MINUTE
    return time_dict

def get_seconds():
    try:
        seconds = int(input('Seconds: '))
    except ValueError:
        print("Finish...")
        return 0
    else:
        return seconds

def print_time_intervals(time_d):
    for key, val in time_d.items():
        if val:
            print(f'{val} {key}', end=' ')
    print('')


print('To finish program simply press Enter key.')
seconds = get_seconds()
while int(seconds):
    print_time_intervals(format_seconds(seconds))
    seconds = get_seconds()

