"""
ID: alexlu.1
LANG: PYTHON3
TASK: hamming
"""

import pprint

with open("hamming.in", "r") as f:
  n, b, d = [int(x) for x in f.readline().strip().split()]

def test_difference(a, b):
  #return 10
  n = a ^ b
  result = 0
  while n > 0:
    result += n % 2
    n = n // 2
  return result

def ind(iterable, used):
  if used:
    return iterable.index(used[-1])+1
  else:
    return 0

def combinations(iterable, n, m=1, results=[], used=[]):
  # print(m)
  if m > n:
    results.append(used)
    print(results)
    return results

  for x in iterable[ind(iterable, used):]:
    success = True
    if used:
      for y in used:
        if test_difference(x, y) < d:
          success = False
          break
    if success:
      # print(used+[x])
      results = combinations(iterable, n, m + 1, results, used + [x])

  return results

result = [0]
for x in range(1, 2**b):
  success = True
  for y in result:
    if test_difference(x, y) < d:
      success = False
      break
  if success:
    result.append(x)
  if len(result) == n:
    break

with open("hamming.out", "w") as f:
  for x in range(len(result)):
    if x % 10 == 0:
      if x > 0:
        f.write("\n")
      f.write(f"{result[x]}")
    else:
      f.write(f" {result[x]}")
  f.write("\n")
# a = combinations(range(128),16)
# pprint.pprint(a)

