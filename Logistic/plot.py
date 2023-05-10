import math
import matplotlib.pyplot as plt


def C(x):
    return math.cos(x)


def S(x):
    return math.sin(x)


def E(x):
    return (1 / math.e) * math.e**x


def A(x):
    return math.atan(x)


functions = {"cos(x)": C, "sin(x)": S, "1/e * e^x": E, "arctan(x)": A}

for fig, (name, f) in enumerate(functions.items()):
    x_vals = [i / 10 for i in range(-40, 41)]
    # calculate the corresponding range of function values
    y_vals = [f(x) for x in x_vals]
    plt.plot(x_vals, y_vals)
    # identify the fixed points of the function
    fixed_points = [
        x_vals[i] for i in range(len(y_vals) - 1) if y_vals[i] * y_vals[i + 1] <= 0
    ]
    plt.plot(fixed_points, [0] * len(fixed_points), "ro")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Plot of {name}")
    plt.show()
