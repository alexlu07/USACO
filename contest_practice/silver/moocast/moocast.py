from collections import deque
def inside(x, y, r, x2, y2):
    return (x2-x) ** 2 + (y2-y) ** 2 <= r ** 2

with open("moocast.in", "r") as f:
    n = int(f.readline().strip())
    cows = []
    neighbors = [[] for i in range(n)]
    for i in range(n):
        x, y, r = [int(x) for x in f.readline().strip().split()]
        for j in range(len(cows)):
            if inside(cows[j][0], cows[j][1], cows[j][2], x, y):
                neighbors[j].append(i)
            if inside(x, y, r, cows[j][0], cows[j][1]):
                neighbors[i].append(j)

        cows.append([x, y, r])

def flood_fill(start):
    visited = [False for i in range(n)]
    comp_size = 0
    queue = deque([start])
    visited[start] = True
    while len(queue) > 0:
        i = queue.popleft()
        comp_size += 1
        for j in neighbors[i]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True

    return comp_size

result = 0
for i in range(n):
    size = flood_fill(i)
    if size > result:
        result = size


# print(component)
print(result)
with open("moocast.out", "w") as f:
    f.write(str(result))
