def change(amount):
  if amount == 24:
    return [7, 7, 5, 5]
  elif amount == 25:
    return [5, 5, 5, 5, 5]
  elif amount == 26:
    return [7, 7, 7, 5]
  elif amount == 27:
    return [7, 5, 5, 5, 5]
  elif amount == 28:
    return [7, 7, 7, 7]

  coins = change(amount - 5)
  coins.append(5)
  return coins


assert change(24) == [7, 7, 5, 5]
assert change(25) == [5, 5, 5, 5, 5]
assert change(26) == [7, 7, 7, 5]
assert change(27) == [7, 5, 5, 5, 5]
assert change(28) == [7, 7, 7, 7]
assert change(29) == [7, 7, 5, 5, 5]
