import math
# with open("cowntagion.in", "r") as f:
#     n = int(f.readline().strip())
#     neighbors = [[] for i in range(n)]
#     for i in range(n-1):
#         x, y = [int(i)-1 for i in f.readline().strip().split()]
#         neighbors[x].append(y)
#         neighbors[y].append(x)

n = int(input().strip())
neighbors = [[] for i in range(n)]
for i in range(n-1):
        x, y = [int(i)-1 for i in input().strip().split()]
        neighbors[x].append(y)
        neighbors[y].append(x)

neighbors[0].append(0)
result = 0
stack = [(0, 0)]
while len(stack) > 0:
    i, parent = stack.pop()
    if len(neighbors[i]) == 1:
        continue
    result += math.ceil(math.log2(len(neighbors[i]))) + len(neighbors[i])-1
    for j in neighbors[i]:
        if j != parent:
            stack.append((j, i))

print(result)
