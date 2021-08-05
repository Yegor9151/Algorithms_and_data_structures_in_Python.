"""
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

chars = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

first = input('Введите номер первой буквы: ')
second = input('Введите номер второй буквы: ')

idx_first = int(first) - 1
idx_second = int(second) - 1

print(f'{first} буква - {chars[idx_first]}\n'
      f'{second} буква - {chars[idx_second]}')
