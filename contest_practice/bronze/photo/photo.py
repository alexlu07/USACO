with open("photo.in", "r") as f:
    n = int(f.readline().strip())
    b = [int(i) for i in f.readline().strip().split()]

# first_last = 2 * sum(range(n)) - sum(b)
# firsts = []
# if first_last


result = None
for i in range(1, n):
    cont = False
    a = [i]
    for j in b:
        if j - a[-1] < 1:
            cont = True
            break
        a.append(j - a[-1])
    if cont:
        continue

    if len(set(a)) < n:
        continue

    result = a
    break

# print(result)
with open("photo.out", "w") as f:

    for i in range(n-1):
        f.write(str(result[i]) + " ")
    f.write(str(result[-1]))
