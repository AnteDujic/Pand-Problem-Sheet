# **MODULE: Programming and Scripting**
## **WEEKLY TASKS**
## **AUTHOR: Ante Dujic**

This Repostitory contains programs written to solve the problems assigned in weekly tasks for Programming and Scripting Module.

Programs:
1. WEEKLY TASK 1 - bmi.py
2. WEEKLY TASK 2 - secondString.py
3. WEEKLY TASK 3 - collatz.py
4. WEEKLY TASK 4 - weekday.py
5. WEEKLY TASK 5 - squareRoot.py
6. WEEKLY TASK 6 - es.py
7. WEEKLY TASK 7 - plottask.py


## **1. bmi.py**
Write a program that calculates somebody’s Body Mass Index (BMI)
The inputs are the person's height in centimetres and weight in kilograms.
The output is their weight divided by their height in metres squared.

*CODE:*

```python
height = float (input ("Enter height (cm): "))
weight = float (input ("Enter weight (kg): "))

BMI = round((weight/((height/100)**2)),2)

print ("BMI is: ",BMI)     
```
*EXPLANATION:*

_ Program asks the user to input height (cm) and weight (kg) as a float number. It then calculates BMI using formula BMI = kg/m^2 (converting cm to m), rounds it using round() function  and prints it out._

*REFERENCES:*
-	https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
-	https://www.w3schools.com/python/ref_func_round.asp
-	https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792


## **2. secondString.py**

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


## **3. collatz.py**

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

*CODE:*

```python

number = int (input ("Please enter a positive integer: ")

while number <= 0:                                                   
    print ("You've entered a negative integer!")
    number = int (input ("Please enter a POSITIVE integer: "))

numbers = []                                                          
numbers.append (int(number))                                   

while number != 1
    if number % 2 == 0:                                                  
        number = number / 2                                       
    else:                                                                       
        number = (number * 3) + 1                                 
    numbers.append (int(number))

print (numbers)
```


*EXPLANATION:*

_Program asks the user to input a positive integer. The While loop is set up, if the input is less (negative) or equal to  0. As long as that is true, program runs in loop outputting the programmed sentence and prompting the user to input a positive integer. If false, program moves to the next line, setting up a list and add to list commands. Then the While loop is set up, if the current number is different then 1, to run the following lines (If number is even to run the calculation, or (else) if number is not even (is odd) to run the other given calculation). It keeps adding the numbers to the list. If false (If the current number is equal to 1) the While loop stops and goes to the next line. The program prints out the list._

*REFERENCES:*

-   https://www.w3schools.com/python/python_lists.asp
-	https://www.w3schools.com/python/ref_list_append.asp
-	https://www.w3schools.com/python/python_while_loops.asp


## **4. weekday.py**

Write a program that outputs whether or not today is a weekday.

*CODE:*

```python
import datetime as dt                                      

today = dt.datetime.now()

if (int ((today.strftime("%u"))) > 5):
    print ("Today is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday.")
```

*EXPLANATION:*

_A module datetime gets imported. It manipulates date and time.Then, variable for a current day (taday) is set up - dt.datetime.now(). To get the proper date the ‘’%u” formatting is used, starting with Mon  (1) and ending with Sun (7). Program checks what day it is and its corresponding number and compares it to 5 to check if it’s weekday (1-5), or weekend (6-7). To allow comparison strftime() method is used, as it returns string representing the day - which is then converted to integer._

*REFERENCES:*

-	https://www.w3schools.com/python/python_datetime.asp
-   https://www.programiz.com/python-programming/datetime


## **5. squareroot.py**

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root, using Newton method.

*CODE:*

```python
import math

def sqrt (x):
   n = 1.0
   tolerance = 0.000001
   while True:
        n = 0.5 * (n + x / n)
        difference = abs(x - n ** 2)
        if difference <= tolerance:
            break
   return n

x = float (input("Please enter a positive number: "))

if x < 0:
    print ("It is imposible to find a sqare root of a negative number")
    x = float (input("Please enter a POSITIVE number: "))

print("The sqare root of {} is approx. {}" .format (x, (round ((sqrt (x)), 1))))
```

*EXPLANATION:*

_Newton method is used to get the (approx.) square root of a number. It consists of making an educated guess and then entering it into equotation. It is done repeatedly, until the correct square root is obtained. First the math module gets imported, to allow the use of mathematical functions. Then the functions is set up. Within the function variable for initializing the function and the variable for exiting the loop are set up. Then the while loop is set up to run until the condition is met (until difference between absolute value of input number and n^2 is equal or less then tolerance). Outside of function, program prompts the user for an input (positive number). If the input number is negative the massage will be output and the user will be asked to input a positive number. Finally, the function is called within the print function, and the output is rounded to 1 decimal space._

*REFERENCE:*

-	https://docs.python.org/3/library/math.html
-	https://www.school-for-champions.com/algebra/square_root_approx.htm#.YFsohq_7SUn
-	https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
-	https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html
-	https://www.w3schools.com/python/python_functions.asp
-	https://realpython.com/python-return-statement/


## **6. es.py**

Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

*CODE:*

```python
import sys

myFile = sys.argv[1]

with open (myFile, "rt") as f:
    data = f.read ()
    stringCount = data.count ("e")
    print (stringCount)
```

*EXPLANATION:*

_The sys module is imported, to allow the use of sys.argv - a list in Python, which contains the command-line arguments passed to the script. The first argument (sys.argv[0]) is the program name and The rest of the arguments are stored at the subsequent indices (sys.argv[1], sys.argv[2], etc.). The file to be read is defined as the sys.argv[1], which allows for it to be taken from the command line. The file is opened using with open() command. The count() method is used to return the number of times a specified value (string) appears in the file._

*REFERENCE:*

-	https://www.w3schools.com/python/ref_string_count.asp
-	https://www.guru99.com/python-string-count.html
-	https://realpython.com/python-command-line-arguments/
-	https://www.tutorialsteacher.com/python/sys-module
-	https://docs.python.org/3/library/sys.html


## **7. plottask.py**

Write a program that displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes.

*CODE:*
```python
import numpy as np
import matplotlib.pyplot as plt 

x = np.array (range(0, 4))   
yF = x
yG = x**2
yH = x**3

plt.plot (x, yF, label = "f(x)", color='red', linestyle='solid', marker='o', markerfacecolor='red', markersize=5) 
plt.plot (x, yG, label = "g(x)", color='green', linestyle='dashed', marker='o', markerfacecolor='green', markersize=5)
plt.plot (x, yH, label = "h(x)", color='blue', linestyle='dotted', marker='o', markerfacecolor='blue', markersize=5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Functions \n f(x)=x; g(x)=x^2; h(x)=x^3")
plt.legend()

plt.show ()
```

*EXPLANATION:*

_First numpy and matplotlib.pyplot modules get imported. Numpy to work with arrays and matplotlib.pyplot for plotting . Variable x is defined as array in the range from 0 to 4. Variables y for each function are defined (yF, yG, yH) as tasked. Then, plots gets created using plt.plot, where we define some visuals for each function plot (label, color, linestyle, marker, markerfacecolor, markersize). Axis are named using plt.xlabel() and plt.ylabel(), plot named using plt.title and legend defined using plt.legend(). Finally, plot gets output using plt.show()_


*REFERENCE:*

-	https://realpython.com/numpy-tutorial/
-	https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html
-	https://www.w3schools.com/python/matplotlib_pyplot.asp
-   https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp
-   https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html
-   https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib


## **README FORMATTING**
- https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax

