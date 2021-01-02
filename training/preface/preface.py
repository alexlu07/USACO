"""
ID: alexlu.1
LANG: PYTHON3
TASK: preface
"""
with open("preface.in") as f:
  n = int(f.readline().strip())

possibilities = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
def find_letters(x, results):
  i = 0
  while x > 0:
    number = list(possibilities)[i]
    if number <= x:
      x -= number
      for char in possibilities[number]:
        results[char] += 1
    else:
      i += 1
  
  return results



results = {'I': 0, 'V': 0, 'X': 0, 'L': 0, 'C': 0, 'D': 0,'M': 0}

for x in range(1, n+1):
  results = find_letters(x, results)

with open("preface.out", "w") as f:
  for x in results:
    if results[x] > 0:
      f.write(f"{x} {results[x]}\n")