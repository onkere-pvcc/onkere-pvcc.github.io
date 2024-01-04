def sum_of_squares(xs):
  sum = 0
  for x in xs:
    sum += x**2
  return sum

def test(got, expected):
  if got == expected:
    print("Test passed")
  else:
    print(f"Test failed. Got {got}, expected {expected}")

print(sum_of_squares([2, 3, 4]), 29)
print(sum_of_squares([]), 0)
print(sum_of_squares([2, -3, 4]), 29)