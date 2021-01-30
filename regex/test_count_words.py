import pytest
from count_words import *
from input_text import *


def test_count_words_simple():
  assert 5 == count_words("Ich denke es sind fünf.")
  assert 10 == count_words(text_0)


def test_count_words_with_e():
  assert 2 == count_words_with("Ich denke es sind fünf.", "e")
  assert 3 == count_words_with(text_0, "e")


def test_count_words_manual():
  # b = text_1
  new_text = text_1.strip().replace("\t", " ").replace("\n", " ")
  a_old = len(new_text)+1
  while len(new_text) < a_old:
    a_old = len(new_text)
    new_text = new_text.replace("  ", " ")
    
  print(new_text.split(" "))
  assert 86-1 == len(new_text.split(" "))


def test_count_words():
  assert 86-1 == count_words(text_1)

