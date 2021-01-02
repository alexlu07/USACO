"""
ID: alexlu.1
LANG: PYTHON3
TASK: comehome
"""
import bisect
with open("comehome.in", "r") as f:
    p = int(f.readline().strip())
    pastures = ["Z"]
    distance = [float("inf") for i in range(100)]
    visited = [False for i in range(100)]
    paths = [[None for j in range(100)] for i in range(100)]
    distance[0] = 0
    smallest_nodes = [0]

    for line in range(p):
        a, b, value = f.readline().strip().split()
        if not a in pastures:
            pastures.append(a)
        if not b in pastures:
            pastures.append(b)
        a, b = pastures.index(a), pastures.index(b)
        if paths[a][b]:
            paths[a][b] = min(paths[a][b], int(value))
            paths[b][a] = min(paths[b][a], int(value))
        else:
            paths[a][b] = int(value)
            paths[b][a] = int(value)

# nodesvisited = 0
# while nodesvisited < len(pastures):
#     nodesvisited += 1
#     i = min([a for a in range(len(pastures)) if not visited[a]],key=lambda x: distance[x])

#     if distance[i] == float("inf"):
#         print("graph is not connected")
#         break

#     visited[i] = True

#     for j in range(len(pastures)):
#         if paths[i][j]:
#             if distance[i] + paths[i][j] < distance[j]:
#                 distance[j] = distance[i] + paths[i][j]
#                 if j == pastures.index("R"):
#                     print(distance[j])


nodesvisited = 0
while nodesvisited < len(pastures):
    nodesvisited += 1
    i = smallest_nodes.pop(0)

    if distance[i] == float("inf"):
        print("graph is not connected")
        break

    visited[i] = True

    for j in range(len(pastures)):
        if paths[i][j]:
            if distance[i] + paths[i][j] < distance[j]:
                distance[j] = distance[i] + paths[i][j]
                # if j == pastures.index("R"):
                #     print(distance[i], distance[j])
                if j in smallest_nodes:
                    smallest_nodes.remove(j)
                k = bisect.bisect_left([distance[x] for x in smallest_nodes], distance[j])
                smallest_nodes.insert(k, j)
                print(smallest_nodes)

result = float("inf")
node = None
for i in range(len(pastures)):
    if pastures[i].isupper() and pastures[i] != "Z":
        if distance[i] < result:
            result = distance[i]
            node = pastures[i]
# print([(pastures[x], x) for x in range(len(pastures)) if pastures[x].isupper()])
# print([(distance[x], x) for x in range(len(pastures)) if pastures[x].isupper()])

print(result)
with open("comehome.out", "w") as f:
    f.write(f"{node} {result}\n")
