# with open("rut.in", "r") as f:
#     n = int(f.readline().strip())
#     north = []
#     east = []
#     cows = []
#     for i in range(n):
#         direction, x, y = f.readline().strip().split()
#         if direction == "N":
#             cows.append(("N", len(north)))
#             north.append([int(x), int(y), 0, 0, i])
#         else:
#             cows.append(("E", len(east)))
#             east.append([int(x), int(y), 0, 0, i])

n = int(input().strip())
north = []
east = []
cows = []
for i in range(n):
    direction, x, y = input().strip().split()
    if direction == "N":
        cows.append(("N", len(north)))
        north.append([int(x), int(y), 0, 0, i])
    else:
        cows.append(("E", len(east)))
        east.append([int(x), int(y), 0, 0, i])

north = sorted(north, key=lambda i: i[0])
east = sorted(east, key=lambda i: i[1])

for i in north:
    for j in east:
        if j[2] == 1:
            continue
        if j[1] < i[1] or i[0] < j[0]:
            continue
        if j[1] - i[1] > i[0] - j[0]:
            i[2] = 1
            j[3] += i[3] + 1
            break
        if j[1] - i[1] < i[0] - j[0]:
            j[2] = 1
            i[3] += j[3] + 1

# print(north)
# print(east)
north = sorted(north, key=lambda i: i[4])
east = sorted(east, key=lambda i: i[4])
for i in cows:
    if i[0] == "N":
        print(north[i[1]][3])
    else:
        print(east[i[1]][3])
