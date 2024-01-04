def num_even_digits(n):
  num_evens = 0
  while n > 0:
    digit = n % 10
    if digit % 2 == 0:
      num_evens += 1
    n = n // 10
  return num_evens

def test(got, expected):
  if got == expected:
    print("Test passed")
  else:
    print(f"Test failed. Got {got}, expected {expected}")

print(num_even_digits(123456), 3)
print(num_even_digits(2468), 4)
print(num_even_digits(1357), 0)
print(num_even_digits(0), 1)