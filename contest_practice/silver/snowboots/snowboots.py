with open("snowboots.in", "r") as f:
    n, b = [int(x) for x in f.readline().strip().split()]
    tiles = [int(x) for x in f.readline().strip().split()]
    boots = []
    for i in range(b):
        boots.append([int(x) for x in f.readline().strip().split()])

used = [float("inf") for i in range(n)]
used[0] = 0

# print(boots)
# print(tiles)
for i in range(n):
    # print(i, used)
    if used[i] == float("inf"):
        continue
    for j in range(used[i], b):
        if (tiles[i] > boots[j][0]):
            continue
        for x in range(boots[j][1]):
            new_i = i+boots[j][1]-x
            if new_i >= n:
                continue
            if j < used[new_i] and boots[j][0] >= tiles[new_i]:
                used[new_i] = j

# print(used)
with open("snowboots.out", "w") as f:
    f.write(str(used[-1]))
