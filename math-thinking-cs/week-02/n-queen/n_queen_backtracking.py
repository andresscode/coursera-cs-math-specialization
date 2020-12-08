import sys

def is_valid(p):
  i = len(p) - 1
  for j in range(i):
    if i - j == abs(p[i] - p[j]):
      return False
  return True


def extend_solution(p, n):
  if len(p) == n:
    print(p)
    return

  for i in range(n):
    if i not in p:
      p.append(i)
      if is_valid(p):
        extend_solution(p, n)
      p.pop()


extend_solution([], int(sys.argv[1]))
