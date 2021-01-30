import os
import time

# Die Ausgabenkonsole leeren
os.system("cls")

# Obere Grenze definieren
n = 100000

# Merke Zeitpunkt
start = time.time()

print("Suche nach Primzahlen bis %d" % (n))

# Hier ist die Idee mit Mengen und Mengenoperationen zuarbeiten.
menge = set(range(2,n+1))
liste = list(menge)

# Die While-Schleife soll beendet werden, wenn alle Vielfachen
# der aktuell untersuchten Primzahl größer n wären.
# z.B.: Untersucht man Zahlen bis 100 wird man mit 51 kein
# Vielfaches mehr finden. 2 * 51 > 100. 
stopValue = int(n/2)
cp = 2
resultList = [cp]
while cp <= stopValue:
    menge -= set(liste[cp-2::cp])
    cp = list(menge)[0]
    menge -= {cp} 
    resultList.append(cp)

resultList.extend(menge)


# wieder Zeitpunkt merken
end = time.time()
print("Die Suche hat %f Sekunden gedauert." % (end-start))

size = len(resultList)
print("Anzahl Primzahlen bis %d beträgt %d" % (n,size))
print("Die letzte Primzahl vor %d lautet %d" % (n,resultList[size-1]))
