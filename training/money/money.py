"""
ID: alexlu.1
LANG: PYTHON3
TASK: money
"""
with open("money.in", "r") as f:
    v, n = [int(i) for i in f.readline().strip().split()]
    coins = sorted([int(i) for line in f.readlines() for i in line.strip().split()])
    print(coins)

#original setup =======
# results = [{tuple(0 for i in coins)}] + [set() for i in range(n+coins[-1])]
# for coin in range(len(coins)):
#     shell = tuple(1 if i == coin else 0 for i in range(len(coins)))
#     results[coins[coin]].add(shell)


# # alexlu original ===
# for i in range(1, n+1):
#     print("======" , i)
#     for coin in range(len(coins)):
#         print(" ", coin)
#         if i - coins[coin] < 0:
#             continue
#         #print("  ", len(results[i-coins[coin]]))
#         for arrangement in results[i-coins[coin]]:
#             # new_arrangement = tuple(value+1 if x == coin else value for x, value in enumerate(arrangement))
#             new_arrangement = tuple(arrangement[:coin]) + (arrangement[coin]+1,) + tuple(arrangement[coin+1:])
#             results[i].add(new_arrangement)

# jun ===================
# for i in range(1, n+1):
#     #print("======" , i)
#     for coin in range(len(coins)):
#         #print(" ", coin, len(results[i]))
#         for arrangement in results[i]:
#             new_arrangement = tuple(value+1 if x == coin else value for x, value in  enumerate(arrangement))
#             results[i+coins[coin]].add(new_arrangement)


# for level, i in enumerate(results):
#     print(level, i)

#third idea ==============
results = [1] +  [0 for i in range(n)]

for coin in coins:
    for i in range(n):
        if coin+i > n:
            continue
        results[coin+i] += results[i]

print(results[n])

# print(len(results[-1]))
with open("money.out", "w") as f:
    f.write(f"{results[n]}\n")


