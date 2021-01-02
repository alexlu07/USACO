with open("gymnastics.in") as f:
    k, n = [int(x) for x in f.readline().strip().split()]
    sessions = []
    for i in range(k):
        sessions.append([int(x) for x in f.readline().strip().split()])

pairs = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            continue

        consistent = True
        for session in sessions:
            for cow in session:
                if cow == i:
                    break
                if cow == j:
                    consistent = False

        if consistent == True:
            pairs += 1

print(pairs)
with open("gymnastics.out", "w") as f:
    f.write(str(pairs))