from tier import *

class Katze(Tier):
  def __init__(self, name):
    super().__init__(name)
    
  def laut_machen(self):
    return "miau"

  def name_sagen(self):
    return self.laut_machen()