import numpy as np
from math import factorial


def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# 1.
# Найти вероятность того, что все карты – крести:
p1 = (combinations(13, 4) / combinations(52, 4)) * 100
print(f'Шанс выпадания 4 карты крести: {round(p1, 2)}%')
# Шанс выпадания 4 карты крести: 0.26%

# Найти вероятность, что среди 4-х карт окажется хотя бы один туз:
p2 = (combinations(4, 1) * combinations(48, 3)) / combinations(52, 4)
print(f'Шанс выпадания 1 туза карты крести: {round(p2 * 100, 2)}%')
# Шанс выпадания 1 туза карты крести: 25.56%


# 2.
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
p1 = (1 / combinations(10, 3)) * 100
print(f'Вероятность того, что человек, не знающий код, откроет дверь с первой попытки: {round(p1, 2)}%')
# Вероятность того, что человек, не знающий код, откроет дверь с первой попытки: 0.83%


# 3.
# Какова вероятность того, что все извлеченные детали окрашены?
p1 = (combinations(9, 3) / combinations(15, 3)) * 100
print(f'Bероятность того, что все извлеченные детали окрашены: {round(p1, 2)}%')
# Bероятность того, что все извлеченные детали окрашены: 18.46%


# 4.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
p1 = 2 / combinations(100, 2)
print(f'Bероятность того, что 2 приобретенных билета окажутся выигрышными: {round(p1 * 100, 2)}%')
# Bероятность того, что 2 приобретенных билета окажутся выигрышными: 0.04%
