"""
ID: alexlu.1
LANG: PYTHON3
TASK: stamps
"""
import time
import collections
start = time.time()
with open("stamps.in", "r") as f:
  k, n = [int(x) for x in f.readline().strip().split()]
  stamps = [int(x) for line in f.readlines() for x in line.strip().split()]

  values = [(True, 0)] + [(False, float("inf")) for i in range(max(stamps)*(k+1))]
# print(max(stamps)*(k+1))

loop = time.time()


# for stamp in stamps:
#     print(stamp)
#     # print(i, values[i])
#     i = 0
#     while i <= k*max(stamps):
#         if values[i][1] < k:
#             if values[i][1]+1 < values[i+stamp][1]:
#                 values[i+stamp] = (True, values[i][1]+1)
#         i += 1

i = 0
while values[i][0] == True:
    if i % 10000 == 0:
        print(i)
    # print(i, values[i])
    for stamp in stamps:
        if values[i][1] < k:
            if values[i][1]+1 < values[i+stamp][1]:
                values[i+stamp] = (True, values[i][1]+1)
    i += 1

print(i-1)
with open("stamps.out", "w") as f:
  f.write(f"{i-1}\n")
#2:00
print("Start time:", loop-start, "Loop time:", time.time()-loop)
