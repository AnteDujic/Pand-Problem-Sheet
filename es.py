# Program that reads in a text file
    # It outputs the number of e's in the file
# Author: Ante Dujic

myFile = input ("Please write a file name (.txt): ")
stringToCount = input ("Please write a string you want to count:")

with open (myFile, "rt") as f:
    data = f.read ()
    stringCount = data.count (stringToCount)
    print (stringCount)

    # https://www.w3schools.com/python/ref_string_count.asp
    # https://www.guru99.com/python-string-count.html#:~:text=Python%20count,want%20the%20search%20to%20begin.