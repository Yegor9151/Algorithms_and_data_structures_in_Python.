"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

# Preprocess
import random

A = [random.randint(0, 100) for _ in range(10)]
print(A)

min_i = 0
max_i = 0
for i in range(len(A)):
    if A[min_i] > A[i]:
        min_i = i
    if A[max_i] < A[i]:
        max_i = i
print(A[min_i], A[max_i])

A[min_i], A[max_i] = A[max_i], A[min_i]
print(A)
