import matplotlib.pyplot as plt

# define data
x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

# make plot
plt.scatter(x_values, cubes, edgecolor='none', s=40)

# customize plot
plt.title('cubes', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('cube of value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

# show plot
plt.show()

# define data
x_values = list(range(1, 5000))
y_values = [x ** 3 for x in x_values]

# make plot
plt.scatter(x_values, y_values, edgecolor='none', s=40)

# customize plot
plt.title('cubes', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('cube of value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 5100 ** 3])

# show plot
plt.show()
