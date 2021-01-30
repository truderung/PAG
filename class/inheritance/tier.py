
class Tier():
  def __init__(self, name):
    self.name = name

  def laut_machen(self):
    raise NotImplementedError

  def name_sagen(self):
    raise NotImplementedError
