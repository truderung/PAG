from tierheim import *
from tier import *
from hund import *
from papagei import *
from katze import *
import pytest


def test_tierheim_construction():
  TierHeim(5)

def test_ist_platz():
  heim = TierHeim(5)
  assert heim.ist_noch_platz()

def test_tier_abgeben():
  heim = TierHeim(5)

  tier = Hund("Bello")
  heim.tier_abgeben(tier)

  heim.tier_abgeben(Katze("Susi"))
  heim.tier_abgeben(Papagei("Paul"))

def test_heim_ueberfuellt():
  heim = TierHeim(5)

  tier = Hund("Bello")
  heim.tier_abgeben(tier)

  heim.tier_abgeben(Katze("Susi"))
  heim.tier_abgeben(Hund("Strolch"))
  heim.tier_abgeben(Papagei("Paul"))
  heim.tier_abgeben(Papagei("Minni"))
  with pytest.raises(Exception):
    heim.tier_abgeben(Papagei("Troll"))

def test_tier_sehen():
  heim = TierHeim(5)

  tier = Hund("Bello")
  heim.tier_abgeben(tier)

  assert heim.tier_sehen(0) == tier

  heim.tier_abgeben(Katze("Susi"))
  heim.tier_abgeben(Hund("Strolch"))
  heim.tier_abgeben(Papagei("Paul"))
  heim.tier_abgeben(Papagei("Minni"))

  for i in range(5):
    heim.tier_sehen(i)
