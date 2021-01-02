import bisect
with open("whereami.in", "r") as f:
    n = int(f.readline().strip())
    string = f.readline().strip()

result = None
for l in range(1, n+1):
    seen = []
    for i in range(n-l+1):
        s = string[i:i+l]
        if len(seen) == 0:
            seen.append(s)
            continue
        index = bisect.bisect_left(seen, s)
        if index == len(seen):
            seen.insert(index, s)
            continue
        if seen[index] == s:
            break
        seen.insert(index, s)
    else:
        result = l
        break

print(result)

with open("whereami.out", "w") as f:
    f.write(str(result))

