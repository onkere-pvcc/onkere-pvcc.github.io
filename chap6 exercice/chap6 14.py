def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False

print(is_even(4) == True)
print(is_even(5) == False)
print(is_even(0) == True)
print(is_even(-2) == True)
print(is_even(7) == False)