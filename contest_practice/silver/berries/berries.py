import bisect
with open("berries.in", "r") as f:
    n, k = [int(x) for x in f.readline().strip().split()]
    original_berries = []
    if n < k:
        original_berries = [0 for i in range(k-n)]
    for i in f.readline().strip().split():
        bisect.insort(original_berries, int(i))

# print(original_berries)
bessie = k//2
result = 0
for i in range(1, 1001):
    berries = original_berries.copy()
    # print(i)
    lost = 0
    short = 0
    for basket in range(k):
        b = berries.pop()
        if b < i:
            short += 1
            lost += i-b
            bisect.insort(berries, 0)
            continue
        bisect.insort(berries, b-i)
    if short > bessie:
        break
    if bessie * i - lost > result:
        result = bessie * i - lost
print(result)
with open("berries.out", "w") as f:
    f.write(str(result))
