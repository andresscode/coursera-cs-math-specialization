import sys

def fast(b, e, m):
  r = 1
  b = b % m
  
  if b == 0:
    return 0

  while e > 0:
    if e & 1 == 1:
      r = r * b % m
    e = e >> 1
    b = b * b % m

  return r

print(fast(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
