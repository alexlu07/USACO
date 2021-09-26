n, q = [int(x) for x in input().strip().split()]
sums = [0]
bsums = [0]
paint = [ord(x)-65 for x in input().strip()]
seen = [0 for i in range(26)]
previous = -1
for i in range(n):
    x = sums[i]
    if seen[paint[i]] == 0:
        x += 1
        seen[paint[i]] = 1
    if paint[i] < previous:
        for j in range(paint[i]+1, 26):
            seen[j] = 0
    previous = paint[i]
    sums.append(x)

seen = [0 for i in range(26)]
previous = -1
for i in range(n):
    # print(paint[n-i-1])
    x = bsums[i]
    if seen[paint[n-i-1]] == 0:
        x += 1
        seen[paint[n-i-1]] = 1
    if paint[n-i-1] < previous:
        for j in range(paint[n-i-1]+1, 26):
            seen[j] = 0
    previous = paint[n-i-1]
    bsums.append(x)

# print(sums, bsums)
# print(paint)
for i in range(q):
    a, b = [int(x) for x in input().strip().split()]
    # print(a, b)

    strokes = sums[a-1] + bsums[n-b]
    print(strokes)
# for i, a in enumerate(input().strip()):
#     if i == 0:
#         sh = [0 for i in range(26)]
#         sh[ord(a)-65] = 1
#         sums.append(sh)
#     else:
#         sh = sums[i-1].copy()
#         sh[ord(a)-65] += 1
#         sums.append(sh)

# for i in range(q):
#     a, b = [int(x)-1 for x in input().strip().split()]
#     strokes = 0
#     if a != 0:
#         for j in range(26):
#             if sums[a-1][j] > 0:
#                 strokes += 1
#     if b != n-1:
#         for j in range(26):
#             if sums[n-1][j] > sums[b][j]:
#                 strokes += 1
#     print(strokes)
