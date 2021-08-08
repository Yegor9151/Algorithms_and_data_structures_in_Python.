"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

# Preprocess
import random

A = [random.randint(0, 10) for _ in range(10)]
print(A)

result = random.choice(A)
for i in A:
    if result < i:
        result = i

# General
result = [result] * 2
for i in A:
    if result[0] > i:
        result[0] = i

A.remove(result[0])
for i in A:
    if result[1] > i:
        result[1] = i

print(result)
