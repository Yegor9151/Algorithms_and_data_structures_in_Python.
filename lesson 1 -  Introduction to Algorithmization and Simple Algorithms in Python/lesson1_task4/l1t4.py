"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

first = input('Введите первую букву: ')
second = input('Введите вторую букву: ')

idx_first = ord(first) - ord('a') + 1
idx_second = ord(second) - ord('a') + 1

print(f'{first} - {idx_first} буква в алфавите\n'
      f'{second} - {idx_second} буква в алфавите')

rng = idx_second - idx_first - 2
print(f'Меджу {first} и {second} ' + ('нет букв' if rng < 0 else f'- {rng} букв'))
