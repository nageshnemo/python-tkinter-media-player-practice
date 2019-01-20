# write an app containing a button and as soon as Button is clicked it should display the current date and time in a label
# in python we have a module called datetine
# this module contains a class called datetime
# this class contains class method now() which returns current date and time


"""
from datetime import *
today = datetime.now()
print(today)

"""
# strftime function
from datetime import *
today = datetime.now()
day = today.strftime("%d")
month = today.strftime("%b")
year = today.strftime("%y")
print(day)
print(month)
print(year)
