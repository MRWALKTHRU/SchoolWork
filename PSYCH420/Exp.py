import numpy as np
from matplotlib import pyplot as mat

# Create the x axis, makes dots from 1 to 5 with 100 equal intervals
x = np.linspace(1,5,100)
# Create the y axis
y = (1/(x**2))

# Create the plot by assigning a figure and axes (This part kinda confuses me still)
fig, ax = mat.subplots()
# plots the graph
ax.plot(x, y, color='tab:red', linewidth='2')


# Make it look nice
ax.set_yticks([0.1, 0.5, 1])
ax.set_yticklabels(["10%", "50%", "100%"])
ax.set_xticks([1,2,3,4,5])
ax.set_ylabel("Memory Accuracy")
ax.set_xlabel("Days since learning")
mat.title("The Ebbinghaus Forgetting Curve")

# Make it show up
mat.show()
