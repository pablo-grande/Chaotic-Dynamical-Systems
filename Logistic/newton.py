import numpy as np


def f(z):
    return z**2 + 5 / 4


p1 = np.roots([1, 0, -5 / 4])
print("Period-1 orbit(s):", p1)

min_threshold = 2

p2 = []
for p in p1:
    x0 = p
    for i in range(20):
        x1 = f(x0)
        x2 = f(x1)
        z = x0 - (x1 - x0) ** 2 / (x2 - 2 * x1 + x0)
        if abs(z - x0) < min_threshold:
            p2.append(z)
            break
        x0 = z
print("Period-2 orbit(s):", p2)

p3 = []
for p in p1:
    x0 = p
    for i in range(20):
        x1 = f(x0)
        x2 = f(x1)
        x3 = f(x2)
        z = x0 - (x1 - x0) ** 2 * (x2 - x0) / (x3 - 3 * x2 + 3 * x1 - x0)
        if abs(z - x0) < min_threshold:
            p3.append(z)
            break
        x0 = z
print("Period-3 orbit(s):", p3)
