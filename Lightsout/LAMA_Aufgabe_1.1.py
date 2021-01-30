import random


def matrixprint (lightout):
  for i in lightout:
    print(i)

    
    
def eingabe (size):
  sp, zl= input("gib bitte spalte und zeile ein: ").split(',')
  
  if not zl.isdigit() or not sp.isdigit() or (int(zl)>size-1 or int(zl)<0 or int(sp)<0 or int(sp)>size-1):
   return eingabe(size)
  else:
    return int(sp), int(zl)
    
    
def spielzug (sp, zl):
  if lightout[zl][sp]:
    lightout[zl][sp] = 0
  else:
    lightout[zl][sp] = 1
  return None

    
###########################################################################
############################# start vom Programm ##########################
###########################################################################

import os


size = 5

lightout = [ [0]*size for i in range(size)]

for i in range (0,size):
    for j in range(0,size):
        lightout[i][j] = random.randint(0,1)


while sum(sum(lightout,[])) > 0:
  os.system("cls")
  
  matrixprint(lightout)
  sp, zl = eingabe(size)

  spielzug(sp, zl)  # die gewählte Lampe
  
  if sp > 0:
    spielzug(sp-1, zl) # nach links

  if sp < size-1:  
    spielzug(sp+1,zl) # nach rechts
  
  if zl > 0:
    spielzug(sp,zl-1) # nach oben
  
  if zl < size-1:
    spielzug(sp,zl+1) # nach unten


print("toll, du hast gewonnen!")








