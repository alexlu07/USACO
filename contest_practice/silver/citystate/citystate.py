with open("citystate.in", "r") as f:
    n = int(f.readline().strip())
    citystates = [[0 for i in range(676)] for i in range(676)]
    for i in range(n):
        city, state = f.readline().strip().split()
        city = 26*(ord(city[0])-65) + ord(city[1]) - 65
        state = 26*(ord(state[0])-65) + ord(state[1]) - 65
        citystates[city][state] += 1

result = 0
for i in range(676-1):
    for j in range(i+1, 676):
        result += citystates[i][j] * citystates[j][i]

# print(result)
with open("citystate.out", "w") as f:
    f.write(str(result))
