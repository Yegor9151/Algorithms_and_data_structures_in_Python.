"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import defaultdict

ent_count = int(input("Введите число предприятий:"))
enterprises = defaultdict(int)
all_profit = 0
for i in range(ent_count):
    ent_name = input(f"Введите название {i + 1} предприятия:")
    for j in range(4):
        profit = int(input(f"Введите прибыль от {ent_name} за {j + 1} квартал"))
        all_profit += profit
        enterprises[ent_name] += profit

mean_profit = all_profit / (ent_count * 4)

more_mean = defaultdict(int)
less_mean = defaultdict(int)
for i, v in enterprises.items():
    v /= 4
    if v > mean_profit:
        more_mean[i] = v
    elif v < mean_profit:
        less_mean[i] = v

print(f'Средняя прибыль за год для всех предприятий = {mean_profit}')
print(f'\nПредприятия чья прибыль выше средней')
for k, v in more_mean.items():
    print(f'{k} = {v}')
print(f'\nПредприятия чья прибыль ниже средней')
for k, v in less_mean.items():
    print(f'{k} = {v}')
