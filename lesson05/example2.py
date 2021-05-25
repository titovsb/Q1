'''
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
не используя ключевое слово yield.
'''

if __name__ == '__main__':

    MAX_NUM = 5

    myiter = (i for i in range(1, MAX_NUM+1, 2))
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
