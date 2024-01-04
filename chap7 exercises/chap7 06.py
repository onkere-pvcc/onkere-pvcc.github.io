def count_words_until_sam(words):
  count = 0
  for word in words:
    count += 1
    if word == "sam":
      break
  return count

import unittest

class Test(unittest.TestCase):

  def test_typical_case(self):
    words = ["a", "b", "c", "d", "sam", "e", "f"]
    result = count_words_until_sam(words)
    self.assertEqual(result, 4)

  def test_sam_not_found(self):
    words = ["a", "b", "c", "d", "e", "f"]
    result = count_words_until_sam(words)
    self.assertEqual(result, 6)

  def test_sam_at_start(self):
    words = ["sam", "b", "c", "d"]
    result = count_words_until_sam(words)
    self.assertEqual(result, 1)

if __name__ == '__main__':
  unittest.main()