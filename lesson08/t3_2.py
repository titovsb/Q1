"""
Декоратор в базе. маскировку и прочее в файле t3_1
"""

def type_logger(func):
    def logger(*args):
        print(', '.join([f'{func.__name__}({x}: {type(x)})' for x in args]))
        return func(*args)
    return logger

@type_logger
def calc_cube(*args):
    return [x**3 for x in args]

if __name__ == '__main__':
    a = calc_cube(3,4,5,6)
    print(a)
