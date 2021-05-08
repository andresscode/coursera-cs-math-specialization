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


def chinese(a, ra, b, rb):
  _, x, y = wrapper(a, b)
  tmp = ra * b * y + rb * a * x
  return tmp % (a * b)


import sys


print(chinese(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))

