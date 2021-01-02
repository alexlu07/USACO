with open("blist.in", "r") as f:
    timeline = []
    n = int(f.readline().strip())
    for i in range(n):
        s, e, b = [int(x) for x in f.readline().strip().split()]
        timeline.append([s, 1, b])
        timeline.append([e, -1, b])

timeline = sorted(timeline)
buckets = 0
result = 0
for i in timeline:
    buckets += i[1] * i[2]
    if buckets > result:
        result = buckets

with open("blist.out", "w") as f:
    f.write(str(result))
