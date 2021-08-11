"""1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.Примечание. Идеальным решением будет:a. выбрать хорошую задачу, которую имеет смысл оценивать,b. написать 3 варианта кода (один у вас уже есть),c. проанализировать 3 варианта и выбрать оптимальный,d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),e. написать общий вывод: какой из трёх вариантов лучше и почему."""import randomimport cProfiledef gen_array(n):    return [random.randint(-1000, 1000) for _ in range(n)]def max_from_min1(n: int) -> int:    sub_zero = [i for i in gen_array(n) if i < 0]    num = float('-inf')    for i in sub_zero:        if i > num:            num = i    return numdef max_from_min2(n: int) -> int:    num = float('-inf')    for i in gen_array(n):        if i < 0 and i ** 2 < num ** 2:            num = i    return numdef max_from_min3(n: int) -> int:    num = float('-inf')    for i in gen_array(n):        if num < i < 0:            num = i    return num# cProfile.runctx('max_from_min1(10000000)', globals(), locals())# cProfile.runctx('max_from_min2(10000000)', globals(), locals())# cProfile.runctx('max_from_min3(10000000)', globals(), locals())"""        max_from_min1    timeit:(n=10)      = 1000 loops, best of 5: 7.66 usec per loop(n=100)     = 1000 loops, best of 5: 76 usec per loop    cProfile:1    0.000    0.000   17.583   17.583 lesson4_task1.py:23(gen_array)1    2.522    2.522   17.583   17.583 lesson4_task1.py:24(<listcomp>)1    0.124    0.124   18.193   18.193 lesson4_task1.py:27(max_from_min1)1    0.486    0.486    0.486    0.486 lesson4_task1.py:28(<listcomp>)        max_from_min2    timeit:(n=10)      = 1000 loops, best of 5: 9.59 usec per loop(n=100)     = 1000 loops, best of 5: 99.8 usec per loop    cProfile:1    0.000    0.000   17.864   17.864 lesson4_task1.py:23(gen_array)1    2.624    2.624   17.864   17.864 lesson4_task1.py:24(<listcomp>)1    2.719    2.719   20.583   20.583 lesson4_task1.py:36(max_from_min2)        max_from_min3    timeit:(n=10)      = 1000 loops, best of 5: 7.52 usec per loop(n=100)     = 1000 loops, best of 5: 77.2 usec per loop    cProfile:1    0.000    0.000   18.293   18.293 lesson4_task1.py:23(gen_array)1    2.622    2.622   18.293   18.293 lesson4_task1.py:24(<listcomp>)1    0.581    0.581   18.873   18.873 lesson4_task1.py:44(max_from_min3)Вывод:Самый первый вариант функции оказался самым эффективным, ни смотря на то, что в нем массив прогоняется 2 раза.Возможно это из-за того, что после первого прогона, около половины значений отфильтровывается."""