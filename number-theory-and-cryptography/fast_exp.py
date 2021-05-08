import sys

def fast(b, k, m):
  c = b % m
  for _ in range(k):
    c = c * c % m
  return c

print(fast(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
