"""
ID: alexlu.1
LANG: PYTHON3
TASK: crypt1
"""
with open("crypt1.in", "r") as f:
  n = f.readline().strip()
  numbers = sorted([int(x) for x in f.readline().strip().split()])
print(numbers)

l2 = [(a, b) for a in numbers for b in numbers]
l3 = [a * 100 + b * 10 + c for a in numbers for b in numbers for c in numbers]
l4 = [a * 1000 + b * 100 + c * 10 + d for a in numbers for b in numbers for c in numbers for d in numbers]

# print(l2)
# print(l3)
# print(l4)

counter = 0
for x in l3:
  for a, b in l2:
    i = x * a
    j = x * b
    k = i * 10 + j
    if i > 999 or j > 999 or k > 9999:
      continue
    if i not in l3 or j not in l3 or k not in l4:
      continue
    counter += 1
    print(x, a, b, i, j, k, counter)

print(counter)
with open("crypt1.out", "w") as f:
  f.write(f"{counter}\n")