from misc import product
from factorization import *
import pytest

def test_prim_faktor_probedivision():
  a = [2,3,5,7,11,13,17,19,23,59]
  assert a == prim_faktor_zerlegung(product(a))
