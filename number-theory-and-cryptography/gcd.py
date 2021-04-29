import sys


def gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0
  return gcd(b, a % b) if b > 0 else a


def wrapper(a, b):
  if a >= b:
    return gcd(a, b)
  else:
    return gcd(b, a)

print(wrapper(int(sys.argv[1]), int(sys.argv[2])))
