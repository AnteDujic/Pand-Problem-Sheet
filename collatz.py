# Program that asks the user to input any positive integer and outputs the following
    # At each step calculates the next value by taking the current value and
        # If it's even - devide by two, if it's odd - multiply by three and add one
    # Program ends when the current value is 1
# Author: Ante Dujic

# Inputting integer (Prompting user to enter a positive integer)
    # Convert to int, as it's str by default
number = int (input ("Please enter a positive integer: "))           

# Setting While loop, if the input is negative (less than 0) or 0
    # If true output the message and prompt the user for the input again
    # If false exit loop, move to the next line
while number <= 0:                                                   
    print ("You've entered a negative integer!")
    number = int (input ("Please enter a POSITIVE integer: "))

# Create a list
numbers = []

# Add to the list
numbers.append (int(number))                                   

# Setting While loop, if number is different to 1 (When it gets to 1 exit loop)
while number != 1:                                                   
    if number % 2 == 0:                                           # If even
        number = number / 2                                       # Divide by 2
    else:                                                         # If odd (not even)
        number = (number * 3) + 1                                 # Multiply by 3 and add 1
    
    # Add numbers to the list
    numbers.append (int(number))                               

# Output the list
print (numbers)


"""
REFERENCES:
- while loop: https://www.w3schools.com/python/python_while_loops.asp
- list: https://www.w3schools.com/python/python_lists.asp
- add to list: https://www.w3schools.com/python/ref_list_append.asp
"""
