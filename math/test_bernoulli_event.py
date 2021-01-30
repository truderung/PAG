from bernoulli_event import *
import pytest


# Verteilungsfunktion
def test_pdf():
  assert pdf(0,3,0.5) == 0.125
