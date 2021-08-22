"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""


def create_graph(n):  # здесь просто создаем матрицу друзей
    result = []
    for i in range(n):
        row = [1] * n
        row[i] = 0
        result.append(row)
    return result


while True:
    try:
        N = int(input("Введите число друзей"))
        break
    except ValueError:
        print('Можно вводить только целые числа')

friends_graph = create_graph(N)


def unique_edges(graph):
    result = 0
    for i, row in enumerate(graph):  # берем каждого отдельного друга
        print(f'\nМатрица рукопожатий {i + 1} друга', *graph, sep='\n')
        for j, col in enumerate(row):  # перебираем его список друзей
            result += col  # если текущий друг еще не здаровался с очередным другом, то подсчитываем рукопожатие
            graph[i][j] = graph[j][i] = 0  # обрубаем возможность здароваться у этих двух друзей с обеих сторон
    return result


handshake = unique_edges(friends_graph)
print(f'\nВсего не повторяющихся рукопожатий - {handshake}')
