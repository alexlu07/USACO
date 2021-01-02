with open("lineup.in") as f:
    n = int(f.readline().strip())
    names = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
    numbers = {"Beatrice": 0,
               "Belinda": 1,
               "Bella": 2,
               "Bessie": 3,
               "Betsy": 4,
               "Blue": 5,
               "Buttercup": 6,
               "Sue": 7}
    neighbors = [[] for i in range(8+1)]
    for i in range(n):
        x, y = [numbers[j] for j in f.readline().strip().split(" must be milked beside ")]
        neighbors[x].append(y)
        neighbors[y].append(x)

# order = []
# cow = -1
available = [1 for i in range(8)]
# print(neighbors)
# for c in range(8):
#     cows = neighbors[cow] if neighbors[cow] else list(range(8))
#     print(neighbors[cow])
#     print(cows)
#     for i in cows:
#         if available[i]:
#             available[i] = 0
#             order.append(i)
#     else:
#         order.pop()

def solve(cow, parent, depth=0):
    if neighbors[cow]:
        cows = neighbors[cow]
        if len(neighbors[cow]) == 1 and neighbors[cow][0] == parent:
            # print(cow)
            cows = list(range(8))
    else:
        cows = list(range(8))

    for i in cows:
        if available[i]:
            if len(neighbors[cow]) == 0:
                if len(neighbors[i]) == 2:
                    continue
            # print(depth * 5 * "|", names[i], i)
            available[i] = 0
            # print(depth * 5 * "|", available)
            order = solve(i, cow, depth+1)
            if order:
                # print("adlfjasdl")
                return order + [i]
            # print(depth * 5 * "|", names[i], i, "---")
            available[i] = 1
    else:
        if any(available):
            return False

        return [cow]

    #
    # order.append(i)
    # if available[i]:
    #     available[i] = 0
    # else:
    #     order.pop()

# print([names[x] for x in solve(-1, None)[8:0:-1]])
result = solve(-1, None)[8:0:-1]
with open("lineup.out", "w") as f:
    for i in result:
        f.write(names[i] + "\n")