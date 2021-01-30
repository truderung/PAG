import math

def prim_faktor_zerlegung(a):
  import math
  b = 2
  prim_liste = []
  sqrt_a = int(math.sqrt(a))
  while sqrt_a >= b:
    
    if a % b == 0:
      a = a // b
      prim_liste = prim_liste + [b]
    else:
      b = b+1
  
  return prim_liste
