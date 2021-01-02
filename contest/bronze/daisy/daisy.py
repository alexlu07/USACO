# with open("daisy.in", "r") as f:
    # n = int(f.readline().strip())
    # p = [int(i) for i in f.readline().strip().split()]

n = int(input().strip())
p = [int(i) for i in input().strip().split()]
result = 0
for i in range(n):
    for j in range(i, n):
        average = sum(p[i:j+1]) / (j-i+1)
        if average.is_integer():
            for x in range(i, j+1):
                if p[x] == average:
                    result += 1
                    break


print(result)
