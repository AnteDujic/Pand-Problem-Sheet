# Program that takes a positive floating-point number as input 
    # Outputs an approximation of its square root
# Author: Ante Dujic

# Importing math module to allow use of mathematical functions 
import math

# Defining the function
def sqrt (x):
   n = 1.0                                       # Iteration initialisation
   tolerance = 0.000001                                 # Set the tolerance for comparison (exiting the loop)
   while True:
        n = 0.5 * (n + x / n)      # Formula
        difference = abs(x - n ** 2)             # Difference
        if difference <= tolerance:                     # Exiting the loop if condition met
            break
   return n

# Prompting user for the number input
x = float (input("Please enter a positive number: "))

# If input number is negative output the massage
    # And prompt the user for the positive number input
if x < 0:
    print ("It is imposible to find a sqare root of a negative number")
    x = float (input("Please enter a POSITIVE number: "))

# Output | Calling the function and rounding to 1 decimal space)
print("The sqare root of {} is approx. {}" .format (x, (round ((sqrt (x)), 1))))

"""
REFERENCES:
- math module: https://docs.python.org/3/library/math.html
- function: https://www.w3schools.com/python/python_functions.asp
- return: https://realpython.com/python-return-statement/
- formula: https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html
"""