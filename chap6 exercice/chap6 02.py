def day_name(day):
  days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

  if day >= 0 and day <= 6:
    return days[day]
  else:
    return None

print(day_name(3) == "Wednesday") # Pass
print(day_name(6) == "Saturday") # Pass
print(day_name(42) == None) # Pass