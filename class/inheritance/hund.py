from tier import *

class Hund(Tier):
  def __init__(self, name):
    super().__init__(name)
    
  def laut_machen(self):
    return "wuff"

  def name_sagen(self):
    return "wuff"