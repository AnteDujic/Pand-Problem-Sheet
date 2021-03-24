# Program that asks the user to input any positive integer and outputs the following
    # At each step calculates the next value by taking the current value and
        # If it's even - devide by two, if it's odd - multiply by three and add one
    # Program ends when the current value is 1
# Author: Ante Dujic

# Inputting integer (Prompting user to enter a positive integer)
    # Convert to int, as it's str by default
numberEntered = int (input ("Please enter a positive integer: "))           

# Setting While loop, if the input is negative (less than 0) or 0
    # If true output the message and prompt the user for the input again
    # If false exit loop, move to the next line
while numberEntered <= 0:                                                   
    print ("You've entered a negative integer!")
    numberEntered = int (input ("Please enter a POSITIVE integer: "))

# Create a list
numbersListed = []

# Add to the list
numbersListed.append (int(numberEntered))                                   

# Setting While loop, if number is different to 1 (When it gets to 1 exit loop)
while numberEntered != 1:                                                   
    if numberEntered % 2 == 0:                                                  # If even
        numberEntered = numberEntered / 2                                       # Divide by 2
    else:                                                                       # If odd (not even)
        numberEntered = (numberEntered * 3) + 1                                 # Multiply by 3 and add 1
    
    # Add numbers to the list
    numbersListed.append (int(numberEntered))                               

# Output the list
print (numbersListed)