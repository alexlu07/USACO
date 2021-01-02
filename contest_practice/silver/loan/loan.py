with open("loan.in", "r") as f:
    n, k, m = [int(x) for x in f.readline().strip().split()]

def valid(n, k, x):
    g = 0
    while k > 0 and g < n:
        y = (n-g) / x
        if y < m:
            return k * m >= (n-g)
        g += int(y)
        k -= 1

    return g >= n


low = 1
high = 10 ** 12
while low < high:
    # print(low, high)
    mid = (low + high + 1) // 2
    if valid(n, k, mid):
        low = mid
    else:
        high = mid-1

# print(low)
with open("loan.out", "w") as f:
    f.write(str(low))
