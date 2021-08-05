"""
6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков.
Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

abc = input('Введите длины сторон треугольника (a, b, c): ')
abc = abc.split(',')
a, b, c = map(int, abc)

existence = True if (a + b > c and a + c > b and b + c > a) else False

triangle_type = None
if existence:
    if a == b == c:
        triangle_type = 'равносторонный'
    elif a == b or a == c or b == c:
        triangle_type = 'равнобедренный'
    else:
        triangle_type = 'разносторонный'

print(f'Треугольник существует, и он {triangle_type}' if existence else 'Треугольник не существует')
