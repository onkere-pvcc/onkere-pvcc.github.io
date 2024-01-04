def turn_clockwise(direction):
  if direction == "N":
    return "E"
  elif direction == "E":
    return "S"
  elif direction == "S":
    return "W"
  elif direction == "W":
    return "N"
  else:
    return None

print(turn_clockwise("N") == "E") # Pass
print(turn_clockwise("W") == "N") # Pass
print(turn_clockwise(42) == None) # Pass
print(turn_clockwise("rubbish") == None) # Pass