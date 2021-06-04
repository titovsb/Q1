'''
Валидация email

Использование:
> from lesson08.t1 import email_parse
> email_parse('any@dimain.zone')
'''

import re


def email_parse(email):
    regexp = re.compile(r'[\w*\.]+@[\w*]+\.[\w*\.]+')
    result = regexp.match(email)
    if result:
        return dict(zip(['username','domain'], result.group().split('@')))
    raise ValueError(f'Неверный адрес {email}')


if __name__ == '__main__':
    print(email_parse('hostmaster@mail.ru'))
    print(email_parse('titov@atmosfera.msk.ru'))
    print(email_parse('mail.user@domain.com.ru.local'))
    print(email_parse('Upper1@Email2Domain.local'))
    print(email_parse('mail@domain'))
    print(email_parse('noemail'))
    print(email_parse('123@'))
    print(email_parse('@123'))
