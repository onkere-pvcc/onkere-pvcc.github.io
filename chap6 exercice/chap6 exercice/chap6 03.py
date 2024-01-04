def day_num(day_name):
    days = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}

    # Check if the given day_name is in the dictionary
    if day_name in days:
        return days[day_name]
    else:
        return None

def day_name(day_num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if 0 <= day_num < len(days):
        return days[day_num]
    else:
        return None

# Test cases
print(day_num("Friday"))  # Should print 5
print(day_num("Sunday"))  # Should print 0
print(day_num(day_name(3)))  # Should print 3
print(day_name(day_num("Thursday")))  # Should print "Thursday"
print(day_num("Halloween"))  # Should print None