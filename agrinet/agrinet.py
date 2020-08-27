"""
ID: alexlu.1
LANG: PYTHON3
TASK: agrinet
"""

with open("agrinet.in", "r") as f:
    n = int(f.readline().strip())
    fin = [int(item) for line in f.readlines() for item in line.strip().split()]
    weight = [fin[i:i+n] for i in range(0, len(fin), n)]
    print(weight)

distance = [float("inf") for i in range(n)]
intree = [False for i in range(n)]

treesize = 1
treecost = 0
intree[0] = True
for j in range(n):
    if j == 0:
        continue
    distance[j] = weight[0][j]

while treesize < n:
    i = min([x for x in range(n) if not intree[x]], key= lambda x: distance[x])

    if distance[i] == float("inf"):
        print("Graph is not connected.")
        break

    treesize += 1
    treecost += distance[i]
    intree[i] = True

    for j in range(n):
        if i == j:
            continue
        distance[j] = min(distance[j], weight[i][j])

print(treesize)
print(treecost)
with open("agrinet.out", "w") as f:
    f.write(f"{treecost}\n")
