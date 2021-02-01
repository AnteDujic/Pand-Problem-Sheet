# Program that calculates Body Mass Index (BMI)
# Author: Ante Dujic

# Inputting height and weight

height = int (input ("Enter height (cm): "))
weight = int (input ("Enter weight (kg): "))

# Calculating and rounding BMI to 2 decimal places

BMI = round((weight/((height/100)**2)),2)

# Printing the BMI

print ("BMI is:",BMI)