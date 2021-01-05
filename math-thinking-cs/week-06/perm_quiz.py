def sequence():
  w1 = list('marine')
  w2 = list('airmen')
  seq = []
  for i in range(len(w2)):
    for j in range(len(w1)):
      if w1[j] == w2[i] and j != i:
        tmp = w1[j]
        w1[j] = w1[i]
        w1[i] = tmp
        seq.append((j, i))
  return seq
  

result = sequence()
print(result)
