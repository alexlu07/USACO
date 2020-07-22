"""
ID: alexlu.1
LANG: PYTHON3
TASK: sprime
"""
import math

with open("sprime.in", "r") as f:
  n = int(f.readline().strip())

ends = ["1", "3", "7", "9"]

def check_prime(x):
  if x % 3 == 0:
    return False
  for d in range(7, math.floor(math.sqrt(x)) + 1, 2):
    if x % d == 0 and x != d:
      return False
  return True


results = []
def solve(counter, str_n, recursions):
  counter += 1
  if counter > recursions:
    results.append(int(str_n))
    return

  if counter == 1:
    solve(counter, "2", recursions)
    solve(counter, "3", recursions)
    solve(counter, "5", recursions)
    solve(counter, "7", recursions)
    return

  for x in ends:
    if check_prime(int(str_n + x)):
      solve(counter, str_n + x, recursions)


solve(0, "", n)


with open("sprime.out", "w") as f:
  for x in results:
    print(x)
    f.write(f"{x}\n")