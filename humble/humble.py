"""
ID: alexlu.1
LANG: PYTHON3
TASK: humble
"""





import time
start = time.time()

with open("humble.in", "r") as f:
    k, n = [int(x) for x in f.readline().strip().split()]
    s = [int(x) for x in f.readline().strip().split()]


pindex = [0 for i in range(k)]
humble = [0 for i in range(n+1)]
nhum = 0
humble[nhum] = 1
nhum += 1

while nhum < n+1:
    minimum = float("inf")
    minp = -1
    for i in range(k):
        # print("->", pindex[i])
        # print(i)
        # print(s[i], humble[pindex[i]], humble[nhum-1])
        while s[i] * humble[pindex[i]] <= humble[nhum-1]:
            pindex[i] += 1
        # print("<-", pindex[i])

        if s[i] * humble[pindex[i]] < minimum:
            minimum = s[i] * humble[pindex[i]]
            minp = i

    humble[nhum] = minimum
    nhum += 1
    pindex[minp] += 1
    # print("MIN", minimum)
print(len(humble))
print(humble[n])

# humble = SortedSet([1])
# print(n)
# print((n+1)//min(s))
# iterations = 0
# for i in range((n+1)//min(s)):
#     h = humble.pop(0)
#     for p in s:
#         iterations += 1
#         humble.add(h*p)

# # print(humble)
# print(humble[n])

with open("humble.out", "w") as f:
    f.write(f"{humble[n]}\n")
# print(humble)
# print(pindex)
print(f"Finished in {time.time()-start} seconds.")


# humbles = [1]
# result = None
# for i in range(30):
#     h = humbles.pop(0)
#     # print(len(humbles))
#     print(h)
#     ind = bisect.bisect(s, h)
#     print(ind, s[ind if ind-1 < 0 else ind-1:])
#     for p in s[bisect.bisect(s, h):]:
#         bisect.insort(humbles, h*p)
#         print(f"appened: {h} {h*p}")
#     if i == n:
#         result = h
#         print(h)

# with open("humble.out", "w") as f:
#     f.write(f"{result}\n")

# found = []
# a = []
# humbles = [1]
# result = None
# for i in range(n+1):
#     h = humbles.pop(0)
#     # print(h)
#     for p in s:
#         # if not h*p in found:
#         if h*p == 12:
#             print(h, p)
#         bisect.insort(humbles, h*p)
#         bisect.insort(a, h*p)
#     if i == n:
#         result = h
#         print(h)

# a = [list(g) for k, g in groupby(a)]
# print([x for x in a if len(x) > 1])
# with open("humble.out", "w") as f:
#     f.write(f"{result}\n")


# found = []
# humbles = [1]
# result = None
# for i in range(n+1):
#     h = humbles.pop(0)
#     print(len(humbles))
#     # print(h)
#     for p in s:
#         if not h*p in found:
#             bisect.insort(humbles, h*p)
#             found.append(h*p)
#     if i == n:
#         result = h
#         print(h)

# with open("humble.out", "w") as f:
#     f.write(f"{result}\n")

# humble = [False for i in range(10000)]
# humble[1] = True

# h = 0
# x = 1
# while h < n+1:
#     print(h, x)
#     if humble[x]:
#         h += 1
#         for p in s:
#             humble[x * p] = True
#     x += 1

# result = [i for i in range(len(humble)) if humble[i]]
# # print(result)
# # print(len(result))
# print(result[n])

# with open("humble.out", "w") as f:
#     f.write(f"{result[n]}\n")
