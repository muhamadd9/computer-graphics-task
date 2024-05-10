import matplotlib.pyplot as plt

# Original rectangle vertices
x = [0, 4, 4, 0, 0]
y = [0, 0, 3, 3, 0]

# Scaling factors
sx = 2
sy = 4

# Perform scaling
scaled_x = [vertex * sx for vertex in x]
scaled_y = [vertex * sy for vertex in y]

# Plotting the original rectangle
plt.plot(x, y, 'b-', label='Original')

# Plotting the scaled rectangle
plt.plot(scaled_x, scaled_y, 'r--', label='Scaled')

# Set axis limits
plt.xlim(min(x + scaled_x) - 1, max(x + scaled_x) + 1)
plt.ylim(min(y + scaled_y) - 1, max(y + scaled_y) + 1)

# Add legend and labels
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')

# Display the plot
plt.show()