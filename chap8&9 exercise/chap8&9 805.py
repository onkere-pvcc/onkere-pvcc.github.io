text = """The only thing we have to fear is fear itself - nameless, unreasoning, unjustified terror which paralyzes needed efforts to convert retreat into advance."""

def analyze_text(text):
  text = text.replace('.', '') # Remove punctuation
  words = text.split()
  num_words = len(words)

  num_e_words = 0
  for word in words:
    if 'e' in word:
      num_e_words += 1

  print(f"Your text contains {num_words} words, of which {num_e_words} ({num_e_words/num_words:.1%}) contain an 'e'.")

analyze_text(text)