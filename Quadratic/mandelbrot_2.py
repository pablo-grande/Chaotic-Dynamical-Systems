import numpy as np
import matplotlib.pyplot as plt


def iterate_z(z, c, max_iterations, threshold=2):
    """
    Perform iteration of the quadratic polynomial function Qc(z) = z^2 + c.

    Parameters:
        z (complex): The complex number to iterate.
        c (complex): The parameter c in Qc(z) = z^2 + c.
        max_iterations (int): Maximum number of iterations.
        threshold (int): Point of escape.

    Returns:
        int: The number of iterations until the point escapes or max_iterations is reached.
    """
    iteration = 0
    for _ in range(max_iterations):
        z = z**2 + c
        # stopping condition
        if abs(z) > threshold:
            break
        iteration += 1
    return iteration

def mandelbrot_set(N, max_iterations=100):
    """
    Plot the Mandelbrot set for the function Qc(z) = z^2 + c.

    Parameters:
        N (int): Grid size for the complex plane.
        max_iterations (int): Maximum number of iterations.

    Returns:
        None
    """
    x = np.linspace(-2, 2, N)
    y = np.linspace(-2, 2, N)
    grid = np.array([complex(r, i) for r in x for i in y]).reshape(N, N)

    escape_iterations = np.zeros((N, N))

    for l in range(N):
        for m in range(N):
            c = -2 + 4*l/N + (-2 + 4*m/N)*1j
            z = 0  # Initialize the critical orbit
            escape_iterations[l, m] = iterate_z(z, c, max_iterations)

    bounded_mask = escape_iterations == 100
    escaping_mask = escape_iterations < 100
    cmap_escaping = 'Oranges'
    cmap_bounded = 'Purples'

    plt.imshow(escaping_mask.T, cmap=cmap_escaping, extent=(-2, 2, -2, 2))
    plt.imshow(bounded_mask.T, cmap=cmap_bounded, extent=(-2, 2, -2, 2), alpha=0.6)
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.savefig('Quadratic/mandelbrot_2.png')
    plt.close()

N = 500
mandelbrot_set(N)
