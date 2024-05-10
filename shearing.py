import matplotlib.pyplot as plt

# Original rectangle vertices
x = [0, 4, 4, 0, 0]
y = [0, 0, 2, 2, 0]

# Shearing factors
sx = 2
sy = 4

# Perform shearing
sheared_x = [vertex + sy * y[i] for i, vertex in enumerate(x)]
sheared_y = [vertex + sx * x[i] for i, vertex in enumerate(y)]

# Plotting the original rectangle
plt.plot(x, y, 'b-', label='Original')

# Plotting the sheared rectangle
plt.plot(sheared_x, sheared_y, 'r--', label='Sheared')

# Set axis limits
plt.xlim(min(x + sheared_x) - 1, max(x + sheared_x) + 1)
plt.ylim(min(y + sheared_y) - 1, max(y + sheared_y) + 1)

# Add legend and labels
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')

# Display the plot
plt.show()