import random, copy

class RandomShrinkIter():
  def __init__(self, liste = []):
    self.liste = copy.deepcopy(liste)
    
  def __next__(self):
    if len(self.liste) > 0:
      random.shuffle(self.liste)
      return self.liste.pop()
    else:
      raise StopIteration
