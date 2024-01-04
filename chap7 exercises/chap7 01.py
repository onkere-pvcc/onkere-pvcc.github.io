def count_odd_numbers(nums):
  count = 0
  for num in nums:
    if num % 2 != 0:
      count += 1
  return count
nums = [1, 2, 3, 4, 5]
print(count_odd_numbers(nums)) # Prints 3