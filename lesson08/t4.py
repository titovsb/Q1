from functools import wraps

def valid_checker(check):
    def _valid(func):
        @wraps(func)
        def deco(num):
            if not check(num):
                raise ValueError(f'Неверное значение: {num}')
            result = func(num)
            print('WRAPPER -', type(result), result)
            return result
        return deco
    return _valid


@valid_checker(lambda x: x > 0)
def calc_cube(num):
    return num**3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube(-5))


    exit(0)
