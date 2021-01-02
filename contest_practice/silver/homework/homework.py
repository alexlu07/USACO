import bisect
# with open("homework.in", "r") as f:
#     n = int(f.readline().strip())
#     scores = [int(x) for x in f.readline().strip().split()]
#     total = sum(scores)
#     sums = [(total, min(scores))]
#     grades = scores[::-1]
#     results = []
# for k, i in enumerate(scores[:-2]):
#     print(k)
#     grades.pop()
#     if i == sums[-1][1]:
#         sums.append((sums[-1][0]-i, min(grades)))
#     else:
#         sums.append((sums[-1][0]-i, sums[-1][1]))
#     bisect.insort_left(results,((sums[-1][0]-sums[-1][1])/(n-k-2), k+1))

# # print(sums)
# # print(results)
# with open("homework.out", "w") as f:
#     maximum = results[-1][0]
#     f.write(str(results[-1][1]))
#     for i in results[n-2:-1:-1]:
#         if i[0] == maximum:
#             f.write(" " + str(i[1]))
#             continue
#         break

with open("homework.in", "r") as f:
    n = int(f.readline().strip())
    scores = [int(x) for x in f.readline().strip().split()][::-1]
    sums = [(0, float("inf"))]
    results = []

for x, i in enumerate(scores):
    if i < sums[-1][1]:
        sums.append((sums[-1][0]+i, i))
    else:
        sums.append((sums[-1][0]+i, sums[-1][1]))

    if x == 0 or x == n-1:
        continue

    k = n - x - 1
    bisect.insort_left(results, ( (sums[-1][0]-sums[-1][1])/x, k ))

# print(sums)
# print(results)
with open("homework.out", "w") as f:
    maximum = results[-1][0]
    f.write(str(results[bisect.bisect_left(results, (maximum, 0))][1]))
    for i in range(bisect.bisect_left(results, (maximum, 0))+1, n-2):
        f.write("\n" + str(results[i][1]))
