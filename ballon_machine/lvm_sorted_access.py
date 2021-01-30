from data_input import *
from operator import itemgetter
#from search_algorithm.binary_search import *
import os
import time

os.system("cls")


stream = line_to_list(line3)
opt_count = sum(stream) // 20
opt_rest = sum(stream) % 20
fach_reihe = [0,0,0,0,0,0,0,0,0,0]
ausgabe_fach = 0
anz_pakete = 0
verpackte_ballons = 0
anz_iter = 0

# how to import as package ###########
def binary_search(liste, gesucht):
    start = 0
    ende = len(liste) - 1

    while start <= ende:
        mitte = (start + ende)//2

        if liste[mitte] == gesucht:
            return mitte
        elif liste[mitte] < gesucht:
            start = mitte+1
        else:
            ende = mitte-1

    return -1
#################################

def take_next():
  if len(stream) > 0:
    return stream.pop(0)
  else:
    return 0

def fach(i):
  global ausgabe_fach, fach_reihe
  ausgabe_fach += fach_reihe[i]
  fach_reihe[i] = take_next()

def verpacken():
  global ausgabe_fach, anz_pakete, verpackte_ballons
  anz_pakete += 1
  verpackte_ballons += ausgabe_fach
  ausgabe_fach = 0

def remove_items_from_list(src_list, item_list):
  for i in item_list:
    try:
      src_list.remove(i)
    except ValueError:
      pass  # do nothing!
  return src_list

def __internal_search(liste, x):
  global anz_iter

  if x <= 0:
    return None

  anz_iter += 1
  
  result = binary_search(list(zip(*liste))[1], x)
  if result == -1:
    a = x//2
    b = -(-x//2) 
    
    org_liste = liste.copy()
    while a > 0:
      res_a = __internal_search(liste, a)
      if res_a == None:
        a -= 1
        b += 1
        liste = org_liste.copy()
      else:
        res_b = __internal_search(remove_items_from_list(liste, res_a), b)
        if res_b == None:
          a -= 1
          b += 1
          liste = org_liste.copy()
        else:
          return res_a + res_b
    
    return None
  else:
    return [liste[result]]

def suche_summanden(liste, value):
  liste = sorted(enumerate(liste.copy()), key = itemgetter(1))
  result = __internal_search(liste, value)
  if result == None:
    return None
  else:
    return list(list(zip(*result))[0])
  
# core mechanism
# fillup the initiate state
for i in range(10):
  fach(i)

start = time.time()

### start algorithm #######################################

such_wert = 20
while sum(fach_reihe) >= 20:
  folge = suche_summanden(fach_reihe, such_wert)

  if type(folge) is list:
    for i in folge:
      fach(i)

    for i in range(len(fach_reihe)):
      if fach_reihe[i] == 0:
        fach(i)
        
    verpacken()
    such_wert = 20
  else:
    such_wert += 1


###########################################################


end = time.time()

print("Anzahl Pakete: %d" % (anz_pakete))
print("Verpackte Ballons: %d" % (verpackte_ballons))
print("Verbleibender Rest in Schalen: %s, Restsumme %d" % (str(fach_reihe), sum(fach_reihe)))
print("")
print("Dauer: %f Sekunden" % (end-start))
print("Anzahl der Iterationen: %d" % (anz_iter))
print("")
print("Optimale Anzahl Pakete: %d" % (opt_count))
print("Optimale Restsumme: %d" % (opt_rest))
