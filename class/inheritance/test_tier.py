from tier import *
from hund import *
from katze import *
from papagei import *
import pytest


def test_tier_construction():
  with pytest.raises(NotImplementedError):
    Tier("Bello")
  with pytest.raises(NotImplementedError):
    Tier("Bello").name_sagen()
  with pytest.raises(NotImplementedError):
    Tier("Bello").laut_machen()

def test_hund_construction():
  tier = Hund("Bello")
  assert tier.name_sagen() == "wuff"
  assert tier.laut_machen() == "wuff"
  assert tier.name == "Bello"

