"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

chars = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

first = input('Введите первую букву: ')
second = input('Введите вторую букву: ')

idx_first = chars.index(first) + 1
idx_second = chars.index(second) + 1
print(f'{first} - {idx_first} буква в алфавите\n'
      f'{second} - {idx_second} буква в алфавите')

rng = idx_second - idx_first - 2
print(f'Меджу {first} и {second} ' + ('нет букв' if rng < 0 else f'- {rng} букв'))
