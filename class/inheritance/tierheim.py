from tier import *

class TierHeim():
  def __init__(self, kapazitaet):
    self.zellen = ["" for _ in range(kapazitaet)]

  def ist_noch_platz(self):
    return len(self.zellen) != len(list(filter(None, self.zellen)))

  def tier_abgeben(self, tier):
    if not self.ist_noch_platz():
      raise Exception("Tierheim überfüllt")

    print("Prozedur: %s wird untersucht, geimpft, gechipt, und ggf. kastriert." % (type(tier)))
    self.zellen[self.find_empty_cell()] = tier

  def tier_sehen(self, zellennummer):
    tier = self.zellen[zellennummer]
    if tier == "":
      raise Exception("Zelle ist unbesetzt")

    print(tier.laut_machen())
    print(tier.name_sagen())
    print(type(tier))

    return tier

  def find_empty_cell(self):
    for i in range(len(self.zellen)):
      if self.zellen[i] == "":
        return i