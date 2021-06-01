'''
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
'''


def odd_nums(num:int) -> int:
    for i in range(1, num+1, 2):
        yield i


if __name__ == '__main__':

    myiter = odd_nums(5)
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))     # StopIteration


'''
1
3
5
StopIteration
'''
