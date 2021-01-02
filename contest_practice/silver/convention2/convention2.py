import bisect
import heapq
with open("convention2.in", "r") as f:
    n = int(f.readline().strip())
    sorted_cows = []
    for i in range(n):
        a, t = [int(x) for x in f.readline().strip().split()]
        bisect.insort_right(sorted_cows, [a, i, t])

result = 0
waiting = [(sorted_cows[0][1], 0)]
time = 0
max_cow = 1
while max_cow + 1 < n:
    if len(waiting) == 0:
        waiting.append((sorted_cows[max_cow][1], max_cow))
        max_cow += 1
    priority, i = heapq.heappop(waiting)
    if time - sorted_cows[i][0] > result:
        result = time - sorted_cows[i][0]

    if sorted_cows[i][0] > time:
        time = sorted_cows[i][0]
    time += sorted_cows[i][2]

    for j in range(max_cow, n):
        if sorted_cows[j][0] > time:
            max_cow = j
            break

        heapq.heappush(waiting, (sorted_cows[j][1], j))

# print(result)

with open("convention2.out", "w") as f:
    f.write(str(result))
