"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random

A = [random.randint(0, 10) for _ in range(100)]
print(A)

B = {}
for i in A:
    if i in B:
        B[i] += 1
    else:
        B[i] = 1
print(B)

max_b, result = 0, 0
for i, v in B.items():
    if v > max_b:
        max_b, result = v, i
print(f'число {result} встречается {max_b} раз')
