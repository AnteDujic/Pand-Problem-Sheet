# Program that displays a plot of the functions
    # f(x)=x, g(x)=x^2, h(x)=x^3
    # in the range [0,4] on the one set of axes
# Author: Ante Dujic

import numpy as np
import matplotlib.pyplot as plt 

x = np.array (range(0, 4))   
yF = x
yG = x**2
yH = x**3

plt.plot (x, yF, label = "f(x)", color='red', linestyle='solid', marker='o', markerfacecolor='red', markersize=5) 
plt.plot (x, yG, label = "g(x)", color='green', linestyle='dashed', marker='o', markerfacecolor='green', markersize=5)
plt.plot (x, yH, label = "h(x)", color='blue', linestyle='dotted', marker='o', markerfacecolor='blue', markersize=5)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Functions \n f(x)=x; g(x)=x^2; h(x)=x^3")
plt.legend()
plt.show ()
