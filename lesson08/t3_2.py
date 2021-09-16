"""
Декоратор в базе. именованные аргументы
"""

def type_logger(func):
    def logger(**kwargs):
        print(', '.join([f'{func.__name__}({k}: {v} {type(v)})' for k,v in kwargs.items()]))
        return func(**kwargs)
    return logger

@type_logger
def calc_cube(**kwargs):
    return [v**3 for _,v in kwargs.items()]

if __name__ == '__main__':
    mydict = dict(zip(['a','b','c'],[2,3,4]))
    a = calc_cube(**mydict)
    print(*a)
