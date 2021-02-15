# Program that asks the user to input any positive integer and outputs the following
    # At each step calculates the next value by taking the current value and
        # If it's even - devide by two, if it's odd - multiply by three and add one
# Author: Ante Dujic


numberEntered = int (input ("Please enter a positive integer: "))           # Convert input to int, as it's str by default

while numberEntered <= 0:                                                   # Set While loop, if input is negative or 0 (not positive)
    print ("You've entered a negative integer!")
    numberEntered = int (input ("Please enter a POSITIVE integer: "))

numbersListed = []                                                          # Create the list
numbersListed.append (int(numberEntered))                                   # Add numbers to the list

while numberEntered != 1:                                                   # Set While loop, if number is not 1 to:
    if numberEntered % 2 == 0:                                                  # If even
        numberEntered = numberEntered / 2                                       # Divide by 2
    else:                                                                       # If odd (not even)
        numberEntered = (numberEntered * 3) + 1                                 # Multiply by 3 and add 1
    numbersListed.append (int(numberEntered))                               # Add numbers to the list

print (numbersListed)