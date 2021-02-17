MODULE: Programming and Scripting
WEEKLY TASKS
AUTHOR: Ante Dujic

WEEK 2
•	bmi.py
Write a program that calculates somebody’s Body Mass Index (BMI)
-	The inputs are the person's height in centimetres and weight in kilograms
-	The output is their weight divided by their height in metres squared

Program asks the user to input height (cm) and weight (kg). It then calculates BMI using formula BMI = kg/m2 (converting cm to m), rounds it and prints it out.


WEEK 3
•	secondString.py
Write a program that takes asks a user to input a string and outputs every second letter in reverse order.

Program asks the user to write a sentence. It takes every second letter of that sentence using slicing notation and then print them out in reverse order using slicing notation again.
REF: https://stackoverflow.com/questions/509211/understanding-slice-notation


WEEK 4
•	collatz.py
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

Program asks the user to input a positive integer (…int (input…). I’ve converted input to int as it’s str as per default. I’ve set up While loop if the input is less (negative) or equal to  0. As long as that is true, program runs in loop outputting the programmed sentence and prompting the user to input a positive integer. If false program moves to the next line, setting up a list and add to list commands. I’ve then set up While loop to run the following lines (If number is even to run the calculation, or (else) if number is not even (is odd) to run the other given calculation) if the current number is different then 1. It keeps adding the numbers to the list. If false (If the current number is equal to 1) the While loop stops and goes to the next line. The program prints out the list.
REF: https://www.w3schools.com/python/ref_list_append.asp
	https://www.w3schools.com/python/python_while_loops.asp


