import collections
import bisect
with open("measurement.in", "r") as f:
    n, g = [int(x) for x in f.readline().strip().split()]
    days = []
    for i in range(n):
        bisect.insort_left(days, [int(x) for x in f.readline().strip().split()])

cows = collections.defaultdict(lambda: g)
order = [g for i in range(n)]
displayed = n
result = 0
for day in days:
    # print(day, order, cows)
    old = cows[day[1]]
    new = cows[day[1]] + day[2]
    cows[day[1]] = new
    if day[2] > 0:
        if new == order[-1] and old < order[-1]:
            displayed += 1
            result += 1
        elif new > order[-1] and old < order[-1]:
            displayed = 1
            result += 1
            # print("2")
        elif new > order[-1] and old == order[-1] and displayed != 1:
            displayed = 1
            result += 1
            # print("1")
    else:
        # print("3?")
        if new == order[-2] and old == order[-1] and displayed == 1:
            displayed = 1
            for i in range(n-2, -1, -1):
                if order[i] == order[-2]:
                    displayed += 1
                    continue
                break
            result += 1
            # print("3")
        elif new < order[-2] and old == order[-1] and displayed == 1:
            displayed = 0
            for i in range(n-2, -1, -1):
                if order[i] == order[-2]:
                    displayed += 1
                    continue
                break
            result += 1
        elif new < order[-1] and old == order[-1] and displayed != 1:
            displayed -= 1
            result += 1
    order.pop(bisect.bisect_left(order, old))
    bisect.insort_left(order, new)


print(result)
with open("measurement.out", "w") as f:
    f.write(str(result))
