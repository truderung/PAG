import copy


class PGMImage():
  def __init__(self, data = [], size = (0, 0)):
    self.data = data
    if self.data != [] and size == (0, 0):
      self.height = len(self.data)
      if self.height > 0:
        self.width = len(self.data[0])
      else:
        self.width = 0
    else:
      self.width, self.height = size

    self.size = self.width, self.height

  def copy(self):
    return self.__copy__()

  def deepcopy(self, memo=None):
    return self.__deepcopy__(memo)

  def __copy__(self):
    return PGMImage(self.data, self.size)

  def __deepcopy__(self, memo):
    return PGMImage(copy.deepcopy(self.data), copy.deepcopy(self.size))
 
  def __iter__(self):
    return iter(self.data)

  def __getitem__(self, idx):
    return self.data[idx]

  def __setitem__(self, idx, value):
    self.data[idx] = value

  def normalize(self, min_value = 0, max_value = 255):
    image_min_value = self.min_value()
    step = (self.max_value()-image_min_value)/(max_value-min_value)
    for i in range(self.height):
      self.data[i] = [round((e-image_min_value)/step+min_value) for e in self.data[i]]

  def max_value(self):
    max_val = -float('Inf')
    for line in self.data:
      max_val = max(max_val, max(line))
    return max_val

  def min_value(self):
    min_val = float('Inf')
    for line in self.data:
      min_val = min(min_val, min(line))
    return min_val
