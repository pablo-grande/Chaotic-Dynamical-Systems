import numpy as np
import matplotlib.pyplot as plt


functions = {
    "x-x^2": lambda x: x - x**2,
    "2(x-x^2)": lambda x: 2 * (x - x**2),
    "x^3 - (1/9)x": lambda x: x**3 - (1 / 9) * x,
    "x^3 - x": lambda x: x**3 - x,
    "1/2 sin(x)": lambda x: 1/2 * np.sin(x),
    "sin(x)": lambda x: np.sin(x),
    "e^(x-1)": lambda x: np.e ** (x - 1),
    "e^x": lambda x: np.e**x,
    "arctan(x)": lambda x: np.arctan(x),
    "pi/4 arctan(x)": lambda x: np.pi / 4 * np.arctan(x),
    "-pi/4 arctan(x)": lambda x: -np.pi / 4 * np.arctan(x),
    "x^3-x^2-x": lambda x: x**3 - x**2 - x,
    "sqrt(x+1)": lambda x: np.sqrt(x + 1),
}


# set up the grid
x_min, x_max = -2, 2
y_min, y_max = -2, 2
x, y = np.meshgrid(np.linspace(x_min, x_max, 20), np.linspace(y_min, y_max, 20))
for name, f in functions.items():
    dx = f(x)
    dy = np.ones_like(dx)
    # quiver plot where vectors are represented by arrows
    plt.quiver(x, y, dx, dy, color="r")
    # plot the nullclines
    plt.contour(x, y, dx, levels=[0], colors="b")
    plt.contour(x, y, dy, levels=[0], colors="g")

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(name)
    plt.show()
