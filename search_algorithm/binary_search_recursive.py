
such_liste = [2, 5, 7, 2, 34, 4, 25, 9]

def binary_search(liste, gesucht, start, ende):
    if ende < start:
        return -1

    mitte = (start + ende)//2
    if liste[mitte] == gesucht:
        return mitte
    elif liste[mitte] < gesucht:
        return binary_search(liste, gesucht, mitte+1, ende)
    else:
        return binary_search(liste, gesucht, start, mitte-1)


sorted_list = sorted(such_liste)
end = len(sorted_list) - 1

print( binary_search(sorted_list, 34, 0, end) )
print( binary_search(sorted_list, 9, 0, end) )
print( binary_search(sorted_list, 2, 0, end) )
print( binary_search(sorted_list, 1, 0, end) )
