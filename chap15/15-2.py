from matplotlib import pyplot as plt  # explicit expression

# define data
x_values = list(range(1, 5000))
cubes = [x ** 3 for x in x_values]

# make plot
plt.scatter(x_values, cubes, edgecolor='none', c=cubes, cmap=plt.cm.BuGn, s=40)

# customize plot
plt.title('cubes', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('cube of value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 5100 ** 3])

# show plot
plt.show()
