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


def wrapper(a, b):
  if a >= b:
    return extended_gcd(a, b)
  else:
    return extended_gcd(b, a)


import sys


print(wrapper(int(sys.argv[1]), int(sys.argv[2])))
