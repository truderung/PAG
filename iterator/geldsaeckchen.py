import copy

# Elternklasse
class Muenze():
  def __init__(self, wert):
    self.value = wert

  def gib_wert(self):
    return round(self.value, 2)

# Spezialisierungen / Ableitungen / Vererbungen
class Cent1(Muenze):
  def __init__(self):
    super().__init__(0.01)

class Cent50(Muenze):
  def __init__(self):
    super().__init__(0.5)

class Euro1(Muenze):
  def __init__(self):
    super().__init__(1)

class Euro2(Muenze):
  def __init__(self):
    super().__init__(2)


# Klasse Geldsaeckchen kann Instanzen der Klasse
# Münzen aufnehmen
class Geldsaeckchen():
  def __init__(self):
    self.muenzen = set()
  
  def add(self, muenze):
    if isinstance(muenze, Muenze):
      self.muenzen.add(muenze)
    else:
      raise TypeError

  def ist_vorhanden(self, muenze):
    for i in self.muenzen:
      if muenze.gib_wert() == i.gib_wert():
        return True
    return False

  def add_gehalt(self):
    g = {Cent1(),Cent1(),Cent1(),Cent1(),Cent1(),Euro1(),Euro1(),Euro1(),Euro1(),Euro1(), \
        Euro2(),Euro2(),Euro2(),Euro2(),Euro2(),Cent50(),Cent50(),Cent50(),Cent50(),Cent50()}
    self.muenzen = self.muenzen.union(g)

  def summe(self):
    sum = 0
    for i in self.muenzen:
      sum += i.gib_wert()
    return round(sum, 2)
  
  def count(self):
    return len(self.muenzen)

  def __iter__(self):
    self.iter_set = copy.deepcopy(self.muenzen)
    return self

  def __next__(self):
    if len(self.iter_set) == 0:
      raise StopIteration

    return self.iter_set.pop()