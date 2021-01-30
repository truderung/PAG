from misc import *
import pytest

def test_ggT():
    assert ggT(8, 12) == 4
    assert ggT(8, 7) == 1
    assert ggT(-8, 7) == -1
    assert ggT(8, 0) == 8

def test_kgV():
    assert kgV(12, 18) == 36
    assert kgV(3, 6) == 6
    assert kgV(5, 1) == 5
    assert kgV(15, 0) == 0

def test_product():
  a = [3,4,5]
  assert product(a) == 60
  assert product([0]) == 0

  with pytest.raises(ValueError):
    product([])
  
  