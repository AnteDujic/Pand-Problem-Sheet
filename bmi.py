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

"""
REFERENCES:
- input: https://www.w3schools.com/python/ref_func_input.asp
- formula: https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
- round: https://www.w3schools.com/python/ref_func_round
- BMI calculator: https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792
"""