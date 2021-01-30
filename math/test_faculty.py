from faculty import faculty as f
import pytest


def test_faculty_error():
  with pytest.raises(ValueError):
    f(-1)
  with pytest.raises(ValueError):
    f(-51)
  with pytest.raises(ValueError):
    f(-0.0000000000000000000000000001)

def test_faculty():
  assert f(0) == 1
  assert f(1) == 1
  assert f(2) == 2
  assert f(3) == 6
  assert f(4) == 24
  assert f(14) == 87178291200
