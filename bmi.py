# Program that calculates Body Mass Index (BMI)
# Author: Ante Dujic

# Inputting height and weight (prompting user for the inputs)
    # convert input to float, because it's str by default

height = float (input ("Enter height (cm): "))                
weight = float (input ("Enter weight (kg): "))

# Calculating and rounding BMI to 2 decimal places
    # syntax: round(number, digits)

BMI = round((weight/((height/100)**2)),2)                   

# Printing the BMI

print ("BMI is:",BMI)                                       