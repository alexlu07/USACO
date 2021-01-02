"""
ID: alexlu.1
LANG: PYTHON3
TASK: nocows
"""
with open("nocows.in", "r") as f:
    n, k = [int(i) for i in f.readline().strip().split()]
print(n, k )

results = [[0 for j in range(202)] for i in range(101)]
small_trees = [[0 for j in range(202)] for i in range(101)]

results[1][1] = 1
for i in range(2, k+1):
    for j in range(1, n+1, 2):
        print(i, j)
        x = 1
        while x < j-x:
            c = 2 if x != j-1-x else 1
            # print("c:", c, x, "results:", [small_trees[i-2][x],results[i-1][j-1-x]], [results[i-1][x],small_trees[i-2][j-1-x]], [results[i-1][x],results[i-1][j-1-x]], end=" ")
            results[i][j] += c * (small_trees[i-2][x]*results[i-1][j-1-x] +
                                  results[i-1][x]*small_trees[i-2][j-1-x] +
                                  results[i-1][x]*results[i-1][j-1-x])
            results[i][j] %= 9901
            # print(results[i][j])
            x += 2

    for x in range(n+1):
        small_trees[i-1][x] += results[i-1][x] + small_trees[i-2][x]
        small_trees[i-1][x] %= 9901
        # print("small_trees:", i-1, x, small_trees[i-1][x])

print("results:", results[k][n])
with open("nocows.out", "w") as f:
    f.write(f"{results[k][n]}\n")

# class Node:
#     def __init__(self, parent, depth):
#         self.parent = parent
#         self.depth = depth

# nodes_left = n - 1
# stack = [node(None, 0)]
# explored = []
# while True:
#     node = stack.pop()
#     if
