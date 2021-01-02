
with open("backforth.in", "r") as f:
    buckets_1 = [int(x) for x in f.readline().strip().split()]
    buckets_2 = [int(x) for x in f.readline().strip().split()]

def solve(t1, t2, b1, b2, l, d):
    # print(d * "||||", t1)
    if d > 3:
        return [t1]

    if l == 0:
        result = [j for i in b1 for j in solve(t1-i, t2+i, b1[:b1.index(i)] + b1[b1.index(i)+1:], b2 + [i], 1, d+1)]
    else:
        result = [j for i in b2 for j in solve(t1+i, t2-i, b1 + [i], b2[:b2.index(i)] + b2[b2.index(i)+1:], 0, d+1)]

    return set(result)

# print(buckets_1, buckets_2)
result = set(solve(1000, 1000, buckets_1, buckets_2, 0, 0))
with open("backforth.out", "w") as f:
    f.write(str(len(result)))
