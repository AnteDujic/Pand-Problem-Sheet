# Program that takes a positive floating-point number as input 
    # Outputs an approximation of its square root
# Author: Ante Dujic

import math

tolerance = 0.000001
def sqrt (x):
   estimate = 1.0
   while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate


x = float (input("Please enter a positive number: "))
print("The sqare root of {} is approx. {}" .format (x, (round ((sqrt (x)), 1))))