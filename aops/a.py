import random

p = 0.1


money = 0
results = []
for i in range(1000000):
    x = 0
    while (random.random() >= p): x += 1
    if x < c: money += c
    results.append(x)

print(sum(results)/len(results))
print(money/len(results))