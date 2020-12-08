import sys

def solve(a, i, d):
  if d == 1:
    return (a * i) + a
  tmp = solve(a, i, d - 1)
  return (tmp * i) + tmp


print(solve(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])))
