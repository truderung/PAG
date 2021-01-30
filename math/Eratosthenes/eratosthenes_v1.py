import os
import time

# Die Ausgabenkonsole leeren
os.system("cls")

# Obere Grenze definieren
n = 10000000

# Merke Zeitpunkt
start = time.time()

print("%d Elemente in eine Liste einfügen mit dem Befehl append" % (n))

# Neue Liste erzeugen
liste = []

# Die Liste um jeweils ein Element erweitern
for i in range(1,n+1):
    liste.append(i)

# wieder Zeitpunkt merken
end = time.time()

print("Die Verarbeitung hat %f Sekunden gedauert." % (end-start))

# Zum Vergleich Liste erstellen mit Range
print("")


# Merke Zeitpunkt
start = time.time()

print("%d Elemente in eine Liste einfügen mit dem Befehl range" % (n))

# Neue Liste erzeugen
liste = list(range(1,n+1))

# wieder Zeitpunkt merken
end = time.time()

print("Die Verarbeitung hat %f Sekunden gedauert." % (end-start))
