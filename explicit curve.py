import numpy as np
import matplotlib.pyplot as plt

def explicit_curve(function, xlim=(-10, 10), ylim=(-10, 10), num_points=1000):
    x = np.linspace(xlim[0], xlim[1], num_points)
    y = eval(function)  

    plt.plot(x, y) 
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()


function = 'np.sin(x)'
explicit_curve(function)