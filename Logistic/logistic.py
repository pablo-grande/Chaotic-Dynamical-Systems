import math
from random import random


def iterate(func, x, limit=10):
    for _ in range(limit):
        x = func(x)
        print(x)


def C(x):
    return math.cos(x)


def S(x):
    return math.sin(x)


def E(x):
    return (1 / math.e) * math.e**x


def A(x):
    return math.atan(x)


functions = (C, S, E, A)
for i in range(1, 6):
    print("Iteration", i)
    for f in functions:
        seed = random()
        print(f"{f.__name__}(x) where x = {seed}")
        iterate(f, seed)
