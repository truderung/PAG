
such_liste = [2, 5, 7, 2, 34, 4, 25, 9]


def lineare_suche(liste, gesucht):
    for index, element in enumerate(liste):
        if element == gesucht:
            return index
    return -1


print(lineare_suche(such_liste, 34))
print(lineare_suche(such_liste, 9))
print(lineare_suche(such_liste, 2))
print(lineare_suche(such_liste, 1))
