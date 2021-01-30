
such_liste = [2, 5, 7, 2, 34, 4, 25, 9]

def binary_search(liste, gesucht):
    start = 0
    ende = len(liste) - 1

    while start <= ende:
        mitte = (start + ende)//2

        if liste[mitte] == gesucht:
            return mitte
        elif liste[mitte] < gesucht:
            start = mitte+1
        else:
            ende = mitte-1

    return -1


sorted_list = sorted(such_liste)

print( binary_search(sorted_list, 34) )
print( binary_search(sorted_list, 9) )
print( binary_search(sorted_list, 2) )
print( binary_search(sorted_list, 1) )
