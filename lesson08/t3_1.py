"""
Декоратор со всеми возможностями
"""

from functools import wraps

def logger(v=0):
    def type_logger(func):

        @wraps(func)                # маскировка
        def logger(*args):
            result = func(*args)
            print(', '.join([f'{func.__name__}({x}: {type(x)})' for x in args]))
            if v == 1:
                print(type(result), result)
            return result
        return logger
    return type_logger

@logger(v=1)    # можно попробовать v=1
def calc_cube(*args):
    return [x**3 for x in args]

if __name__ == '__main__':
    a = calc_cube(3,4,5,6)
    print(a)
