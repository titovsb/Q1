import utils

print(utils.currency_rate2('usd'))
print(utils.currency_rate2('eUr'))
print(utils.currency_rate2('rur'))  # None
print(utils.currency_rate2('Kzt'))  # nominal=100

"""
({'date': datetime.date(2021, 5, 22)}, {'charcode': 'USD'}, {'currency': Decimal('73.5803')})
({'date': datetime.date(2021, 5, 22)}, {'charcode': 'EUR'}, {'currency': Decimal('89.9446')})
None
({'date': datetime.date(2021, 5, 22)}, {'charcode': 'KZT'}, {'currency': Decimal('0.171534')})
"""
