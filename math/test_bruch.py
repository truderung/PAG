from bruch import *
import pytest


def test_konstruktion():
  a = Bruch(4,8)
  assert a.zaehler == 4
  assert a.nenner == 8, "Should be 8"
  del a

  with pytest.raises(TypeError):
    Bruch([5])

  with Bruch(-1, 5) as b:
    assert b.zaehler == -1

  with Bruch(0, 5) as b:
    assert b.zaehler == 0

  with pytest.raises(TypeError):
    Bruch([2.2], 5)

  with pytest.raises(TypeError):
    Bruch(2, [5.4])

  with pytest.raises(ValueError):
    Bruch(2, 0)


def test_kuerzen():
  with Bruch(4, 7) as b:
    b.kuerzen()
    assert b == Bruch(4, 7)

  with Bruch(4, 76) as b:
    b.kuerzen()
    assert b == Bruch(1, 19)


def test_copy():
  with Bruch(3,4) as b:
    with b as a:
      assert id(a) == id(b)
      assert a is b
    with b.copy() as a:
      assert id(a) != id(b)
      assert a is not b
      assert a == b
    

def test_gleich():
  assert Bruch(1, 2) == Bruch(2, 4)
  assert (Bruch(1, 2) == Bruch(1, 4)) == False
  assert Bruch(1, -2) == Bruch(-1, 2)
  assert Bruch(1, 2) == Bruch(-1, -2)
  
  with Bruch(3, 9) as a:
    with Bruch(12, 36) as b:
      assert a == b
      assert a.zaehler == 3
      assert a.nenner == 9
      assert b.zaehler == 12
      assert b.nenner == 36


def test_ungleich():
  with Bruch(2, 5) as b:
    assert b != Bruch(3, 5)
    assert Bruch(3, 123456789012345679) != Bruch(3, 123456789012345678)


def test_summieren():
  assert Bruch(3, 4).summe(Bruch(2, 4)) == Bruch(5, 4)
  assert Bruch(3, 8).summe(Bruch(2, 4)) == Bruch(7, 8)
  assert Bruch(3, 8).summe(Bruch(1, 1)) == Bruch(11, 8)
  assert Bruch(3, 8).summe(Bruch(9, 8)) == Bruch(3, 2)

  assert Bruch(2, 4) + Bruch(3, 4) == Bruch(5, 4)
  assert Bruch(2, 4) + Bruch(3, 8) == Bruch(7, 8)
  assert Bruch(1, 1) + Bruch(3, 8) == Bruch(11, 8)
  assert Bruch(9, 8) + Bruch(3, 8) == Bruch(3, 2)

  with Bruch(3, 8) as b:
    assert b + Bruch(-1, 8) == Bruch(1, 4)
    assert b + Bruch(-5, 8) == Bruch(-1, 4)

def test_multiplizieren():
  assert Bruch(3, 4).produkt(Bruch(2, 1)) == Bruch(6, 4)
  assert Bruch(3, 4)*Bruch(2, 1) == Bruch(6, 4)


# Unit Tests Should Only Test Public Methods!
# The short answer is that you shouldn't test 
# private methods directly, but only their effects 
# on the public methods that call them. 
# Unit tests are clients of the object under test,
# much like the other classes in the code
# that are dependent on the object
def test_erweitern():
  with Bruch(8, 12) as b:
    pass
    # b.__erweitern_auf_kgV_nenner(kgv)(36)
    # assert b.zaehler == 24
    # assert b.nenner == 36


def test_subtrahieren():
  with Bruch(11, 12) as b:
    with Bruch(2, 3) as a:
      # test of __erweitern_auf_kgV_nenner is inclusive
      assert b - a == Bruch(1, 4)
      # but check also if __erweitern_auf_kgV_nenner does
      # manipulate the original data
      assert a == Bruch(2, 3)
      assert b == Bruch(11, 12)


