"""
Второй вариант задачи 2 без использования магии и функций.
"""

START_RANGE = 1
FINISH_RANGE = 1000

# создаем список кубов чисел
source_list = list(range(START_RANGE, FINISH_RANGE, 2))

firstsum = 0
secondsum = 0
for i in range(len(source_list)):

        # находим сумму цифр текущего элемента исходного списка
        sums = 0
        digit = str(pow(source_list[i], 3))
        for s in digit:
            sums = sums + int(s)
        # если сумма делится без остатка на 7, то накапливаем
        if not (sums % 7):
            firstsum += int(digit)

        # находим сумму цифр текущего элемента списка увеличенного на 17
        sums = 0
        digit = str(pow(source_list[i], 3)+17)
        for s in digit:
            sums = sums + int(s)

        # если сумма делится без остатка на 7, то накапливаем во второе место
        if not (sums % 7):
            secondsum += int(digit)

print(firstsum)
print(secondsum)
