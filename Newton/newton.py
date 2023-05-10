#!/usr/bin/env python
# -*- coding: utf-8 -*
"""
Newton's Method for finding the roots of a polynomial function.
"""
from textwrap import dedent


def polynomial(x):
    return x**5 + x**2 - x + 1


def derivative_p(x):
    return 5 * x**4 + 2 * x - 1


def newton(x_n, step):
    """
    Computes the next approximation of the root of the polynomial function using Newton's Method.

    Args:
        x_n (float): The initial guess for the root of the polynomial function.
        step (int): The step number of the iteration. Defaults to 0.

    Returns:
        float: The next approximation of the root of the polynomial function.
    """
    p = polynomial(x_n)
    p_prime = derivative_p(x_n)
    f = p / p_prime
    x_n1 = x_n - f
    print(
        dedent(
            f"""
            x_{step} = {x_n} - ({p}/{p_prime})
            x_{step} = {x_n} - ({f})
            x_{step} = {x_n1}
            """
        )
    )
    return x_n1


steps = 6
seeds = [-2, 1 - 1j, -1 + 1j, -1 - 1j]
for seed in seeds:
    print(f"x_0: {seed}")
    for i in range(1, steps + 1):
        seed = newton(seed, i)
