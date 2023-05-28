import numpy as np

def compute_fixed_points_and_multipliers(a, b, c):
    """
    Quadratic formula implementation with multipliers

    Parameters:
        a (int): First coefficient
        b (int): Second coefficient
        c (complex): The parameter c in Qc(z) = z^2 + c_phi
    
    Returns:
        z_1 (int): First fixed point
        multiplier_1 (np.abs): absolute values of the derivatives
        z_2 (int): Second fixed point
        multiplier_2 (np.abs): absolute values of the derivatives
    """
    z_1 = (-b + np.sqrt(b**2 - 4 * a * c)) / (2 * a)
    z_2 = (-b - np.sqrt(b**2 - 4 * a * c)) / (2 * a)
    derivative_1 = 2 * z_1
    derivative_2 = 2 * z_2
    return z_1, np.abs(derivative_1), z_2, np.abs(derivative_2)

phi = (np.sqrt(5) - 1) / 2
c_phi = 1/2 * np.exp(2 * np.pi * 1j * phi) - 1/4 * np.exp(4 * np.pi * 1j * phi)

print("Fixed point 1 {}\nMultiplier 1 {}\nFixed point 2: {}\nMultiplier 2: {}".format(*compute_fixed_points_and_multipliers(1, -1, c_phi)))
