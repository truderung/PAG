from tier import *

class Papagei(Tier):
  def __init__(self, name):
    super().__init__(name)
    
  def laut_machen(self):
    return "krächz"

  def name_sagen(self):
    return self.name

  def fliegen(self):
    return "fly, fly, bird"
