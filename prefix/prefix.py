"""
ID: alexlu.1
LANG: PYTHON3
TASK: prefix
"""
with open("prefix.in", "r") as f:
    p = []
    while True:
        line = f.readline().strip()
        if line == ".":
            break
        p.append(line.split())
    p = [c for line in p for c in line]
    s = "".join(line.strip() for line in f.readlines())
    print(len(s), s[0])

results = [True] + [None for i in s]
advance = len(max(p, key=len))
for length in range(1, len(s)+1):
    # print(f"==== {length} ==== {advance}")
    if advance < 0:
        break
    advance -= 1
    for prefix in p:
        sub_length = length - len(prefix)
        # print(prefix, sub_length)
        if sub_length < 0 or s[sub_length:length] != prefix:
            continue
        if results[sub_length]:
            results[length] = True
            advance = len(max(p, key=len))
            # print(f"set to true:")
            break
    else:
        results[length] = False

# print(results)
with open("prefix.out", "w") as f:
    f.write(f"{len(results) - results[-1::-1].index(True) - 1}\n")
