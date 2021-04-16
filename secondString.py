# Program that asks user to input a string and outputs every second letter in reverse order
# Author: Ante Dujic

# Inputting a string (Prompting user for the input)
stringInput = input ("Please enter a sentence: ")

# Taking every second character of a string
stringSecond = (stringInput [1::2])

# Outputting every second character in reverse
print (stringSecond [::-1])

"""
REFERENCES:
- string slicing:
       https://stackoverflow.com/questions/509211/understanding-slice-notation
       https://www.w3schools.com/python/python_strings_slicing.asp
       https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
"""