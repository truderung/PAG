import os
import time
import math

# Die Ausgabenkonsole leeren
os.system("cls")

# Obere Grenze definieren
n = 5000000

# Merke Zeitpunkt
start = time.time()

print("Suche nach Primzahlen bis %d" % (n))

# Wie viel bringt es, wenn mit einer Liste von Zahlen
# begonnen wird, die außer 2 keine geraden Zahlen enthält?

# Die Tatsache, dass mehrstellige Primzahlen (also > 10) nur mit 1, 3, 7 oder 9 enden können,
# erlaubt eine um 60% kleinere Initial-Menge
menge = {2,5} | set(range(3,n+1,10)) | set(range(7,n+1,10)) | set(range(9,n+1,10)) | set(range(11,n+1,10))

# Festgestellt, dass es ausreicht, lediglich das Vielfache von 
# Primzahlen bis Wurzel n (sqrt(n)) zu suchen und zu streichen.
# Das reduziert die Anzahl der notwendigen Schleifendurchläufe 
# und somit Zeit enorm.
stopValue = int(math.sqrt(n))
cp = 2
primZahlen = {2}
while cp <= stopValue:
    menge -= set(range(cp,n+1,cp))
    cp = sorted(menge)[0]
    primZahlen |= {cp}

primZahlen |= menge

# wieder Zeitpunkt merken
end = time.time()
print("Die Suche hat %f Sekunden gedauert." % (end-start))

size = len(primZahlen)
print("Anzahl Primzahlen bis %d beträgt %d" % (n,size))
print("Die letzte Primzahl vor %d lautet %d" % (n,sorted(primZahlen)[size-1]))
