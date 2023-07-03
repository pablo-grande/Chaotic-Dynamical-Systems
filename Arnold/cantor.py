import numpy as np
import matplotlib.pyplot as plt

def lift(x, omega, epsilon):
    return x + omega + epsilon/(2*np.pi) * np.sin(2*np.pi*x)

def compute_rotation_number(omega, epsilon, x0=0.5, max_iterations=1000):
    x = x0
    for _ in range(max_iterations):
        x = lift(x, omega, epsilon)
    return x / max_iterations

def plot_rotation_numbers(N, epsilon_0):
    omegas = np.linspace(0, 1, N+1)
    rotation_numbers = [
        compute_rotation_number(omega, epsilon_0)
        for omega in omegas
    ]

    plt.plot(omegas, rotation_numbers, 'bo-')
    plt.xlabel('omega')
    plt.ylabel('Rotation Number')
    plt.title(f'Numerical Approximation of Rotation Number (epsilon_0 = {epsilon_0})')
    plt.savefig('cantor.png')
    plt.close()

N = 100
epsilon_0 = 0.8

plot_rotation_numbers(N, epsilon_0)