#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      adius
#
# Created:     03/09/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Prompt the user for input
hour = input("Enter the hour: ")
minutes = input("Enter the minutes: ")
am_pm = input("Enter AM or PM: ")

# Concatenate the inputs into a single string variable
time_str = hour + ":" + minutes + " " + am_pm

# Print the formatted time
print(time_str)
