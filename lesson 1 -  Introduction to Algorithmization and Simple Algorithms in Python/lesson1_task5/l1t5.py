"""
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

char = input('Введите номер буквы: ')
idx_char = ord('a') + int(char) - 1

print(f'{char} буква - {chr(idx_char)}\n')
