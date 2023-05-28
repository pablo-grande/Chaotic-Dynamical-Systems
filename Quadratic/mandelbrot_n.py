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

    escape_mask = escape_iterations == 100
    fixed_point_mask = escape_iterations == 1
    # converging towards a periodic orbit of two
    period_two_mask = np.logical_and(escape_iterations > 1, escape_iterations % 2 == 0)
    # converging towards a periodic orbit of three
    period_three_mask = np.logical_and(escape_iterations > 1, escape_iterations % 3 == 0)
    # converging towards a periodic orbit of four
    period_four_mask = np.logical_and(escape_iterations > 1, escape_iterations % 4 == 0)
    # converging towards a periodic orbit of five
    period_five_mask = np.logical_and(escape_iterations > 1, escape_iterations % 5 == 0)

    cmap_escape = 'Greys'   # Color #0
    cmap_fixed_point = 'inferno'   # Color #1
    cmap_period_two = 'Blues'   # Color #2
    cmap_period_three = 'Greens'   # Color #3
    cmap_period_four = 'Oranges'   # Color #4
    cmap_period_five = 'Purples'   # Color #5

    plt.imshow(escape_mask.T, cmap=cmap_escape, extent=(-2, 2, -2, 2))
    plt.imshow(fixed_point_mask.T, cmap=cmap_fixed_point, extent=(-2, 2, -2, 2), alpha=0.3)
    plt.imshow(period_two_mask.T, cmap=cmap_period_two, extent=(-2, 2, -2, 2), alpha=0.3)
    plt.imshow(period_three_mask.T, cmap=cmap_period_three, extent=(-2, 2, -2, 2), alpha=0.3)
    plt.imshow(period_four_mask.T, cmap=cmap_period_four, extent=(-2, 2, -2, 2), alpha=0.3)
    plt.imshow(period_five_mask.T, cmap=cmap_period_five, extent=(-2, 2, -2, 2), alpha=0.3)

    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.savefig('Quadratic/mandelbrot_n.png')
    plt.close()

N = 500
mandelbrot_set(N)
