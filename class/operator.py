
class Bruch():
  def __init__(self, zaehler, nenner):
      self.zaehler = zaehler
      self.nenner = nenner

  def output(self):
    print(self)

  def product(self, bruch):
    result = Bruch(self.zaehler * bruch.zaehler, self.nenner * bruch.nenner)
    return result

  def sum(self, bruch):
    result = Bruch(self.zaehler*bruch.nenner + bruch.zaehler*self.nenner, self.nenner * bruch.nenner)
    return result

  def __add__(self, other):
    return self.sum(other)

  def __mul__(self, other):
    return self.product(other)

  def __str__(self):
    return "Bruch: %d / %d" % (self.zaehler, self.nenner)


b = Bruch(1,2)
b.output()

a = Bruch(3,4)
c = b.sum(a)
c.output()

## this is possible because overriding operators
e = b + c
print(e)

print(c*e)