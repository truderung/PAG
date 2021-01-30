import os
import time

# Die Ausgabenkonsole leeren
os.system("cls")

# Obere Grenze definieren
n = 100000

# Merke Zeitpunkt
start = time.time()

print("Suche nach Primzahlen bis %d" % (n))

# Liste mit [2] und allen ungeraden Zahlen (ab 3 in 2er Schritten, 3,5,7,9,11,...)
liste = [2] + list(range(3,n+1,2))

# current index: die Stelle in der Liste, die aktuell bearbeitet wird
ci = 1

# neue Liste erstellen, die alle Zahlen aufnimmt,
# die noch behalten werden sollen
# hier die ersten 2 Elemente, also 2 und 3
newList = liste[:ci+1]

# mache Schleife, solange ci nicht das Ende der Liste erreicht hat
while ci < len(liste):
    # current prime: aktuelle Primzahl
    cp = liste[ci]
    for x in liste[ci+1:]: # gehe alle Elemente ab ci durch
        if x % cp:
            newList.append(x) # behalte nur die Zahlen, die kein Vielfaches von cp sind

    # verwerfe die alte Liste und setze neue Liste als aktuelle Liste ein
    liste = newList
    ci += 1 # rücke ci eins weiter
    newList = liste[:ci+1] # belade newList wieder mit den Elementen, die bereits bearbeitet sind

# wieder Zeitpunkt merken
end = time.time()
print("Die Suche hat %f Sekunden gedauert." % (end-start))

size = len(liste)
print("Anzahl Primzahlen bis %d beträgt %d" % (n,size))
print("Die letzte Primzahl vor %d lautet %d" % (n,liste[size-1]))
