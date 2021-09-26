n = int(input().strip())

rows = [[0, 0] for i in range(n)]
cols = [[0, 0] for i in range(n)]
for i in range(n):
    row = input().strip().split()
    for j in range(n):
        x = int(row[j])
        if j % 2 == 0:
            rows[i][0] += x
        else:
            rows[i][1] += x

        if i % 2 == 0:
            cols[j][0] += x
        else:
            cols[j][1] += x

r = sum([max(i) for i in rows])
c = sum([max(i) for i in cols])
# print(rows)
# print(cols)
print(max(r, c))
