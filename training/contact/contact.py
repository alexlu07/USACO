"""
ID: alexlu.1
LANG: PYTHON3
TASK: contact
"""
#5:00

import collections
import time
start = time.time()
with open("contact.in") as f:
    a, b, n = [int(x) for x in f.readline().strip().split()]
    s = "".join([line.strip() for line in f.readlines()])

print(a, b, n)
# print(s)
x = 0
counter = collections.defaultdict(int)
for i in range(len(s)):
    for l in range(a, b+1):
        x += 1
        string = s[i:i+l]
        if len(string) == l:
            counter[string] += 1
            # print(string, i)

print(x, "Time passed:", time.time()-start)
results = collections.defaultdict(list)
for v, f in sorted(counter.items(), key = lambda x: x[1], reverse=True):
    if len(results) > n:
        break
    results[f].append(v)

# print(results)

with open("contact.out", "w") as f:
    c = 0
    for frequency, values in sorted(results.items(),reverse=True):
        # print(frequency, c)
        c += 1
        if c > n:
            print("done")
            break
        f.write(f"{frequency}\n")
        values = sorted(values, key=lambda x: int("1" + x))
        for row in [values[i:i+6] for i in range(0, len(values), 6)]:
            f.write(" ".join(row))
            f.write("\n")
print(f"Time passed: {time.time()-start}")
# for l in range(a, b+1):


