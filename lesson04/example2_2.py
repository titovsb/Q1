"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
"""
import requests
import xml.etree.ElementTree as ET
from decimal import *


def currency_rate(cur_find:str) -> dict:
    """
    Return CBR rate for cur_str
    :param cur_find:
    :return: float
    """
    CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
    r = requests.post(CBR_URL)
    xml = ET.fromstring(r.text)
    for el in xml.iter('Valute'):
        charcode, nominal, name, value = el[1], el[2], el[3], el[4]
        if charcode.text == str.upper(cur_find):
            getcontext().prec = 6
            tmp = value.text.split(',')
            return (Decimal(tmp[0]) + Decimal(tmp[1])/10000)/ Decimal(nominal.text)
    else:
        return None


if __name__ == '__main__':
    tmp = currency_rate('USD')
    print(type(tmp), tmp)
    tmp = currency_rate('eUr')
    print(type(tmp), tmp)
    tmp = currency_rate('rur')     # None
    print(type(tmp), tmp)
    tmp = currency_rate('Kzt')     # Nominal = 100
    print(type(tmp), tmp)

"""
<class 'decimal.Decimal'> 73.5803
<class 'decimal.Decimal'> 89.9446
<class 'NoneType'> None
<class 'decimal.Decimal'> 0.171534
"""
