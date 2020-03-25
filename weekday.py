# Donal Buggy

# A program to check if today is a weekday or the weekend, and return a string depending on the result

import datetime

# datetime checks today's time/date information and stores in a variable
today = datetime.datetime.now()

# consulted W3Schools (https://www.w3schools.com/python/python_datetime.asp) to check day of the week in datetime

# if statement uses the strftime() method to check the index position of the day informstion. If it is found to be between Monday and Friday, prints the first statement. Otherwise prints the second statement

if today.strftime("%w") == "0" or today.strftime("%w") < "5":
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")
