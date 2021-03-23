# **MODULE: Programming and Scripting**
## **WEEKLY TASKS**
## **AUTHOR: Ante Dujic**

This README file contains explanation of the code written to solve the problems assigned in weekly tasks for Programming and Scripting Module.



## **WEEK 2**
### **bmi.py**
Write a program that calculates somebody’s Body Mass Index (BMI)
-	The inputs are the person's height in centimetres and weight in kilograms
-	The output is their weight divided by their height in metres squared

*CODE:*

```python
height = float (input ("Enter height (cm):”))
weight = float (input ("Enter weight (kg): "))

BMI = round((weight/((height/100)**2)),2)

print ("BMI is:",BMI)     
```
*EXPLANATION:*

_Program asks the user to input height (cm) and weight (kg) as a float number. It then calculates BMI using formula BMI = kg/m^2 (converting cm to m), rounds it using round() function  and prints it out._

*REFERENCES:*
-	https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
-	https://www.w3schools.com/python/ref_func_round.asp
-	https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792


## **WEEK 3**
### **secondString.py**

Write a program that asks a user to input a string and outputs every second letter in reverse order.

*CODE:*

```python
stringInput = input ("Please enter a sentence: ")
stringSecond = (stringInput [1::2])
print (stringSecond [::-1])
```

*EXPLANATION:*

_Program asks the user to write a sentence. It takes every second letter of that sentence using slicing notation and then prints them out in reverse order using slicing notation again._

*REFERENCES:*
- https://stackoverflow.com/questions/509211/understanding-slice-notation
- https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python

## **WEEK 4**
### **collatz.py**

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

*CODE:*

```python

numberEntered = int (input ("Please enter a positive integer: ")

while numberEntered <= 0:                                                   
    print ("You've entered a negative integer!")
    numberEntered = int (input ("Please enter a POSITIVE integer: "))

numbersListed = []                                                          
numbersListed.append (int(numberEntered))                                   

while numberEntered != 1
    if numberEntered % 2 == 0:                                                  
        numberEntered = numberEntered / 2                                       
    else:                                                                       
        numberEntered = (numberEntered * 3) + 1                                 
    numbersListed.append (int(numberEntered))

print (numbersListed)
```


*EXPLANATION:*

_Program asks the user to input a positive integer. The While loop is set up, if the input is less (negative) or equal to  0. As long as that is true, program runs in loop outputting the programmed sentence and prompting the user to input a positive integer. If false program moves to the next line, setting up a list and add to list commands. Then the While loop is set up, to run the following lines (If number is even to run the calculation, or (else) if number is not even (is odd) to run the other given calculation) if the current number is different then 1. It keeps adding the numbers to the list. If false (If the current number is equal to 1) the While loop stops and goes to the next line. The program prints out the list._

*REFERENCES:*

-	https://www.w3schools.com/python/ref_list_append.asp
-	https://www.w3schools.com/python/python_while_loops.asp

## **WEEK 5**
### **weekday.py**

Write a program that outputs whether or not today is a weekday.

*CODE:*

```python
import datetime                                         

today = datetime.datetime.now()

if (int ((today.strftime("%u"))) > 5):
    print ("Today is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday.")
```

*EXPLANATION:*

_A module ‘’datetime’’ gets imported. It manipulates date and time. To get the proper date the ‘’%u” formatting is used, starting with Mon  (1) and ending with Sun (7). Program checks what day it is and its corresponding number and compares it to 5 to check if it’s weekday (1-5), or weekend (6-7)._

*REFERENCES:*

-	 https://www.w3schools.com/python/python_datetime.asp

