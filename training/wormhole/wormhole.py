"""
ID: alexlu.1
LANG: PYTHON3
TASK: wormhole
"""
with open("wormhole.in", 'r') as f:
  n = int(f.readline())
  wormholes = [[int(x) for x in f.readline().strip().split()] for line in range(n)]
  wormholes = [[0, 0]] + wormholes

partner = [0 for x in range(n + 1)]
nexthole = [0 for x in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if wormholes[j][0] > wormholes[i][0] and wormholes[j][1] == wormholes[i][1]:
      if nexthole[i] == 0 or wormholes[j][0] - wormholes[i][0] < wormholes[nexthole[i]][0] - wormholes[i][0]:
    	  nexthole[i] = j

def cycle_exists():
  for start in range(1, n + 1):
   # does there exist a cylce starting from start
    pos = start;
    for count in range(n):
      pos = nexthole[partner[pos]];
    if pos != 0:
       return True
  return False

def solve():
  total = 0
  for i in range(1, n + 1):
    if partner[i] == 0:
      break  

  if i == n:
    if cycle_exists():
      return 1
    else:
      return 0

  for j in range(i + 1, n + 1):
    if partner[j] == 0:
      partner[j] = i
      partner[i] = j
      total += solve()
      partner[j] = 0
      partner[i] = 0
  return total

with open("wormhole.out", "w") as f:
  f.write(f"{int(solve())}\n")