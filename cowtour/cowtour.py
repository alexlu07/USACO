"""
ID: alexlu.1
LANG: PYTHON3
TASK: cowtour
"""
import math
with open("cowtour.in", "r") as f:
    n = int(f.readline().strip())
    pastures = [[int(k) for k in f.readline().strip().split()] for i in range(n)]
    # print(pastures)
    paths = [[int(x) for x in f.readline().strip()] for i in range(n)]
    # print(paths)

def distance(a, b):
    return math.sqrt(((a[0]-b[0])**2) + ((a[1]-b[1])**2))

dist = [[math.inf for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if paths[i][j]:
            dist[i][j] = distance(pastures[i], pastures[j])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

def flood_fill(new_field):
    num_visited = 1
    while num_visited > 0:
        num_visited = 0
        for i in range(n):
            if fields[i] == -1:
                num_visited += 1
                fields[i] = new_field
                for j in range(n):
                    if paths[i][j]:
                        if fields[j] == None:
                            fields[j] = -1

fields = [None for i in range(n)]
num_fields = 0
for i in range(n):
    if fields[i] == None:
        fields[i] = -1
        flood_fill(num_fields)
        num_fields += 1

# print(fields)

field_diameters = [0 for field in range(num_fields)]
diameters = [0 for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if diameters[i] < dist[i][j] and not math.isinf(dist[i][j]):
            diameters[i] = dist[i][j]

    if diameters[i] > field_diameters[fields[i]]:
        field_diameters[fields[i]] = diameters[i]

# for i in range(n):
#     if diameters[i] > field_diameters[components[i]]:
#         field_diameters[components[i]] = diameters[i]

best_diameter = math.inf
for i in range(n):
    for j in range(n):
        if fields[i] == fields[j]:
            continue

        diameter = max(diameters[i] + diameters[j] + distance(pastures[i], pastures[j]), field_diameters[fields[i]], field_diameters[fields[j]])
        if diameter < best_diameter:
            print(i, j, diameters[i], diameters[j], distance(pastures[i], pastures[j]))
            best_diameter = diameter

# print(best_diameter)
# for j in range(n):
#     print(6, j)
#     print(dist[6][j])
print("{:.6f}".format(best_diameter))
with open("cowtour.out", "w") as f:
    f.write("{:.6f}\n".format(best_diameter))
