import random

n = 20

# Erstelle eine Liste mit n Elementen bestehend aus
# Zufallszahlen zwischen 1 und 1000
liste = [random.randint(1,1000) for i in range(n)]

print(liste)

# unsorted ist hier eine Hilfsvariable, die behauptet,
# dass die Liste unsortiert sei
unsorted = True

# solange unsorted tatsächlich True bleibt, wird
# die While-Schleife wiederholt durchlaufen
while unsorted:
  schwarzer_zeiger = len(liste) - 1  # setze den 'schwarzen' Zeiger auf das Ende der Liste
  unsorted = False # behaupte im inneren der äußeren while-Schleife, die Liste sei schon sortiert

  # Beginne hier mit der inneren While-Schleife,
  # die den 'schwarzen' und 'roten' Zeiger von hinten
  # nach vorne bewegt und eine Prüfung macht,
  # ob das Element in der Liste, auf das der 'schwarze' Pfeil zeigt,
  # nicht vielleicht kleiner ist, als der linke Nachbar ('roter' Pfeil).
  # Wenn das ja, dann Tausche, wenn nicht bewege die zeiger einfach weiter.
  while schwarzer_zeiger > 0:
    roter_zeiger = schwarzer_zeiger - 1

    # Wenn ja, Tausche die Elemente und setze unsorted auf True.
    # Damit sagt die innere Schleife der äußeren, dass die Liste doch
    # noch unsortiert ist (bzw. sein könnte).
    if liste[roter_zeiger] > liste[schwarzer_zeiger]:
      x = liste[roter_zeiger]
      liste[roter_zeiger] = liste[schwarzer_zeiger]
      liste[schwarzer_zeiger] = x
      unsorted = True

    schwarzer_zeiger -= 1

print(liste)
