"""
ID: alexlu.1
LANG: PYTHON3
TASK: combo
"""
with open("combo.in", "r") as f:
  n = int(f.readline().strip())
  combo1 = [int(x) for x in f.readline().strip().split()]
  combo2 = [int(x) for x in f.readline().strip().split()]

def check_num(num):
  if n == 1:
    return 1
  if num < 1:
    return num + n
  if num > n:
    return num - n
  return num



list1 = [(check_num(a), check_num(b), check_num(c)) for a in range(combo1[0] - 2, combo1[0] + 3) for b in range(combo1[1] - 2, combo1[1] + 3) for c in range(combo1[2] - 2, combo1[2] + 3)]

list2 = [(check_num(a), check_num(b), check_num(c)) for a in range(combo2[0] - 2, combo2[0] + 3) for b in range(combo2[1] - 2, combo2[1] + 3) for c in range(combo2[2] - 2, combo2[2] + 3)]

result = set(list1 + list2)

with open("combo.out", "w") as f:
  f.write(f"{len(result)}\n")