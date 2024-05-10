#Curves Tasks
import numpy as np
from scipy.interpolate import splprep, splev
import matplotlib.pyplot as plt

def spline_curve(x, y, num_points=1000):
    tck, u = splprep([x, y], s=0)
    u_new = np.linspace(u.min(), u.max(), num_points)
    x_new, y_new = splev(u_new, tck)

    plt.plot(x_new, y_new)  # Plot the spline curve
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

x = [0, 1, 3, 4]  
y = [0, 2, -1, 3]  
spline_curve(x, y)