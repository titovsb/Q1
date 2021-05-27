"""
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать
кроме курса дату, которая передаётся в ответе сервера.
Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
какой тип данных лучше использовать в ответе функции?
"""
import requests
import xml.etree.ElementTree as ET
from decimal import *
import datetime


def currency_rate2(cur_find:str) -> None:
    """
    Return CBR rate for cur_str
    :param cur_find:
    :return: float
    """
    CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
    r = requests.post(CBR_URL)
    xml = ET.fromstring(r.text)
    for el in xml.iter('Valute'):
        charcode, nominal, value = el[1].text, el[2].text, el[4].text
        if charcode == str.upper(cur_find):
            dd = xml.get(xml.keys()[0])
            getcontext().prec = 6
            tmp = value.split(',')
            return {'date': datetime.date(*map(int, '22.05.2021'.split('.')[::-1]))},\
                   {'charcode': charcode},\
                   {'currency': (Decimal(tmp[0]) + Decimal(tmp[1])/10000)/ Decimal(nominal)}
    else:
        return None


if __name__ == '__main__':
    tmp = currency_rate2('USD')
    print(type(tmp), tmp)
    tmp = currency_rate2('eUr')
    print(type(tmp), tmp)
    tmp = currency_rate2('rur')     # None
    print(type(tmp), tmp)
    tmp = currency_rate2('Kzt')     # Nominal = 100
    print(type(tmp), tmp)

"""
<class 'tuple'> ({'date': datetime.date(2021, 5, 22)}, {'charcode': 'USD'}, {'currency': Decimal('73.5803')})
<class 'tuple'> ({'date': datetime.date(2021, 5, 22)}, {'charcode': 'EUR'}, {'currency': Decimal('89.9446')})
<class 'NoneType'> None
<class 'tuple'> ({'date': datetime.date(2021, 5, 22)}, {'charcode': 'KZT'}, {'currency': Decimal('0.171534')})
"""




