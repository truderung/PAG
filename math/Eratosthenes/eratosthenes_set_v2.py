import os
import time

# Die Ausgabenkonsole leeren
os.system("cls")

# Obere Grenze definieren
n = 100000

# Merke Zeitpunkt
start = time.time()

print("Suche nach Primzahlen bis %d" % (n))

# Bringt es eine Zeitersparnis, wenn mit einer Liste von Zahlen
# begonnen wird, die außer 2 keine geraden Zahlen enthält?

menge = set(range(3,n+1,2))
liste = [2] + list(menge)

stopValue = int(n/2)
cp = 3
resultList = [2, cp]
while cp <= stopValue:
    menge -= set(liste[int(cp/2)::cp])
    cp = list(menge)[0]
    menge -= {cp}
    resultList += [cp]

resultList.extend(menge)


# wieder Zeitpunkt merken
end = time.time()
print("Die Suche hat %f Sekunden gedauert." % (end-start))

size = len(liste)
print("Anzahl Primzahlen bis %d beträgt %d" % (n,size))
print("Die letzte Primzahl vor %d lautet %d" % (n,liste[size-1]))
