"""
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.

Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(),
  sha1() или любой другой из модуля hashlib задача считается не решённой.
"""

import hashlib


def substring_count(string: str) -> int:
    result = 0
    h_space = hashlib.sha1(' '.encode('utf-8')).hexdigest()

    for len_sub in range(1, len(string)):

        for i in range(len(string) - len_sub + 1):

            p_sub = string[i:i + len_sub].encode('utf-8')
            h_sub = hashlib.sha1(p_sub).hexdigest()

            result += 0 if h_space == h_sub else 1

    return result


print(substring_count("My cat - Vasiliy"))
