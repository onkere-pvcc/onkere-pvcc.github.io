def sum_even_numbers(nums):
  sum = 0
  for num in nums:
    if num % 2 == 0:
      sum += num
  return sum
nums = [1, 2, 3, 4, 5, 6]
print(sum_even_numbers(nums)) # Prints 12