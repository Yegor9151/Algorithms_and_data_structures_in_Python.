"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.

Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2
"""
import cProfile


def prime(n):
    num = 2
    array = [num]
    while len(array) < n:
        num += 1
        for d in array:
            if num % d == 0:
                break
        else:
            array.append(num)

    return array[-1]


def sieve(n):
    num = 2
    while True:
        num += 1
        array = [i for i in range(num)]
        array[1] = 0
        for i in range(2, num):
            if array[i] != 0:
                j = i * 2
                while j < num:
                    array[j] = 0
                    j += i

        array = [i for i in array if i != 0]
        if len(array) == n:
            break

    return array[-1]


# N = 10
# print(prime(N))
# print(sieve(N))

# cProfile.runctx('prime(1000)', globals(), locals())
# cProfile.runctx('sieve(1000)', globals(), locals())
"""
        prime
    timeit:
(n=10) = 1000 loops, best of 5: 4.82 usec per loop
    cProfile:
1    0.038    0.038    0.040    0.040 lesson4_task2.py:26(prime)

        sieve
    timeit:
(n=10) = 1000 loops, best of 5: 94.3 usec per loop
    cProfile:
1       8.562    8.562   10.630   10.630 lesson4_task2.py:40(sieve)
7918    0.998    0.000    0.998    0.000 lesson4_task2.py:44(<listcomp>)
7918    1.067    0.000    1.067    0.000 lesson4_task2.py:53(<listcomp>)

На больших числах проваерять не стал, слишком болго sieve паботает
"""
