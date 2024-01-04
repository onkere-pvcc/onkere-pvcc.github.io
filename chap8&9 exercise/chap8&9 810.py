def reverse(text):
  return text[::-1]

def is_palindrome(text):
  return text == reverse(text)

import testsuite

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))