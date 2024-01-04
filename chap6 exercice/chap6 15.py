def is_odd(n):
  if n % 2 != 0:
    return True
  else:
    return False

print(is_odd(5) == True)
print(is_odd(4) == False)
print(is_odd(1) == True)
print(is_odd(0) == False)
