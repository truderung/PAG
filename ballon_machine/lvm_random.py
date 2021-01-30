from data_input import *
import os
import time

os.system("cls")


stream = line_to_list(line5)
opt_count = sum(stream) // 20
opt_rest = sum(stream) % 20
fach_reihe = [0,0,0,0,0,0,0,0,0,0]
ausgabe_fach = 0
anz_pakete = 0
verpackte_ballons = 0

def take_next():
  global stream
  if len(stream) > 0:
    return stream.pop(0)
  else:
    return 0

def fach(n):
  global ausgabe_fach, fach_reihe
  ausgabe_fach += fach_reihe[n]
  fach_reihe[n] = take_next()

def verpacken():
  global ausgabe_fach, anz_pakete, verpackte_ballons
  anz_pakete += 1
  verpackte_ballons += ausgabe_fach
  ausgabe_fach = 0


# core mechanism
# fillup the initiate state
for i in range(10):
  fach(i)


# start run
import random
anz_iter = 0

start = time.time()

try:
  if sum(fach_reihe) < 20:
    raise Exception('There is no Solution with init setup')

  while sum(fach_reihe) >= 20:
    res = 0
    zahl_stack = []
    rand_stack = list(range(10))  
    random.shuffle(rand_stack)
    anz_iter += 1  
    while res < 20 and len(rand_stack) > 0:
      zahl = rand_stack.pop()
      zahl_stack += [zahl]
      res += fach_reihe[zahl]

    if res == 20:
      for n in zahl_stack:
        fach(n)
      
      for i in range(len(fach_reihe)):
        if fach_reihe[i] == 0:
          fach(i)
                  
      verpacken()
    elif anz_iter > 10000:
      if res > 20:
        for n in zahl_stack:
          fach(n)
        verpacken()
      else:
        raise Exception('No Solution. Try again.')

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

except Exception as error:
    print(repr(error))
    