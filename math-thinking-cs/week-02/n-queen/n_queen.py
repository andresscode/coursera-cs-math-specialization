import sys
import itertools as it

def is_solution(p):
  for (i1, i2) in it.combinations(range(len(p)), 2):
    if abs(i1 - i2) == abs(p[i1] - p[i2]):
      return False
  return True


assert(is_solution([1, 3, 0, 2]) == True)
assert(is_solution([3, 1, 0, 2]) == False)


for p in it.permutations(range(int(sys.argv[1]))):
  if is_solution(p):
    print(p)
    break
