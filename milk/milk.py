"""
ID: alexlu.1
LANG: PYTHON3
TASK: milk
"""
with open("milk.in", "r") as f:
  n, m = [int(x) for x in f.readline().strip().split()]
  farmers = sorted([[int(x) for x in f.readline().strip().split()] for x in range(m)])

print(n, m, farmers)

cost = 0
x = 0
while x < n:
  for i in farmers:
    if x + i[1] < n:
      cost += i[0] * i[1]
      x += i[1]  
    else:
      cost += i[0] * (n-x)
      x = n

with open("milk.out", "w") as f:
  f.write(f"{cost}\n")