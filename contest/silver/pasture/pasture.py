import bisect
# with open("pasture.in", "r") as f:
#     n = int(f.readline().strip())
#     x_sorted = []
#     y_sorted = []
#     for i in range(n):
#         x, y = [int(i) for i in f.readline().strip().split()]
#         bisect.insort_left(x_sorted, (x, y))
#         bisect.insort_left(y_sorted, (y, (x, y)))

n = int(input().strip())
x_sorted = []
y_sorted = []
for i in range(n):
    x, y = [int(i) for i in input().strip().split()]
    bisect.insort_left(x_sorted, (x, y))
    bisect.insort_left(y_sorted, (y, (x, y)))

# print(x_sorted)
x_len = len(x_sorted)
y_len = len(y_sorted)

result = 0
for x1 in range(x_len-1):
    for x2 in range(x1+1, x_len):
        # y_min = bisect.bisect_left((min(x_sorted[x1][1], x_sorted[x2][1]), 0))
        # y_max = bisect.bisect_left((max(x_sorted[x1][1], x_sorted[x2][1]), 0))
        y_set = [i[1] for i in x_sorted[x1:x2+1] if x_sorted[x1][1] > x_sorted[x2][1] and i[1] <= x_sorted[x1][1] or x_sorted[x1][1] < x_sorted[x2][1] and i[1] >= x_sorted[x1][1]]
        # print(y_set)
        yl = len(y_set)
        for y1 in range(yl-1):
            
            result += 1
            # print(x_sorted[x1][0], x_sorted[x2][0], y_set[y1], x_sorted[x2][1])

print(result + n + 1)

# rects = set()
# for i in range(1, n+1):
#     for j in range(n-i+1):
#         rects.add(frozenset(x_sorted[j:j+i]))
#         rects.add(frozenset([x[1] for x in y_sorted[j:j+i]]))

# repeats = 0
# for i in range(1, n+1):
#     for j in range(n-i+1):
#         if frozenset([x[1] for x in y_sorted[j:j+i]]) in rects:
#             repeats += 1
#             # print(i, [x[1] for x in y_sorted[j:j+i]])
#         rects.add(frozenset([x[1] for x in y_sorted[j:j+i]]))

# result = len(rects) + 1
# print(result)
