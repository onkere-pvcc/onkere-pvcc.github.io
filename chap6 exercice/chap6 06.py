def days_in_month(month_name):
    # Dictionary mapping month names to the number of days
    months = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    # Check if the given month_name is in the dictionary
    if month_name in months:
        return months[month_name]
    else:
        return None

# Test cases
print(days_in_month("February"))  # Should print 28
print(days_in_month("December"))  # Should print 31
print(days_in_month("InvalidMonth"))  # Should print None
