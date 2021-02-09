# Program that asks user to input a string and outputs every second letter in reverse order
# Author: Ante Dujic

# Inputting a string

stringInput = str (input ("Please enter a sentence: "))

# Taking every second character of a string

stringSecond = (stringInput [1::2])

# Outputting every second character in reverse

print (stringSecond [::-1])