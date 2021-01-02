"""
ID: alexlu.1
LANG: PYTHON3
TASK: inflate
"""
import time as t
import pprint

start = t.time()

with open("inflate.in", "r") as f:
    m, n = [int(x) for x in f.readline().strip().split()]
    types = [[int(x) for x in f.readline().strip().split()] for line in range(n)]
    #pprint.pprint(types)
print(m, len(types))

minutes = [0 for i in range(m+1)]
for points, time in types:
    minutes[time] = points

setup = t.time()


# for i in range(m+1):
#     for points, time in types:
#         if i - time < 0:
#             continue
#         # print(i, time, points, minutes[i], minutes[i-time])
#         if minutes[i] + points > minutes[i-time]:
#             minutes[i] = minutes[i] + points


for points, time in types:
    for i in range(m-time+1):
        if 3 > 2:
            pass
        #pass
        #if minutes[i] + points > minutes[i+time]:
        #minutes[i+time] = minutes[i] + points
print(f"setup: {setup-start}, dyn: {t.time() - setup}, total: {t.time()-start}")

# print(minutes[m], minutes[0], minutes[120], minutes[240], minutes[260], minutes[280], minutes[300])

print(minutes[m])
with open("inflate.out", "w") as f:
    f.write(f"{minutes[m]}\n")


