"""
ID: alexlu.1
LANG: PYTHON3
TASK: castle
"""
# import time
# start = time.time()
import itertools
class Node:
  def __init__(self, i, j):
    self.partners = []
    self.component = -1
    self.n_wall = None
    self.e_wall = None
    self.i = i
    self.j = j
  def __repr__(self):
    return f"{self.i} {self.j}"
  def __str__(self):
    return f"{self.i} {self.j} partner:{self.partners}"

def decode(n):
  n = 15 - n
  results = []
  for x in range(3, -1, -1):
    if 2 ** x <= n:
      n -= 2 ** x
      if x == 3:
        results.append([1, 0])
      elif x == 2:
        results.append([0, 1])
      elif x == 1:
        results.append([-1, 0])
      else:
        results.append([0, -1])
  return results

def flood_fill(new_component):
  num_visited = None
  while num_visited != 0:
    num_visited = 0
    for row in squares:
      for node in row:
        if node.component == -2:
          num_visited = num_visited + 1
          node.component = new_component
          components[new_component].append(node)
          for partner in node.partners:
            if partner.component == -1:
              partner.component = -2

def sort_left(node):
  return node.j

def sort_down(node):
  return node.i
def break_wall(room1, room2):
  print("---------")
  nodes = [x for row in squares for x in row 
    if (x in room1 and (x.n_wall in room2 or x.e_wall in room2)) 
    or (x in room2 and (x.n_wall in room1 or x.e_wall in room1))]
  if not nodes:
    return None
  print(nodes)
  nodes = [i for i in nodes if i.j == min([x.j for x in nodes])]
  print(nodes)
  new_node = max(nodes, key=lambda x: x.i)
  print(new_node)
  return new_node
  
with open("castle.in", "r") as f:
  m, n = [int(x) for x in f.readline().strip().split()]

  squares = [[Node(row, square) for square in range(m)] for row in range(n)]
  for i in range(n):
    values = [int(x) for x in f.readline().strip().split()]
    for j in range(m):
      paths = decode(values[j])
      for x in paths:
        squares[i][j].partners.append(squares[i+x[0]][j+x[1]])
      if [-1, 0] not in paths:
        if i > 0:
          squares[i][j].n_wall = squares[i-1][j]
      if [0, 1] not in paths:
        if j+1 < m:
          squares[i][j].e_wall = squares[i][j+1]



components = []
num_components = 0
for row in squares:
  for node in row:   
    if node.component == -1:
      node.component = -2
      components.append([])
      flood_fill(num_components)
      num_components += 1

components = sorted(components, reverse = True, key = len)
rooms = [[len(room), x] for x, room in enumerate(components)]
# print(components)
# print(rooms)

equal = True
for x in rooms:
  if x[0] == 1:
    continue
  equal = False
  break
if equal == True:
  i = n - x[0]
  j = 0
  s = x[0] + x[0]
  print("pls")
else:
  i = 1
  search_repeat = False
  size = None
  nodes = []
  while i < len(rooms):
    for x in range(i):
      node = break_wall(components[x], components[i])
      s = rooms[x][0] + rooms[i][0]
          
      if not node:
        continue
      if search_repeat:
        if s != size:
          print(len(nodes))
          print(nodes)

          item = min(nodes, key=lambda x: x[0].j)
          node = item[0]
          s = item[1]
          i = len(rooms)
          search_repeat = False
          break
        nodes.append((node, s))
        continue
      search_repeat = True
      print("searching")
      size = s
      nodes.append((node, s))
      break  
    i += 1
  if search_repeat:
    print(len(nodes))
    print(nodes)
    item = min(nodes, key=lambda x: x[0].j)
    node = item[0]
    s = item[1]

  # print(squares)
  i = node.i
  j = node.j
  print("hi")

with open("castle.out", "w") as f:
  f.write(f"{len(rooms)}\n")
  f.write(f"{rooms[0][0]}\n")
  f.write(f"{s}\n")
  if node.n_wall:
    f.write(f"{i + 1} {j + 1} N\n")
  else:
    f.write(f"{i + 1} {j + 1} E\n")

# print("------------TIME----------------")
# print(time.time() - start)