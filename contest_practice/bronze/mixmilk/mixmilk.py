with open("mixmilk.in", "r") as f:
    a_size, a = [int(x) for x in f.readline().strip().split()]
    b_size, b = [int(x) for x in f.readline().strip().split()]
    c_size, c = [int(x) for x in f.readline().strip().split()]

print(a, b, c)

for i in range(33):
    amt = min(a, b_size-b)
    a -= amt
    b += amt

    amt = min(b, c_size-c)
    b -= amt
    c += amt

    amt = min(c, a_size-a)
    c -= amt
    a += amt

amt = min(a, b_size-b)
a -= amt
b += amt

with open("mixmilk.out", "w") as f:
    f.write(str(a) + "\n")
    f.write(str(b) + "\n")
    f.write(str(c))
