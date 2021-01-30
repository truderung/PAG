from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..', '..', '..'))

from benchmark import Bench

m = 30000

################  delete from list  ############################
def test_list_delete_top():
  liste = list(range(1,m+1))
  
  with Bench():
    for i in range(1,m+1):
        liste.remove(i)
  assert liste == []


def test_list_delete_back():
  liste = list(range(1,m+1))
  umgekehrteListe = reversed(liste)

  with Bench():
    # Hier wird ein worst case (der ungünstigste Fall) erzeugt,
    # in dem aus der liste das hinterste Elemente zuerst gelöscht wird,
    # bis die Liste leer ist. 
    for i in umgekehrteListe:
      liste.remove(i)
  assert liste == []


def test_list_delete_back_slice():
  liste = list(range(1,m+1))
  umgekehrteListe = reversed(liste)

  with Bench():
    # Hier wird ein worst case (der ungünstigste Fall) erzeugt,
    # in dem aus der liste das hinterste Elemente zuerst gelöscht wird,
    # bis die Liste leer ist. 
    for i in umgekehrteListe:
      liste = liste[:i-1]
    assert liste == []

