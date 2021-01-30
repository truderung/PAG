from misc import *


def calc_umfang(durchmesser):
  return durchmesser*pi()


class Kreis():
  def __init__(self, radius):
    self.radius = radius
    self.durchmesser = 2*radius
    self.umfang = calc_umfang(2*radius)


k = Kreis(4)
j = Kreis(2)

print(k.umfang)
print(j.umfang)