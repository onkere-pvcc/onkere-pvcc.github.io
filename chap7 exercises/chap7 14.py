def num_digits(n):
  if n == 0:
    return 1

  if n < 0:
    n = abs(n)

  digits = 0
  while n > 0:
    digits += 1
    n //= 10
  return digits

def test(got, expected):
  if got == expected:
    print("Test passed")
  else:
    print("Test failed. Got {}, expected {}".format(got, expected))

print(num_digits(0), 1)
print(num_digits(-12345), 5)