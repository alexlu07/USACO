# with open("abcs.in", "r") as f:
    # n = map(int, f.readline().strip().split())
n = map(int, input().strip().split())

n = sorted(n)
a = n[0]
b = n[1]
abc = n[-1]
c = abc - a - b

print(a, b, c)
