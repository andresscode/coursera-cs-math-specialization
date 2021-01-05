def sequence():
  w1 = list('marine')
  w2 = list('airmen')
  seq = []
  for i in range(len(w2)):
    for j in range(len(w1)):
      if w1[j] == w2[i] and i != j:
        k = j
        while k != i:
          tmp = w1[k]
          w1[k] = w1[k-1]
          w1[k-1] = tmp
          seq.append((k-1, k))
          k = k - 1
  return seq


print(sequence())
