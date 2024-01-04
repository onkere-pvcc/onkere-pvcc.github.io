def count_words_length_5(words):
  count = 0
  for word in words:
    if len(word) == 5:
      count += 1
  return count
words = ["apple", "banana", "mango", "cherry", "orange"]
print(count_words_length_5(words)) # Prints 2