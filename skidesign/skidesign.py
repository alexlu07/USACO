"""
ID: alexlu.1
LANG: PYTHON3
TASK: skidesign
"""
with open("skidesign.in", "r") as f:
  n = int(f.readline().strip())
  hills = [int(x.strip()) for x in f.readlines()]

costs = []
for x in range(min(hills), max(hills) - 16):
  result = 0
  boundary = (x, x + 17)
  for hill in hills:
    if hill < boundary[0]:
      result += (boundary[0] - hill) ** 2 
    if hill > boundary[1]:
      result += (hill - boundary[1]) ** 2 
  costs.append(result)

cost = min(costs)

with open("skidesign.out", "w") as f:
  f.write(f"{cost}\n")