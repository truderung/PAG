import random


def matrixprint (lightout):
  for i in lightout:
    print(i)

    
    
def eingabe (width, height):
  sp, zl = input("gib bitte spalte und zeile ein: ").split(',')
  
  if not zl.isdigit() or not sp.isdigit() or (int(zl)>height-1 or int(zl)<0 or int(sp)<0 or int(sp)>width-1):
   return eingabe(width, height)
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

os.system("cls")
  
width, height = input("Willkommen bei LigthsOut! Bitte gebe Breite und Höhe deines Spielfeldes ein (komma-getrennt): ").split(',')
width = int(width)
height = int(height)

lightout = [ [0]*width for i in range(height)]

for i in range (0,height):
    for j in range(0,width):
        lightout[i][j] = random.randint(0,1)


while sum(sum(lightout,[])) > 0:
  os.system("cls")
  
  matrixprint(lightout)
  sp, zl = eingabe(width, height)

  spielzug(sp, zl)  # die gewählte Lampe
  
  if sp > 0:
    spielzug(sp-1, zl) # nach links

  if sp < width-1:  
    spielzug(sp+1,zl) # nach rechts
  
  if zl > 0:
    spielzug(sp,zl-1) # nach oben
  
  if zl < height-1:
    spielzug(sp,zl+1) # nach unten


print("toll, du hast gewonnen!")








