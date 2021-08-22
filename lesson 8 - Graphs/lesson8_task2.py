"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""
from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start):
    length = len(graph)

    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    ways = [[] for _ in range(length)]  # создаем пустой 2D массив c высотой length
    ways[start].append(start)  # в стартовую ячейку подавляем её же саму

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True  # отмечаем как посещенное
        for i, vertex in enumerate(graph[start]):  # перебирвем пути и их стоимость
            if vertex and not is_visited[i]:  # если не посещенное имеет цену
                new_cost = vertex + cost[start]  # то мы берем цену складываем с текущей ценой

                if len(ways[i]):  # если в массиве уже что-то есть
                    ways[i] = [start]  # тогда перезаписываем это на последнее значение start
                else:  # иначе
                    ways[i].append(start)  # добавляем последнее значение start

                if cost[i] > new_cost:  # если стоимость следующего объекта больше текущей
                    cost[i] = new_cost
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for i, v in enumerate(ways):  # перебираем индексы и значения
        v = v[0] if v else None  # Вытаскиваем значения ели оно есть
        j = i  # инициализируем отступающий индекс
        if v is None:  # если значение пусто
            ways[i].append('нет пути')  # то пишем, что пути нет
        else:  # иначе
            while j != v:  # запускаем цикл до тех пор пока не доберемся до начала
                ways[i].append(v)
                j = v
                v = ways[j][0]

    for i, v in enumerate(ways):
        if len(v) > 1:
            v[0] = i
            v.reverse()

    return cost, ways


def result(s):
    c, w = dijkstra(g, s)
    for i, v in enumerate(c):
        print(f'{w[i]} - стоимость пути = {v}')


result(int(input("Введите стартовую вершину:")))
