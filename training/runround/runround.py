"""
ID: alexlu.1
LANG: PYTHON3
TASK: runround
"""
with open("runround.in", "r") as f:
    m = int(f.readline().strip())

def test(n):
    counter = 0
    used = set()
    for i in range(len(n)):
        counter += n[counter]
        counter = counter % len(n)
        used.add(n[counter])

    if len(used) == len(n):
        return True
    return False


result = None
for n in range(m+1 , 1000000000):
    # print(n)
    n = [int(x) for x in str(n)]
    if sum(n) % len(n) == 0:
        if test(n):
            result = int("".join([str(x) for x in n]))
            break

with open("runround.out", "w") as f:
    f.write(f"{result}\n")
