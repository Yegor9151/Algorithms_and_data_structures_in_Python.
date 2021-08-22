"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).

Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
import random


def create_graph(N):
    graph = []

    for i in range(N):
        row = []
        range_n = list(range(N))
        range_n.remove(i)

        for _ in range(random.randrange(1, N)):
            num = random.choice(range_n)
            row.append(num)
            range_n.remove(num)

        graph.append(row)

    return graph


gr = create_graph(int(input("введите число вершин графа:")))


def view_graph(graph):
    print('Граф:')
    for i, v in enumerate(graph):
        print(f'{i} > {v}')


view_graph(gr)


def depth_first_search(graph, start, visited):
    visited.append(start)
    for edge in graph[start]:
        if edge not in visited:
            depth_first_search(graph, edge, visited)


vis = []
st = int(input("\nВведите начальную вершину:"))
depth_first_search(gr, st, vis)
print(f'\nПути в глубину графа для {st} вершины: {vis}')
