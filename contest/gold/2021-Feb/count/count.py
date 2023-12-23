import math
q = int(input().strip())
queries =

x = 4
if x == 0:
    dist = 1
else:
    dist = 3 ** (math.floor(math.log(x, 3)) + 1)

chain = 1
if math.log(x/2, 3).is_integer():
    chain = x/2
