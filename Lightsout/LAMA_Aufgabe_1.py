import random


def matrixprint (lightout):
  for i in range (0,len(lightout)):
    print (lightout[i][:])
    
    
def eingabe (size):
  sp, zl= input("gib bitte spalte und zeile ein: ").split(',' or ' ' or '.' )
  
  if not zl.isdigit() or not sp.isdigit() or (int(zl)>size-1 or int(zl)<0 or int(sp)<0 or int(sp)>size-1):
   return eingabe(size)
  else:
    return int(sp), int(zl)
    
    
def spielzug (sp, zl, size):
  if zl>size-1 or sp>size-1:
    return None
  if lightout[sp][zl]==1:
    lightout[sp][zl]= lightout[sp][zl]=0
  elif lightout[sp][zl]==0:
    lightout[sp][zl]= lightout[sp][zl]=1
  return None

    
###########################################################################
############################# start vom Programm ##########################
###########################################################################


size = 5

lightout = [ [0]*size for i in range(0,size)]


for i in range (0,size):
    for j in range(0,size):
        lightout[i][j] = random.randint(0,1)

matrixprint(lightout)
  
while sum(sum(lightout,[])) > 0:  

  zl, sp = eingabe(size)

  spielzug(sp, zl, size)
  spielzug(sp-1,zl, size)
  spielzug(sp+1,zl, size)
  spielzug(sp,zl-1, size)
  spielzug(sp,zl+1, size)

  matrixprint(lightout)
  
print("toll, du hast gewonnen!")








