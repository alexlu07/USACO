import bisect
with open("haybales.in", "r") as f, open("haybales.out", "w") as fout:
    n, q = [int(x) for x in f.readline().strip().split()]
    haybales = []
    for i in f.readline().strip().split():
        bisect.insort_left(haybales, int(i))

    for i in range(q):
        a, b = [int(x) for x in f.readline().strip().split()]
        a_position = bisect.bisect_left(haybales, a)
        b_position = bisect.bisect_left(haybales, b)
        if b_position < n:
            if haybales[b_position] == b:
                b_position += 1
        if i > 0:
            fout.write("\n")
        # print(a_position, b_position, b_position-a_position)
        fout.write(str(b_position-a_position))
