def gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0
  return gcd(b, a % b) if b > 0 else a


def extended_gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0

  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)


def diophantine(a, b, c):
  if a >= b:
    assert c % gcd(a, b) == 0
    d, x, y = extended_gcd(a, b)
  else:
    assert c % gcd(b, a) == 0
    d, y, x = extended_gcd(b, a)
  return c // d * x, c // d * y


import sys


print(diophantine(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
