with open("shell.in", "r") as f:
    n = int(f.readline().strip())
    loc = [1, 2, 3]
    result = [0, 0, 0]
    for i in range(n):
        # print(loc)
        a, b, g = [int(x) for x in f.readline().strip().split()]
        for j in range(3):
            if loc[j] == a:
                loc[j] = b
            elif loc[j] == b:
                loc[j] = a

            if loc[j] == g:
                result[j] += 1
# print(loc)
with open("shell.out", "w") as f:
    f.write(str(max(result)))
