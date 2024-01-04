def c2f(ctemp):
  ftemp = ctemp * 9/5 + 32
  return round(ftemp)

print(c2f(0) == 32) # Pass
print(c2f(100) == 212) # Pass
print(c2f(-40) == -40) # Pass
print(c2f(12) == 54) # Pass
print(c2f(18) == 64) # Pass
print(c2f(-48) == -54) # Pass