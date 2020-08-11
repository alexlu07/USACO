"""
ID: alexlu.1
LANG: PYTHON3
TASK: ttwo
"""
from operator import add
with open("ttwo.in", "r") as f:
    matrix = [[None for j in range(10)] for i in range(10)]
    for i in range(10):
        row = f.readline().strip()
        for j in range(10):
            cell = row[j]
            if cell == "C":
                cow = (i, j)
                cow_rotation = 0
                matrix[i][j] = "."
            elif cell == "F":
                farmer = (i, j)
                farmer_rotation = 0
                matrix[i][j] = "."
            else:
                matrix[i][j] = cell

directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
def move(position, direction):
    delta = directions[direction]
    new_position = tuple(map(add, position, delta))
    for x in new_position:
        if x < 0 or x > 9:
            return position, (direction+1) % 4

    if matrix[new_position[0]][new_position[1]] == "*":
        return position, (direction+1) % 4

    return new_position, direction

minutes = 0
cow_positions = []
for i in range(160000):
    if cow == farmer:
        break
    cow, cow_rotation = move(cow, cow_rotation)
    farmer, farmer_rotation = move(farmer, farmer_rotation)
    minutes += 1
else:
    minutes = 0

with open("ttwo.out", "w") as f:
    f.write(f"{minutes}\n")
