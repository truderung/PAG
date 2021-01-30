class ListIterator():
  def __init__(self, liste = []):
    self.liste = liste
    self.n = 0
    
  def __str__(self):
    return str(self.liste)

  def next(self):
    if self.n < len(self.liste):
      result = self.liste[self.n]
      self.n += 1
      return result 
    else:
      raise StopIteration
