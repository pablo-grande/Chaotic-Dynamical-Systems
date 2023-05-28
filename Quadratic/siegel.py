import numpy as np
import matplotlib.pyplot as plt

phi = (np.sqrt(5) - 1) / 2
c_phi = 1/2 * np.exp(2 * np.pi * 1j * phi) - 1/4 * np.exp(4 * np.pi * 1j * phi)

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

def plot_dynamical_plane(c, N, max_iterations=1000, points=""):
    """
    Plot the Dynamical Plane set for the function Qc(z) = z^2 + c.

    Parameters:
        c (complex): The parameter c in Qc(z) = z^2 + c * phi
        N (int): Grid size for the complex plane.
        max_iterations (int): Maximum number of iterations.
        points (list): Arbitraty points near the indifferent fixed point

    Returns:
        None
    """
    xmin, xmax, ymin, ymax = -2, 2, -2, 2
    x = np.linspace(xmin, xmax, N)
    y = np.linspace(ymin, ymax, N)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    dynamical_plane = np.zeros((N, N))
    for l in range(N):
        for m in range(N):
            z = Z[l, m]
            dynamical_plane[l, m] = iterate_z(z, c, max_iterations)

    plt.imshow(dynamical_plane.T, cmap='hot', extent=[xmin, xmax, ymin, ymax])
    plt.colorbar()
    plt.xlabel('Real')
    plt.ylabel('Imaginary')

    for point in points:
        orbit = [point]
        for _ in range(max_iterations):
            z = orbit[-1]
            next_z = z**2 + c
            orbit.append(next_z)
            if abs(next_z) > 10:
                break
        plt.plot(np.real(orbit), np.imag(orbit), 'w-', linewidth=1)

    plt.savefig(f'Quadratic/siegel_{"2" if points else "1"}.png')
    plt.close()

N = 500
points = [0.5 + 0.1j, 0.51 + 0.1j, 0.49 + 0.11j, 0.5 + 0.09j, 0.52 + 0.1j]
plot_dynamical_plane(c_phi, N, points=points)