def test_kehrwert():
  with Bruch(2, 5) as b:
    a = b.copy()
    a.kehrwert()
    assert a == Bruch(5, 2)
    assert b == Bruch(2, 5)


def test_kleiner():
  with Bruch(2, 5) as b:
    assert b < Bruch(1, 2)
    assert b < Bruch(3, 5)
    assert b < Bruch(5, 10)
    assert Bruch(3, 123456789012345679) < Bruch(3, 123456789012345678)


def test_groesser():
  with Bruch(2, 5) as b:
    assert Bruch(1, 2) > b
    assert Bruch(3, 5) > b
    assert Bruch(5, 10) > b
    assert Bruch(3, 123456789012345678) > Bruch(3, 123456789012345679)


def test_kleiner_gleich():
  with Bruch(2, 5) as b:
    assert b <= Bruch(3, 5)
    assert b <= Bruch(4, 10)
    assert b <= Bruch(8, 20)
    assert b <= Bruch(9, 20)


def test_groesser_gleich():
  with Bruch(2, 5) as b:
    assert Bruch(3, 5) >= b
    assert Bruch(4, 10) >= b
    assert Bruch(8, 20) >= b
    assert Bruch(9, 20) >= b


def test_division():
  with Bruch(2, 5) as b:
    assert (b / Bruch(2, 5)) == Bruch(1, 1)
    assert (b / Bruch(3, 4)) == Bruch(8, 15)
    assert (b / Bruch(3, 5)) == Bruch(2, 3)


################################################################################

# def test_konstruktion_integer():
#   with Bruch(5) as b:
#     assert b.zaehler == 5
#     assert b.nenner == 1
#     assert b == Bruch(5, 1)


# def test_konstruktion_bruch():
#   with Bruch(5, 22) as b:
#     with Bruch(b) as a:
#       assert a == b
#       assert id(a) != id(b)
#       assert a is not b


# def test_summe_integer():
#   with Bruch(5, 22) as b:
#     assert b + 7 == b + Bruch(7, 1)
#     assert b.summe(7) == b + Bruch(7, 1)
#     assert b - 1 == Bruch(-17, 22)
#     with pytest.raises(TypeError):
#       7 + b


# def test_subtrahieren_integer():
#   with Bruch(5, 22) as b:
#     assert b + 7 == b + Bruch(7, 1)
#     assert b.summe(7) == b + Bruch(7, 1)
    
#     with pytest.raises(TypeError):
#       7 - b
            

# # optionale Aufgaben
# def test_kein_zugriff_auf_private():
#   with Bruch(5, 22) as b:
#     with pytest.raises(AttributeError):
#       b.__type_check(b)


# def test_multiplizieren_integer():
#   with Bruch(5, 22) as b:
#     assert b * 2 == Bruch(5, 11)

#     with pytest.raises(TypeError):
#       2 * b


# def test_dividieren_integer():
#   with Bruch(5, 22) as b:
#     assert b / 2 == Bruch(5, 44)

#     with pytest.raises(TypeError):
#       2 / b

# def test_vergleichsoperatoren_integer():
#   with Bruch(8, 5) as b:
#     assert b < 2
#     assert b <= 2
#     assert b > 1
#     assert b >= 1
#     assert b - Bruch(3, 5) == 1
#     assert b - Bruch(3, 5) <= 1
#     assert b - Bruch(3, 5) >= 1


# def test_from_float():
#   with Bruch.from_float(0.1) as b:
#     assert b == Bruch(1, 10)
#     assert b.from_float(0.2) == Bruch(2/10)

#   assert Bruch.from_float(0.3) == Bruch.from_float(6/20)


# def test_konstruktion_float():
#   with Bruch(0.1) as b:
#     assert b == Bruch(1, 10)
#     assert b == Bruch(1/10)

#   assert Bruch(2.999999999999999) == Bruch(2999999999999999, 1000000000000000)
#   import math
#   assert Bruch(math.cos(pi()/3)) == Bruch(5000000000000001, 10000000000000000)