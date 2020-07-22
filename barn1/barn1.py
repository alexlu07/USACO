"""
ID: alexlu.1
LANG: PYTHON3
TASK: barn1
"""
with open("barn1.in", "r") as f:
    m, s, c = [int(x) for x in f.readline().strip().split()]
    cow_num = sorted([int(f.readline().strip()) for x in range(2, c + 2)])
    cow_num = list(map(lambda x, y: [x, y], cow_num, cow_num))

x = 1
while len(cow_num) > m:
    y = 0
    while y < len(cow_num) - 1:
        # print(cow_num[y + 1][0] - cow_num[y][1], cow_num[y + 1][0], cow_num[y][1],
        #       cow_num[y + 1][0] - cow_num[y][1] == x, y)
        if len(cow_num) <= m:
            #print("hi")
            break
        if cow_num[y + 1][0] - cow_num[y][1] == x:
            cow_num[y][1] = cow_num[y + 1][1]
            cow_num.remove(cow_num[y + 1])
            continue

        y += 1
    x += 1
    # print(m, len(cow_num), cow_num, y, x)

with open("barn1.out", "w") as f:
    total_stalls = 0
    for x in cow_num:
        total_stalls += x[1] - x[0] + 1
    f.write(str(total_stalls) + "\n")
