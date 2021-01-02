from collections import deque
with open("lightson.in", "r") as f:
    n, m = [int(x) for x in f.readline().strip().split()]
    lit = [[0 for j in range(n)] for i in range(n)]
    switches = [[[] for j in range(n)] for i in range(n)]
    for i in range(m):
        x, y, a, b = [int(i)-1 for i in f.readline().strip().split()]
        switches[x][y].append((a, b))
    lit[0][0] = 1

# print(switches)
result = 0
while True:
    visited = [[0 for j in range(n)] for i in range(n)]
    n_visited = 1
    visited[0][0] = 1
    queue = deque([(0, 0)])
    while len(queue) > 0:
        i, j = queue.popleft()
        for a, b in switches[i][j]:
            if lit[a][b]:
                continue
            lit[a][b] = 1
        # print(i, j, lit)

        if i-1 >= 0:
            if not visited[i-1][j] and lit[i-1][j]:
                n_visited += 1
                visited[i-1][j] = 1
                queue.append((i-1, j))
        if i+1 < n:
            if not visited[i+1][j] and lit[i+1][j]:
                n_visited += 1
                visited[i+1][j] = 1
                queue.append((i+1, j))
        if j-1 >= 0:
            if not visited[i][j-1] and lit[i][j-1]:
                n_visited += 1
                visited[i][j-1] = 1
                queue.append((i, j-1))
        if j+1 < n:
            if not visited[i][j+1] and lit[i][j+1]:
                n_visited += 1
                visited[i][j+1] = 1
                queue.append((i, j+1))
    if n_visited > result:
        result = n_visited
    else:
        break
    # print(result)

# print(sum([sum(x) for x in lit]))
with open("lightson.out", "w") as f:
    f.write(str(sum([sum(x) for x in lit])))
