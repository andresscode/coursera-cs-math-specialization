import sys


def gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0
  return gcd(b, a % b) if b > 0 else a


def squares(n, m):
    x = gcd(n, m) if n >= m else gcd(m, n)
    return (n // x) * (m // x)


print(squares(int(sys.argv[1]), int(sys.argv[2])))
