# Program that reads in a text file
    # It outputs the number of e's in the file
# Author: Ante Dujic
import sys

myFile = sys.argv[1]                                                        # setting file to open to be taken from command line
stringToCount = input ("Please write a string you want to count:")          # promting user to input a string to be count

with open (myFile, "rt") as f:                                              # raeding the file (rt - read text file)
    data = f.read ()
    stringCount = data.count (stringToCount)                                # counting inputed string
    print (stringCount)                                                     # output the counted string

    # https://www.w3schools.com/python/ref_string_count.asp
    # https://www.guru99.com/python-string-count.html#:~:text=Python%20count,want%20the%20search%20to%20begin.
    # https://realpython.com/python-command-line-arguments/
    # https://www.tutorialsteacher.com/python/sys-module
    # https://docs.python.org/3/library/sys.html
