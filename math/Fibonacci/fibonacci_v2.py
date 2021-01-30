# Die Funktion fibo2(x) berechnet das mit x angeforderte Element 
# einer Fibonacci-Reihe, jedoch auf einem rekursiven Weg.

# Eine Fibonacci-Folge ist so definiert, dass beginnend mit
# 0 und 1 sich die jeweils folgende Zahl durch Addition ihrer beiden
# vorherigen Zahlen ergibt: 0,1,1,2,3,5,8,13,...
# Allgemein lässt sich das x-te Glied berechnen aus:
# für f(x=0) = 0 und f(x=1) = 1 und für jedes weitere x
# f(x) = f(x-1) + f(x-2) (Rekursive Vorschrift)


def fibo2(x):
  if x == 1 or x == 2:
    return 1

  return fibo2(x-1) + fibo2(x-2)
