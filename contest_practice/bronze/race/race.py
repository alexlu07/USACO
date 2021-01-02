# with open("race.in", "r") as f:
#     k, n = [int(i) for i in f.readline().strip().split()]
#     x_list = []
#     for i in range(n):
#         x_list.append(int(f.readline().strip()))

# results = []
# for x in x_list:
#     t = x
#     print("x:", x)
#     while True:
#         dist = None
#         if (t+x-1) % 2 == 0:
#             dist = sum(range(1, (t+x-1)//2+1))*2
#         if (t+x-1) % 2 == 1:
#             dist = sum(range(1, (t+x-1)//2+1))*2 + (t+x-1)//2 + 1

#         print(t, dist)
#         if dist - sum(range(x)) >= k:
#             break

#         t += 1

#     results.append(t)

# print(results)

with open('race.in', 'r') as fin:
    distance, n = map(int, fin.readline().strip().split())
    cases = [int(fin.readline().strip()) for i in range(n)]


solutions = []
for min in cases:
    time = 0
    traveled = 0
    vel = 0
    while distance > traveled:
        time += 1
        vel += 1
        traveled += vel
        if distance <= traveled:
            break
        elif vel >= min:
            time += 1
            traveled += vel
    solutions.append(time)


with open('race.out', 'w') as fout:
    for solution in solutions:
        fout.write(str(solution) + '\n')
