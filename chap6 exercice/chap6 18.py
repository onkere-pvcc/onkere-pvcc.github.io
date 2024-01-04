def f2c(ftemp):
  ctemp = (ftemp - 32) * 5/9
  return round(ctemp)

print(f2c(212) == 100) # Pass
print(f2c(32) == 0) # Pass
print(f2c(-40) == -40) # Pass
print(f2c(36) == 2) # Pass
print(f2c(37) == 3) # Pass
print(f2c(38) == 3) # Pass
print(f2c(39) == 4) # Pass

