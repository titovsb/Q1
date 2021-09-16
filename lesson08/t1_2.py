'''
Валидация email без сплит
'''

import re


def email_parse(email):
    result = re.findall(r'([\w*\.]+)@([\w*]+\.[\w*\.]+)', email)
    if result:
        return dict(zip(['username','domain'], list(result[0])))
    raise ValueError(f'Неверный адрес {email}')


if __name__ == '__main__':
    print(email_parse('hostmaster@mail.ru'))
    print(email_parse('titov@atmosfera.msk.ru'))
    print(email_parse('mail.user@domain.com.ru.local'))
    print(email_parse('Upper1@Email2Domain.local'))
    print(email_parse('Tom.Cruz@aol.net.local'))
    print(email_parse('mail@domain'))
    print(email_parse('noemail'))
    print(email_parse('123@'))
    print(email_parse('@123'))
