def is_kool(word):
  for letter in word:
    if letter == "k":
      return True
  return False



word = input()
word_is_kool = is_kool(word)

if word_is_kool:
  print(f"holy moly, '{word}' is cool!")
else:
  print("not cool ._.")
  
