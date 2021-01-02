with open("planting.in", "r") as f:
    n = int(f.readline().strip())
    neighbors = [0 for i in range(n)]
    for i in range(n-1):
        a, b = [int(x)-1 for x in f.readline().strip().split()]
        neighbors[a] += 1
        neighbors[b] += 1

result = max(neighbors)
print(result+1)
with open("planting.out", "w") as f:
    f.write(str(result+1))
