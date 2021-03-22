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

_Program asks the user to input height (cm) and weight (kg) as a float number. It then calculates BMI using formula BMI = kg/m2 (converting cm to m), rounds it using round() function  and prints it out._

*REFERENCES:*
-	https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
-	https://www.w3schools.com/python/ref_func_round.asp
-	https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792
