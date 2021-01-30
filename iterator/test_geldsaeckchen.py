from geldsaeckchen import *
import pytest


def test_construction_muenze():
  m = Cent1()
  assert type(m) == Cent1
  assert isinstance(m, Cent1)
  assert isinstance(m, Muenze)


def test_construction():
  s = Geldsaeckchen()
  assert type(s) == Geldsaeckchen


def test_add():
  s = Geldsaeckchen()
  
  with pytest.raises(TypeError):
    s.add(5)

  try:
    s.add(Euro1())
  except:
    pytest.fail("Unexpected Error ..")


def test_add_and_count():
  s = Geldsaeckchen()
  assert s.count() == 0
  s.add(Cent1())
  assert s.count() == 1 
  s.add(Cent1())
  assert s.count() == 2


def test_ist_vorhanden():
  s = Geldsaeckchen()
  assert s.ist_vorhanden(Cent1()) == False
  s.add(Cent1())
  assert s.ist_vorhanden(Cent1()) == True
  s.add(Euro1())
  assert s.ist_vorhanden(Euro1()) == True


def test_sum():
  s = Geldsaeckchen()
  assert s.summe() == 0

  s.add(Cent1())
  s.add(Cent1())
  assert s.summe() == 0.02

  s.add_gehalt()
  assert s.summe() == 0.02 + 17.55


def test_iterator():
  s = Geldsaeckchen()

  s.add(Cent1())
  s.add(Cent50())
  s.add(Euro1())
  s.add(Euro2())

  si = iter(s)

  sum = s.summe()
  for _ in range(0, s.count()):
    new_val = next(s)
    sum -= new_val.gib_wert()
    assert s.ist_vorhanden(new_val)
  assert round(sum, 2) == 0