"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

# Preprocess
import random

A = [random.randint(0, 10) for _ in range(10)]
print(A)

first = A[0]
second = A[1]

# General
for i in A:
    if first > i:
        first = i
A.remove(first)

for i in A:
    if second > i:
        second = i

print(first, second)
