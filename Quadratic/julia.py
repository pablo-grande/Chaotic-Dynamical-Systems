import numpy as np
import matplotlib.pyplot as plt

def iterate_z(z, c, max_iterations, threshold=10):
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
    for i in range(max_iterations):
        z = z**2 + c
        # stopping condition
        if abs(z) > threshold:
            return i
    return max_iterations

def plot_julia_set(c, N, max_iterations=100):
    """
    Plot the Julia set for the function Qc(z) = z^2 + c.

    Parameters:
        c (complex): The parameter c in Qc(z) = z^2 + c.
        N (int): Grid size for the complex plane.
        max_iterations (int): Maximum number of iterations.

    Returns:
        None
    """
    xmin, xmax, ymin, ymax = -2, 2, -2, 2

    julia_set = np.zeros((N, N))
    for l in range(N):
        for m in range(N):
            # Use the given expression to define the grid points
            z = -2 + 4 * l / N + (-2 + 4 * m / N) * 1j
            julia_set[l, m] = iterate_z(z, c, max_iterations)

    plt.imshow(julia_set.T, cmap='hot', extent=[xmin, xmax, ymin, ymax])
    plt.colorbar()
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.savefig(f'Quadratic/julia_set_{c.real}_{c.imag}.png')
    plt.close()

c_values = [
    -1/2 - 1/10j, # c0
    1/2j, # c1
    -1, # c2
    1/4, # c3
    -3/4 # c4
]

N = 500
# Iterate over c_values and plot/save Julia sets
for c in c_values:
    plot_julia_set(c, N)
