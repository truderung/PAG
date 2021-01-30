from list_iter import *
import pytest


def test_construction():
  li = ListIterator()
  assert type(li) == ListIterator

  li = ListIterator([1,2,3,4,5,6,7])
  assert type(li) == ListIterator


def test_next():
  li = ListIterator()
  with pytest.raises(StopIteration):
    li.next()

  liste = [1,2,3,4,5,6,7]
  li = ListIterator(liste)
  assert li.next() == 1
  assert li + 1 == 1
  