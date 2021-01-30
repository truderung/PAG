from binominal_coefficients import binominal as bi

def pdf(k, n, p):
  return bi(n,k) * p**k * (1-p) ** (n-k)