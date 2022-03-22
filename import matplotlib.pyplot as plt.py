import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
cubes = [1, 8, 27, 64, 125]

fig, ax = plt.subplots()
ax.plot(input_values, squares, 'mD:', color="red", label="Deaths")
ax.set_yticks(range(5,26,5))

ax1 = ax.twinx()
ax1.plot(input_values, cubes, 'ro--', color="green", label="Vaccines")
ax1.set_yticks(range(25,126,25))

fig.suptitle("Deaths and Vaccines", fontsize=18)
ax.set_title("For Specified Country", fontsize=14)

leg = ax.legend(loc='upper left')
leg1 = ax1.legend(loc='center left')

plt.show()