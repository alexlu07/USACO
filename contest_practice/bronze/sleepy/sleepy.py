with open("sleepy.in", "r") as f:
    n = int(f.readline().strip())
    order = [int(x) for x in f.readline().strip().split()]

current = float("inf")
result = 0
for i in range(n-1, -1, -1):
    if order[i] < current:
        current = order[i]
        result += 1
    else:
        break

# print(n-result)
with open("sleepy.out", "w") as f:
    f.write(str(n-result))
