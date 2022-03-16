import random

class RandomIter():
  def __init__(self, liste = []):
    self.liste = liste
    
  def __next__(self):
    return random.choice(self.liste)
