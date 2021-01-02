"""
ID: alexlu.1
LANG: PYTHON3
TASK: sort3
"""
with open("sort3.in", "r") as f:
  n = int(f.readline().strip())
  sequence = [int(f.readline().strip()) for x in range(n)]
  sorted_sequence = sorted(sequence)
  print(n, sequence, sorted_sequence)

outliers = []
for i in range(len(sequence)):
  if sequence[i] != sorted_sequence[i]:
    outliers.append([sorted_sequence[i], sequence[i]])

counter = 0
pair = None
pairs = []
i = 0
while i < len(outliers):
  x = outliers[i]
  for y in outliers:
    # print(outliers)
    print("____________")
    if x[1] == y[0]:
      if x[0] == y[1]:
        counter += 1
        outliers.remove(x)
        outliers.remove(y)
        print(x, y)
        i -= 1
        break
  i += 1

if len(outliers) > 0:
  counter += int(len(outliers) / 3 * 2)
  print(len(outliers) / 3 * 2)

with open("sort3.out", "w") as f:
  f.write(f"{counter}\n")