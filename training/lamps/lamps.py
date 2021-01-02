"""
ID: alexlu.1
LANG: PYTHON3
TASK: lamps
"""
with open("lamps.in", "r") as f:
    n = int(f.readline().strip())
    c = int(f.readline().strip())
    on = []
    for lamp in f.readline().strip().split():
        if lamp == '-1':
            break
        on.append((int(lamp)-1) % 6)
    off = []
    for lamp in f.readline().strip().split():
        if lamp == '-1':
            break
        off.append((int(lamp)-1) % 6)

buttons = [0, 63, 42, 21, 36]
results = []
if c > 2:
    possibilities = [(x, y) for x in range(4) for y in [0, 4]]
elif c == 2:
    possibilities = [(x, y) for x in range(1, 5) for y in range(1, 5)]
elif c == 1:
    possibilities = [(x, 0) for x in range(1, 5)]
else:
    possibilities = [(0, 0)]

print(n, c, on, off, possibilities)
for possibility in possibilities:
    lamps = 63
    for button in possibility:
        lamps = lamps ^ buttons[button]
    lamps = str(bin(lamps))[2:]
    lamps = "".join(["0" for i in range(6 - len(lamps))]) + lamps
    print(lamps)
    if any([lamps[lamp] == "0" for lamp in on]) or any([lamps[lamp] == "1" for lamp in off]):
        continue
    results.append(lamps)

print(results)
results = sorted([int(x, 2) for x in results])
with open("lamps.out", "w") as f:
    for lamps in results:
        lamps = str(bin(lamps))[2:]
        lamps = "".join(["0" for i in range(6 - len(lamps))]) + lamps
        lamps *= n // 6 + 1
        f.write(f"{lamps[:n]}\n")
    if not results:
        f.write(f"IMPOSSIBLE\n")
