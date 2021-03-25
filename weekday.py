# Program that outputs a different message depending if today is weekday or weekend
# Author: Ante Dujic

# Importing module datetime to work with dates as date objects
import datetime                                         

# Setting variable for current day
today = datetime.datetime.now()

# Comparing current day (1-7) to Friday (5)
    # strf.time() formats date objects
if (int ((today.strftime("%u"))) > 5):                  # "%u" = ISO 8601 weekday Mon(1) - Sun (7)
    print ("Today is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday.")

"""
REFERENCES:
- datetime module: https://www.w3schools.com/python/python_datetime.asp
- day today: https://www.programiz.com/python-programming/datetime
- strftime() formatting: https://www.w3schools.com/python/python_datetime.asp
"""