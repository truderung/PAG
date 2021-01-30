from misc import *

class Bruch():
  def __init__(self, zaehler, nenner = 1):
    if zaehler.__class__ is self.__class__:
      self.__dict__ = zaehler.__dict__.copy()
    elif zaehler.__class__ == float:
      self.__dict__ = self.from_float(zaehler).__dict__
    elif zaehler.__class__ is not int or nenner.__class__ is not int:
      raise TypeError
    elif nenner == 0:
      raise ValueError
    else:
      self.zaehler = zaehler
      self.nenner = nenner


  # ####################################################################
  #  public methods
  # ####################################################################      
  def copy(self):
    obj = type(self).__new__(self.__class__)
    obj.__dict__ = self.__dict__.copy()
    return obj


  @staticmethod
  def from_float(number):
    tmp = str(number).split(".")
    m = tmp[1]
    return Bruch(int(tmp[0])) + Bruch(int(tmp[1]), 10 ** len(m))


  def kuerzen(self):
    ggt = ggT(self.zaehler, self.nenner)
    self.zaehler //= ggt
    self.nenner //= ggt


  def ausgabe(self):
    print(self)


  def produkt(self, other):
    return self.__mul__(other)


  def summe(self, other):
    return self.__sum__(other)


  def differenz(self, other):
    return self.__sub__(other)


  def kehrwert(self):
    tmp = self.zaehler
    self.zaehler = self.nenner
    self.nenner = tmp


  # ####################################################################
  #  private
  # ####################################################################
  def __type_check(self, other):
    if other.__class__ == int or other.__class__ == float:
      return Bruch(other)
    elif self.__class__ == other.__class__:
      return other
    else:
      raise TypeError


  # ####################################################################
  #  operators
  # ####################################################################
  def __sum__(self, other):
    obj = self.__type_check(other)
    return Bruch(self.zaehler * obj.nenner + obj.zaehler * self.nenner, self.nenner * obj.nenner)


  def __sub__(self, other):
    obj = self.__type_check(other)
    if self.nenner != obj.nenner:
      kgv = kgV(self.nenner, obj.nenner)
      a = self.copy()
      a.__erweitern_auf_kgV_nenner(kgv)
      b = obj.copy()
      b.__erweitern_auf_kgV_nenner(kgv)
      return a - b
    return Bruch(self.zaehler-obj.zaehler, self.nenner)


  def __add__(self, other):
    return self.__sum__(other)


  def __mul__(self, other):
    obj = self.__type_check(other)
    return Bruch(self.zaehler * obj.zaehler, self.nenner * obj.nenner)


  def __truediv__(self, other):
    obj = self.__type_check(other)
    b = obj.copy()
    b.kehrwert()
    obj = self * b
    obj.kuerzen()
    return obj

  def __str__(self):
    return "Bruch: %d / %d" % (self.zaehler, self.nenner)


  def __eq__(self, other):
    obj = self.__type_check(other)
    a = self.copy()
    b = obj.copy()
    a.kuerzen()
    b.kuerzen()
    return a.zaehler == b.zaehler and a.nenner == b.nenner


  def __lt__(self, other):
    obj = self.__type_check(other)
    return self.zaehler * obj.nenner < obj.zaehler * self.nenner


  def __gt__(self, other):
    obj = self.__type_check(other)
    return self.zaehler * obj.nenner > obj.zaehler * self.nenner
    

  def __ne__(self, other):
    return not (self == other)    


  def __ge__(self, other):
    return self > other or self == other


  def __le__(self, other):
    return self < other or self == other


  def __enter__(self):
    return self
  

  def __exit__(self, type, value, traceback):
    pass


  # ####################################################################
  #  private methods
  # ####################################################################
  def __erweitern_auf_kgV_nenner(self, _kgV):
    f = _kgV // self.nenner
    newObj = self * Bruch(f, f)
    self.__dict__.update(newObj.__dict__)    
