def sum_upto_first_even(nums):
  sum = 0
  for num in nums:
    if num % 2 == 0:
      break
    sum += num
  return sum

import unittest

class Test(unittest.TestCase):

  def test_typical_case(self):
    nums = [1, 3, 5, 2, 4, 6]
    result = sum_upto_first_even(nums)
    self.assertEqual(result, 9)

  def test_no_even_number(self):
    nums = [1, 3, 5, 7, 9]
    result = sum_upto_first_even(nums)
    self.assertEqual(result, 15)

  def test_even_number_at_start(self):
    nums = [2, 3, 5, 7, 9]
    result = sum_upto_first_even(nums)
    self.assertEqual(result, 0)

if __name__ == '__main__':
  unittest.main()