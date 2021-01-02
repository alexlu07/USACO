"""
ID: alexlu.1
LANG: PYTHON3
TASK: milk3
"""
with open("milk3.in", "r") as f:
  a, b, c = [int(x.strip()) for x in f.readline().split()]

print(a, b, c)

capacity = [a, b, c]

def pour(fr, to, fq, tq):
  delta = capacity[to] - tq
  if fq - delta < 0:
    return 0, tq + fq
  else:
    return fq - delta, tq + delta



possibilities = set()
def search(fr, to, ot, fq, tq, oq):
  fq, tq = pour(fr, to, fq, tq)
  if fr == 0:
    if to == 1:
      b = tq
      c = oq
    else:
      b = oq
      c = tq
    a = fq
  elif to == 0:
    if fr == 1:
      b = fq
      c = oq
    else:
      b = oq
      c = fq
    a = tq
  else:
    if to == 1:
      b = tq
      c = fq
    else:
      b = fq
      c = tq
    a = oq
    
  if (a, b, c) in possibilities:
    print("bye")
    return
  else:
    print("hi")
    possibilities.add((a, b, c))

  if fq != 0:
    if tq < capacity[to]:
      print(1)
      search(fr, to, ot, fq, tq, oq)
    if ot < capacity[ot]:
      print(2)
      search(fr, ot, to, fq, oq, tq)
  if tq != 0:
    # if fq < capacity[fr]:
    #   print(3)
    #   search(to, fr, ot, tq, fq, oq)
    if ot < capacity[ot]:
      print(4)
      search(to, ot, fr, tq, oq, fq)
  if oq != 0:
    if fq < capacity[fr]:
      print()
      search(ot, fr, to, oq, fq, tq)
    if tq < capacity[to]:
      print(1)
      search(ot, to, fr, oq, tq, fq)

search(2, 0, 1, c, 0, 0)
search(2, 1, 0, c, 0, 0)

results = sorted([x[2] for x in possibilities if x[0] == 0])

print(possibilities)
print(results)

with open("milk3.out", "w") as f:
  for x in results[:-1]:
    f.write(f"{x} ")
  f.write(f"{results[-1]}\n")