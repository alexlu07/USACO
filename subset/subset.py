"""
ID: alexlu.1
LANG: PYTHON3
TASK: subset
"""
# import termcolor
# import colorama
# colorama.init()
# colors = {
#   0: 'white',
#   1: 'red'
# }

# def color_print(x):
#   try:
#     color = colors[x]
#     print(termcolor.colored(x, color),end=" ")
#   except KeyError:
#     print(termcolor.colored(x, 'green', attrs=["dark", 'bold']),end=" ")


with open("subset.in", "r") as f:
  n = int(f.readline().strip())

mainset = [x+1 for x in range(n)]
halfsum = n * (n+1) // 4

result = [0 for i in range(halfsum+1)]
print((n*(n+1)))
if (n*(n+1)) % 4 == 0:
  result[0] = 1
  for i in range(1, n+1):
    for j in range(halfsum, i-1, -1):
      result[j] += result[j-i]
      # for x in result:
      #   color_print(x)
      # print(i, j)

  with open("subset.out", "w") as f:
    f.write(f"{result[halfsum] // 2}\n")
  print(result[halfsum]//2)
else:
  print(0)
  with open("subset.out", "w") as f:
    f.write("0\n")
