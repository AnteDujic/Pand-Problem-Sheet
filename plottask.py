# Program that displays a plot of the functions
    # f(x)=x, g(x)=x^2, h(x)=x^3
    # in the range [0,4] on the one set of axes
# Author: Ante Dujic

# Importing numpy and mataplotlib.pyplot
    # numpy - to work with arrays
    # mataplotlib.pyplot- for plotting
import numpy as np
import matplotlib.pyplot as plt 

# Defining variables
x = np.array (range(0, 4))              # x defined as array in range 0 to 4
yF = x
yG = x**2
yH = x**3

# Visualisation
    # Drawing plots and customizing them
plt.plot (x, yF, label = "f(x)", color='red', linestyle='solid', marker='o', markerfacecolor='red', markersize=5) 
plt.plot (x, yG, label = "g(x)", color='green', linestyle='dashed', marker='o', markerfacecolor='green', markersize=5)
plt.plot (x, yH, label = "h(x)", color='blue', linestyle='dotted', marker='o', markerfacecolor='blue', markersize=5)
    # Naming Axis
plt.xlabel("x-axis")
plt.ylabel("y-axis")
    # Naming plot
plt.title("Functions \n f(x)=x; g(x)=x^2; h(x)=x^3")
    # Showing legend
plt.legend()
    # Saving image of the plot
plt.savefig ('functionsPlot.png')
    # Outputing final plot
plt.show ()


"""
REFERENCES:
- numpy: https://realpython.com/numpy-tutorial/
- matplotlib.pyplot: https://www.w3schools.com/python/matplotlib_pyplot.asp
- create array: https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp
- plotting and visualisation: https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html
- nameing axis, title: https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib
"""
