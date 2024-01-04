#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      adius
#
# Created:     18/09/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def get_day_name(day_number):
    if day_number == 0:
        return "Sunday"
    elif day_number == 1:
        return "Monday"
    elif day_number == 2:
        return "Tuesday"
    elif day_number == 3:
        return "Wednesday"
    elif day_number == 4:
        return "Thursday"
    elif day_number == 5:
        return "Friday"
    elif day_number == 6:
        return "Saturday"
    else:
        return "Invalid day number"


day_number =2
day_name = get_day_name(day_number)
print("Day name:", day_name)
