# Program that outputs a different message depending if today is weekday or weekend
# Author: Ante Dujic

import datetime                                         # https://www.w3schools.com/python/python_datetime.asp

today = datetime.datetime.now()

if (int ((today.strftime("%u"))) > 5):                  # "%u" = ISO 8601 weekday Mon(1) - Sun (7)
    print ("Today is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday.")