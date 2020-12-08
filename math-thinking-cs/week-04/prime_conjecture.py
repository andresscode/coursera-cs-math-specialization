def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True


def solve():
  for i in range(1, 1000001):
    num = i ** 2 + i + 41
    if not is_prime(num):
      return num
  return -1


print(solve())
