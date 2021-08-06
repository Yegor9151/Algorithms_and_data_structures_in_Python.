"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""

while True:
    operator = input("Введите опаратор (0 - для выхода): ")
    if operator not in '0+-/*':
        print('неверный оператор')
        continue

    print(operator)
    if operator == '0':
        break

    first = int(input("Введите первое число: "))
    print(f"{first} {operator}")

    second = int(input("введите второе число"))
    print(f"{first} {operator} {second}")

    result = None
    if operator == '+':
        result = first + second
    elif operator == '-':
        result = first - second
    elif operator == '*':
        result = first * second
    elif operator == '/':
        if second == 0:
            print("Ошибка деления на ноль")
            continue
        result = first / second
    print(result)

print("Программа завершена")
