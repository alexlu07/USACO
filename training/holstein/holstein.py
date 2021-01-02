"""
ID: alexlu.1
LANG: PYTHON3
TASK: holstein
"""
import time
start = time.time()
with open("holstein.in", "r") as f:
  v = int(f.readline().strip())
  vl = [int(x) for x in f.readline().strip().split()]
  g = int(f.readline().strip())
  gl = [[int(v) for v in f.readline().strip().split()] for x in range(g)]


def combinations(iterable, used, n, m, results):
  if m > n:
    results.append(used)
    return results
  if used:
    a = iterable.index(used[-1])
  else:
    a = -1
  for x in iterable[a+1:]:
    if used:
      if iterable.index(x) <= iterable.index(used[-1]):
        continue
    results = combinations(iterable, used + [x], n, m + 1, results)

  return results


results = []
for n in range(g):
  results += combinations(range(g), [], n, 0, [])
sums = [[sum(i) for i in zip(*[gl[j] for j in x])] for x in results]
final_results = []

for sum in range(len(sums)):
  success = True
  for vitamin in range(v):
    if sums[sum][vitamin] < vl[vitamin]:
      success = False
      break
  if success:
    final_results.append(results[sum])

with open("holstein.out", "w") as f:
  f.write(f"{len(final_results[0])}")
  for x in final_results[0]:
    f.write(f" {x+1}")
  f.write("\n")