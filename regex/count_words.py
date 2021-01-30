import re

def count_words(test):
  return len(re.findall(r'\S+', test))

def count_words_with(test, letter):
  res = re.findall(r'(?<=' + letter + r')\S+', test)
  print(res)
  return len(res)
