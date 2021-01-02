with open("shuffle.in", "r") as f:
    n = int(f.readline().strip())
    shuffle = [[int(i)-1, 0, 0] for i in f.readline().strip().split()]
    for i in shuffle:
        shuffle[i[0]][1] += 1

result = 0
def follow(i):
    shuffle[i][2] += 1
    if shuffle[i][2] >= shuffle[i][1]:
        global result
        result += 1
        follow(shuffle[i][0])

for x, i in enumerate(shuffle):
    if i[1] == 0:
        follow(x)

# print(shuffle)
# print(result)
with open("shuffle.out", "w") as f:
    f.write(str(n-result))
