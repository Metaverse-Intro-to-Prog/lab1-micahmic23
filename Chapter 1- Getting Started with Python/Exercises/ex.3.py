#Exercise 3: Print date and Time 
#Write a Python program to display the current date and time.

import datetime
now = datetime.datetime.now()
print("Date and Time now:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

