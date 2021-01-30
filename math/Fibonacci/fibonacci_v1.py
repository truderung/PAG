# Die Funktion fibo(x) berechnet das mit x angeforderte Element 
# einer Fibonacci-Reihe.
# Diese Implementierung benutzt eine Liste, berechnet alle
# Glieder der Reihe bis zur Stelle x und liefert den berechneten
# Wert zurück 

# Eine Fibonacci-Folge ist so definiert, dass beginnend mit
# 0 und 1 sich die jeweils folgende Zahl durch Addition ihrer beiden
# vorherigen Zahlen ergibt: 0,1,1,2,3,5,8,13,...
# Im Zusammenhang mit Listen lässt sich das x-te Glied berechnen aus:
# a[x] = a[x-1] + a[x-2]

def fibo(x):
  if x == 0 or x == 1:
    return 1

  a = [0 for i in range(0,x)]

  a[0] = 1
  a[1] = 1

  i = 2
  while i < x:
    a[i] = a[i-1] + a[i-2]
    i += 1

  return a[x-1]
