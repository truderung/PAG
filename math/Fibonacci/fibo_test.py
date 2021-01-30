import os
import time
from fibonacci_v1 import fibo
from fibonacci_v2 import fibo2

# Die Ausgabenkonsole leeren
os.system("cls")

# das zu berechnende Element der Fibonacci-Folge
element = 32

# Messe die Zeit für Berechnung mit Hilfe einer Liste
start = time.time()

ergebnis = fibo(element)

end = time.time()
print("Die Fibonacci-Zahl an %d Stelle lautet %d." % (element, ergebnis))
print("Die Berechnung mit Hilfe einer Liste hat %f Sekunden gedauert" % (end-start))

print("")

# Messe die Zeit für Berechnung in Rekursion
start = time.time()

ergebnis = fibo2(element)

end = time.time()
print("Die Fibonacci-Zahl an %d Stelle lautet %d." % (element, ergebnis))
print("Die Berechnung in Rekursion hat %f Sekunden gedauert" % (end-start))
