# Program that calculates Body Mass Index (BMI)
# Author: Ante Dujic

# Inputting height and weight

height = float (input ("Enter height (cm): "))                # convert input to float, because it's str by default
weight = float (input ("Enter weight (kg): "))

# Calculating and rounding BMI to 2 decimal places

BMI = round((weight/((height/100)**2)),2)                   # formula for BMI, rounding to 2 decimals

# Printing the BMI

print ("BMI is:",BMI)                                       # output