import matplotlib.pyplot as plt

# Original triangle vertices
x = [1, 3, 6]
y = [0, 6, 0]

# Translation values
tx = 2
ty = 5

# Perform translation
translated_x = [vertex + tx for vertex in x]
translated_y = [vertex + ty for vertex in y]

# Plotting the original triangle
plt.plot(x + [x[0]], y + [y[0]], 'b-', label='Original')

# Plotting the translated triangle
plt.plot(translated_x + [translated_x[0]], translated_y + [translated_y[0]], 'r--', label='Translated')

# Set axis limits
plt.xlim(min(x + translated_x) - 1, max(x + translated_x) + 1)
plt.ylim(min(y + translated_y) - 1, max(y + translated_y) + 1)

# Add legend and labels
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')

# Display the plot
plt.show()