def sum_negative_numbers(nums):
  sum = 0
  for num in nums:
    if num < 0:
      sum += num
  return sum
nums = [1, -2, 3, -4, 5]
print(sum_negative_numbers(nums)) # Prints -6