"""
ID: alexlu.1
LANG: PYTHON3
TASK: frac1
"""
import math
with open("frac1.in", "r") as f:
  n = int(f.readline().strip())

frac_list = []

for denominator in range(2, n+1):
  for numerator in range(1, denominator):
    if math.gcd(numerator, denominator) == 1:
      frac_list.append(str(numerator) + "/" + str(denominator))

frac_list.append("0/1")
frac_list.append("1/1")

frac_list = sorted(frac_list, key=lambda i: eval(i))

with open("frac1.out", "w") as f:
  for x in frac_list:
    f.write(f"{x}\n")