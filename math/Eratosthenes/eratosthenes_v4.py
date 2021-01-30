import os
import time

# Die Ausgabenkonsole leeren
os.system("cls")

# Obere Grenze definieren
n = 100000

# Merke Zeitpunkt
start = time.time()

print("Suche nach Primzahlen bis %d" % (n))

liste = [2] + list(range(3,n+1,2))

# Die kompakte Schreibweise der inneren Forschleife erlaubt
# das Vermeiden der zusätzlichen Hilfsliste newList.
ci = 1 # current index
while ci < len(liste):
    cp = liste[ci] # current prime
    liste = liste[:ci+1] + [x for x in liste[ci+1:] if x % cp]
    ci += 1


# wieder Zeitpunkt merken
end = time.time()
print("Die Suche hat %f Sekunden gedauert." % (end-start))

size = len(liste)
print("Anzahl Primzahlen bis %d beträgt %d" % (n,size))
print("Die letzte Primzahl vor %d lautet %d" % (n,liste[size-1]))
