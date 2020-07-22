"""
ID: alexlu.1
LANG: PYTHON3
TASK: numtri
"""


class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.max = -1
    self.left = left
    self.right = right

  def __str__(self):
    return f"{self.val}"

with open("numtri.in", "r") as f:
  n = int(f.readline().strip())
  data = [[Node(int(x)) for x in f.readline().strip().split()] for line in range(n)]

for i, row in enumerate(data):
  for j in range(len(row)):
    if i < len(data) - 1:
      data[i][j].left = data[i+1][j]
      data[i][j].right = data[i+1][j+1]

data = data[::-1]

for row in data:
  for node in row:
    if not node.left and not node.right:
      node.max = node.val
    else:
      node.max = max(node.left.max, node.right.max) + node.val

result = data[-1][-1].max

with open("numtri.out", "w") as f:
  f.write(f"{result}\n")
