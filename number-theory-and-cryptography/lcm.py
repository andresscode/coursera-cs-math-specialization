import sys


def gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0
  return gcd(b, a % b) if b > 0 else a


def lcm(a, b):
  assert a > 0 and b > 0
  if a >= b:
    return (a * b) // gcd(a, b)
  else:
    return (a * b) // gcd(b, a)


print(lcm(int(sys.argv[1]), int(sys.argv[2])))
