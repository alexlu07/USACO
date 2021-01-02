import bisect
from collections import deque
with open("wormsort.in", "r") as f:
    n, m = [int(x) for x in f.readline().strip().split()]
    positions = [int(x)-1 for x in f.readline().strip().split()]
    wormholes = []
    neighbors = [[] for i in range(n)]
    for i in range(m):
        a, b, w = [int(x) for x in f.readline().strip().split()]
        a -= 1
        b -= 1
        bisect.insort_left(wormholes, [w, a, b])
        bisect.insort_left(neighbors[a], b)
        bisect.insort_left(neighbors[b], a)

components = [-1 for i in range(n)]
comp_value = []
total_comp = 0
def flood_fill(start, c):
    connected = []
    visited = [-1 for i in range(n)]
    queue = deque()
    queue.append(start)
    while len(queue) > 0:
        i = queue.popleft()
        # print(queue, neighbors[i])
        if components[i] == c:
            continue
        components[i] = c
        visited[i] = 1
        connected.append(i)
        for j in neighbors[i]:
            # if j == -1:
                # continue
            if visited[j] == -1:
                queue.append(j)
    return connected

for i in range(n):
    if components[i] == -1:
        comp_value.append(flood_fill(i, total_comp))
        total_comp += 1

# print(components)
# print(comp_value)
result = None
for w, a, b in wormholes:
    # print(neighbors)
    # print("a", a, "b", b, "x", bisect.bisect_left(neighbors[a], b))
    neighbors[a].pop(bisect.bisect_left(neighbors[a], b))
    neighbors[b].pop(bisect.bisect_left(neighbors[b], a))
    # print(neighbors)
    old = components[a]
    comp_value.append(flood_fill(a, total_comp))
    # print(w, a, b)
    # print(components)
    if set(comp_value[-1]) - set([positions[i] for i in comp_value[-1]]):
        result = w
        break
    total_comp += 1

    comp_value.append(flood_fill(b, total_comp))
    total_comp += 1

# print(result)
with open("wormsort.out", "w") as f:
    f.write(str(result))
