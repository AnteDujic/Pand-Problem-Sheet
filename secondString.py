# Program that asks user to input a string and outputs every second letter in reverse order
# Author: Ante Dujic

# Inputting a string (Prompting user for the input)

stringInput = input ("Please enter a sentence: ")

# Taking every second character of a string
# REF: https://stackoverflow.com/questions/509211/understanding-slice-notation

stringSecond = (stringInput [1::2])

# Outputting every second character in reverse
# REF: https://stackoverflow.com/questions/509211/understanding-slice-notation

print (stringSecond [::-1])