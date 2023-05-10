import numpy as np
import matplotlib.pyplot as plt

# define the range of lambda values and the number of iterations
lambdas = np.linspace(0, 1, 1000)
n_iterations = 100

# iterate the sine map for each lambda and store the resulting values of x
x_values = []
for lam in lambdas:
    x = np.random.random()
    for i in range(n_iterations):
        x = lam * np.sin(np.pi * x)
    x_values.append(x)

plt.scatter(lambdas, x_values, s=0.1, c='black')
plt.xlabel('Lambda')
plt.ylabel('x')
plt.title('Bifurcation Diagram of the Sine Map')
plt.show()
