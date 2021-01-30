# Übung: Quadrad einer positiven ganzen Zahl x berechnen durch Summe der ersten
# x ungeraden positiven ganzen Zahlen beginnend bei Eins.


# deklarieren und initialisieren
q = 0
# Benutzerabfrage
x = int(input("Bitte einen Wert für x eingeben: "))

# Summe bilden
for k in range(1, x+1):
  q += 2*k - 1

# Ausgabe
print("Das Quadrad von %d beträgt %d." % (x, q))

