# with open("rut.in", "r") as f:
#     n = int(f.readline().strip())
#     north = []
#     east = []
#     cows = []
#     for i in range(n):
#         direction, x, y = f.readline().strip().split()
#         if direction == "N":
#             cows.append(("N", len(north)))
#             north.append([int(x), int(y), "Infinity", i])
#         else:
#             cows.append(("E", len(east)))
#             east.append([int(x), int(y), "Infinity", i])

n = int(input().strip())
north = []
east = []
cows = []
for i in range(n):
    direction, x, y = input().strip().split()
    if direction == "N":
        cows.append(("N", len(north)))
        north.append([int(x), int(y), "Infinity", i])
    else:
        cows.append(("E", len(east)))
        east.append([int(x), int(y), "Infinity", i])

north = sorted(north, key=lambda i: i[0])
east = sorted(east, key=lambda i: i[1])

for i in north:
    for j in east:
        if j[2] != "Infinity":
            continue
        if j[1] < i[1] or i[0] < j[0]:
            continue
        if j[1] - i[1] > i[0] - j[0]:
            i[2] = j[1] - i[1]
            break
        if j[1] - i[1] < i[0] - j[0]:
            j[2] = i[0] - j[0]

# print(north)
# print(east)
north = sorted(north, key=lambda i: i[3])
east = sorted(east, key=lambda i: i[3])
for i in cows:
    if i[0] == "N":
        print(north[i[1]][2])
    else:
        print(east[i[1]][2])
