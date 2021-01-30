import os
import time

# Die Ausgabenkonsole leeren
os.system("cls")

# Obere Grenze definieren
n = 50000

# Merke Zeitpunkt
start = time.time()

print("%d Elemente aus der Liste löschen" % (n))

liste = list(range(1,n+1))
umgekehrteListe = reversed(liste)

# Hier wird ein worst case (der ungünstigste Fall) erzeugt,
# in dem aus der liste das hinterste Elemente zuerst gelöscht wird,
# bis die Liste leer ist. 
for i in umgekehrteListe:
    liste.remove(i)

# wieder Zeitpunkt merken
end = time.time()

print("Die Verarbeitung hat %f Sekunden gedauert." % (end-start))
