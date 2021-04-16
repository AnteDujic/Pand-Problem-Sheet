# Program that reads in a text file
    # It outputs the number of e's in the file
# Author: Ante Dujic

# Importing sys module that allows manipulation of different parts of the Python runtime environment
import sys

# Defining file as a second argument (in the command line) = sys.argv[1]
    # First argument is current program name sys.argv[0]
myFile = sys.argv[1]                                                                

# Opening file using with open() which closes the file automatically
    # rt (read text file)
with open (myFile, "rt") as f:                                              
    data = f.read ()
    stringCount = data.count ("e")                                # counting es string
    print (stringCount)                                           # output the counted string


"""
REFERENCES:
- command line argument: https://realpython.com/python-command-line-arguments/
- sys module: https://www.tutorialsteacher.com/python/sys-module
- sys.argv[]: 
        https://www.tutorialsteacher.com/python/sys-module
        https://docs.python.org/3/library/sys.html
- with open(): https://realpython.com/read-write-files-python/
- count string: 
        https://www.w3schools.com/python/ref_string_count.asp
        https://www.guru99.com/python-string-count.html
"""