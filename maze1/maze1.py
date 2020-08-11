"""
ID: alexlu.1
LANG: PYTHON3
TASK: maze1
"""
import bisect
class Node:
    def __init__(self):
        self.neighbors = []
        self.explored = False
        self.cost = 10000

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __str__(self):
        return str(self.cost)

    def __repr__(self):
        return str(self.cost)


with open("maze1.in", "r") as f:
    w, h = [int(x) for x in f.readline().strip().split()]
    matrix = [list(f.readline().rstrip('\n')) for i in range(2*h + 1)]
    # for i in matrix:
    #     for j in i:
    #         print(j, end="")
    #     print()

exits = []
nodes = [[Node() for j in range(w)] for i in range(h)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for i in range(h):
    for j in range(w):
        for ichange, jchange in directions:
            if matrix[i*2+1+ichange][j*2+1+jchange] == " ":
                if 0 <= i+ichange < h and 0 <= j+jchange < w:
                    nodes[i][j].neighbors.append(nodes[i+ichange][j+jchange])
                else:
                    node = Node()
                    node.neighbors.append(nodes[i][j])
                    node.cost = 0
                    exits.append(node)
                    print(f"exit: {i} {j}")
                    nodes[i][j].neighbors.append(node)

iterations = 0
nodes = [node for row in nodes for node in row]
for source in exits:
    new_nodes = nodes + [source]
    for i in new_nodes:
        i.explored = False
    nodesvisited = 0
    smallest_nodes = [source]
    print("=======")
    while len(smallest_nodes) > 0:
        # print(smallest_nodes)
        node = smallest_nodes.pop(0)
        if node.cost == 10000:
            print("some error: graph not connected?")

        node.explored = True
        nodesvisited += 1
        for neighbor in node.neighbors:
            iterations += 1
            if node.cost + 1 < neighbor.cost:
                neighbor.cost = node.cost + 1
                if neighbor in smallest_nodes:
                    smallest_nodes.remove(neighbor)
                bisect.insort(smallest_nodes, neighbor)
    # print(nodes)

print(max(nodes, key=lambda x: x.cost))
with open("maze1.out", "w") as f:
    f.write(f"{max(nodes, key=lambda x: x.cost)}\n")
