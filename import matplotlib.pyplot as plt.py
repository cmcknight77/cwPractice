import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
cubes = [1, 8, 27, 64, 125]

fig.suptitle("Figure title", fontsize=18)

fig, ax = plt.subplots()
ax.plot(input_values, squares, 'mD:', label="Squares")
ax.set_yticks(range(5,26,5))

ax1 = ax.twinx()
ax1.plot(input_values, cubes, 'ro--', label="Cubes")
ax1.set_yticks(range(25,126,25))

ax.legend()

plt.show()