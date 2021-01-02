from collections import defaultdict

with open("guess.in", "r") as f:
    n = int(f.readline().strip())
    shared = [[0 for i in range(n)] for i in range(n)]
    c = defaultdict(list)
    for i in range(n):
        props = f.readline().strip().split()[2:]
        for j in props:
            for animal in c[j]:
                shared[i][animal] += 1
                shared[animal][i] += 1
            c[j].append(i)

with open("guess.out", "w") as f:
    f.write(str(max(map(max, shared))+1))
