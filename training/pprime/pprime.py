"""
ID: alexlu.1
LANG: PYTHON3
TASK: pprime
"""
import math
with open("pprime.in", "r") as f:
    a, b = [int(x) for x in f.readline().strip().split()]

print(a, b)
len_a = len(str(a))
len_b = len(str(b))

def check_prime(l):
  results = []
  for x in l:
    prime = True
    if x % 3 == 0:
      continue
    for d in range(5, math.floor(math.sqrt(x)) + 1, 2):
      if x % d == 0 and x != d:
        prime = False
        break
    if prime == True:
      results.append(x)
  return results

results = []
def choose_num(counter, recursions, str_n):
  counter += 1

  if counter > recursions // 2 + recursions % 2:
    if recursions % 2 == 1:
      results.append(int(str_n[:-1] + str_n[::-1]))
    else:
      results.append(int(str_n + str_n[::-1]))
    return

  for x in range(10):
    if counter == 1:
      if x % 2 == 0:
        continue
    choose_num(counter, recursions, str_n + str(x))

for x in range(len_a - len_a % 2 + 1, len_b+1, 2):
  print(x)
  choose_num(0, x, "")

results = [x for x in results if x >= a and x <= b]
results = check_prime(results)
if a <= 11 and b >= 11:
  results.append(11)

results = sorted(results)

with open("pprime.out", "w") as f:
  for x in results:
    f.write(f"{x}\n")