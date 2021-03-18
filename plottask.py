# Program that displays a plot of the functions
    # f(x)=x, g(x)=x^2, h(x)=x^3
    # in the range [0,4] on the one set of axes
# Author: Ante Dujic

import numpy as np
import matplotlib.pyplot as plt 

xpoints = np.array (range(0, 4))    # https://www.w3schools.com/python/numpy_creating_arrays.asp
ypointsF = xpoints
ypointsG = xpoints **2
yponitsH = xpoints **3

plt.plot (xpoints, ypointsF)        # https://www.w3schools.com/python/matplotlib_pyplot.asp
plt.plot (xpoints, ypointsG)
plt.plot (xpoints, yponitsH)
plt.show ()
