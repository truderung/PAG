from faculty import faculty

f = faculty
def binominal(n, k):
  return f(n) / f(k) / f(n-k)


b = binominal
def solve_binominal(x, y, n):
  sum = 0
  for k in range(n+1):
    sum += b(n,k)* x ** (n-k) * y ** k
  return sum

# print(solve_binominal(0,0,0))
# print(solve_binominal(0,0,1))
# print(solve_binominal(0,0,5))

# print(solve_binominal(2,3,2))
