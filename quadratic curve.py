import numpy as np
import matplotlib.pyplot as plt

def quadratic_curve(a, b, c, xlim=(-10, 10), ylim=(-10, 10), num_points=1000):
    x = np.linspace(xlim[0], xlim[1], num_points)
    y = a * x**2 + b * x + c

    plt.plot(x, y)  
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()


a = 1
b = 2
c = 1
quadratic_curve(a, b, c)