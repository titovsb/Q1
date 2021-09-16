'''
Задание 3 без собственного класса выглядит проще.
'''

print("Вводите числа, для завершения 'stop'")
mylist = list()
while True:
    el = input(": ")
    if el.lower() == 'stop':
        break
    try:
        mylist.append(int(el))
    except ValueError:
        print(f'Значение "{el}" не является числом')
print(mylist)
