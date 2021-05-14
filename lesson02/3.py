"""
ВАРИАНТ РЕШЕНИЯ in place

Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
"""

def translate_digit(dig):
    if dig.isdigit():
        return f'"{dig:0>2}"'
    elif dig[0] =='+':
        return f'"+{dig[1:]:0>2}"'
    else:
        return dig

source_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(source_list)

idx = len(source_list) - 1
while idx >= 0:
    source_list[idx] = translate_digit(source_list[idx])
    idx -= 1

print(source_list)
print(' '.join(source_list))

