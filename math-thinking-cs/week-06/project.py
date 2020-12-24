def is_even_permutation(p):
  t = 0
  while True:
    done = True
    for i in range(len(p)-1):
      if p[i] > p[i+1]:
        done = False
        p[i], p[i+1] = p[i+1], p[i]
        t = t + 1
    if done:
      break
  return t % 2 == 0


def solution(position):
  moves = []
  if is_even_permutation(position[:-1]):
    print('Hello') 
  return moves


moves = solution([1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 10, 14, 15, 0])
print(moves)
