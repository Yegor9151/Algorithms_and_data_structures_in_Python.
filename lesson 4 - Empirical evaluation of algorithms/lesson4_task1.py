"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

Sample:
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random
import cProfile


def gen_array(n):
    return [random.randint(-1000, 1000) for _ in range(n)]


def max_from_min1(n: int) -> int:
    sub_zero = [i for i in gen_array(n) if i < 0]
    num = float('-inf')
    for i in sub_zero:
        if i > num:
            num = i
    return num


def max_from_min2(n: int) -> int:
    num = float('-inf')
    for i in gen_array(n):
        if i < 0 and i ** 2 < num ** 2:
            num = i
    return num


def max_from_min3(n: int) -> int:
    num = float('-inf')
    for i in gen_array(n):
        if num < i < 0:
            num = i
    return num


# cProfile.runctx('max_from_min1(1000000)', globals(), locals())
# cProfile.runctx('max_from_min2(1000000)', globals(), locals())
cProfile.runctx('max_from_min3(1000000)', globals(), locals())
"""
        max_from_min1
    timeit:
(n=10)      = 1000 loops, best of 5: 7.66 usec per loop
(n=100)     = 1000 loops, best of 5: 76 usec per loop
    cProfile:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.009    0.009    1.916    1.916 <string>:1(<module>)
        1    0.000    0.000    1.844    1.844 lesson4_task1.py:21(gen_array)
        1    0.266    0.266    1.844    1.844 lesson4_task1.py:22(<listcomp>)
        1    0.013    0.013    1.907    1.907 lesson4_task1.py:25(max_from_min1)
        1    0.050    0.050    0.050    0.050 lesson4_task1.py:26(<listcomp>)
  1000000    0.443    0.000    0.638    0.000 random.py:238(_randbelow_with_getrandbits)
  1000000    0.615    0.000    1.253    0.000 random.py:291(randrange)
  1000000    0.326    0.000    1.579    0.000 random.py:335(randint)
        1    0.000    0.000    1.916    1.916 {built-in method builtins.exec}
  1000000    0.084    0.000    0.084    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1023770    0.111    0.000    0.111    0.000 {method 'getrandbits' of '_random.Random' objects}

        max_from_min2
    timeit:
(n=10)      = 1000 loops, best of 5: 9.59 usec per loop
(n=100)     = 1000 loops, best of 5: 99.8 usec per loop
    cProfile:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.095    2.095 <string>:1(<module>)
        1    0.000    0.000    1.853    1.853 lesson4_task1.py:21(gen_array)
        1    0.268    0.268    1.853    1.853 lesson4_task1.py:22(<listcomp>)
        1    0.242    0.242    2.095    2.095 lesson4_task1.py:34(max_from_min2)
  1000000    0.437    0.000    0.632    0.000 random.py:238(_randbelow_with_getrandbits)
  1000000    0.620    0.000    1.252    0.000 random.py:291(randrange)
  1000000    0.333    0.000    1.585    0.000 random.py:335(randint)
        1    0.000    0.000    2.095    2.095 {built-in method builtins.exec}
  1000000    0.085    0.000    0.085    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1023638    0.111    0.000    0.111    0.000 {method 'getrandbits' of '_random.Random' objects}

        max_from_min3
    timeit:
(n=10)      = 1000 loops, best of 5: 7.52 usec per loop
(n=100)     = 1000 loops, best of 5: 77.2 usec per loop
    cProfile:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.038    2.038 <string>:1(<module>)
        1    0.000    0.000    1.988    1.988 lesson4_task1.py:21(gen_array)
        1    0.298    0.298    1.988    1.988 lesson4_task1.py:22(<listcomp>)
        1    0.050    0.050    2.038    2.038 lesson4_task1.py:42(max_from_min3)
  1000000    0.474    0.000    0.681    0.000 random.py:238(_randbelow_with_getrandbits)
  1000000    0.657    0.000    1.338    0.000 random.py:291(randrange)
  1000000    0.352    0.000    1.690    0.000 random.py:335(randint)
        1    0.000    0.000    2.038    2.038 {built-in method builtins.exec}
  1000000    0.090    0.000    0.090    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1023569    0.117    0.000    0.117    0.000 {method 'getrandbits' of '_random.Random' objects}

Вывод:
Самый первый вариант функции оказался самым эффективным, ни смотря на то, что в нем массив прогоняется 2 раза.
Возможно это из-за того, что после первого прогона, около половины значений отфильтровывается.
"""
