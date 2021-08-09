"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

# Preprocess
import random

A = [random.randint(0, 10) for _ in range(10)]
print(A)

first_i = 0
second_i = 1

for i in range(len(A)):
    if A[first_i] > A[i]:
        first_i = i
for i in range(len(A)):
    if A[second_i] > A[i] and i != first_i:
        second_i = i

print(A[first_i], A[second_i])
