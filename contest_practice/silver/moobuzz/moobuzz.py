with open("moobuzz.in", "r") as f:
    n = int(f.readline().strip())

oldmoos = 0
newmoos = 0
counter = n
while True:
    newmoos = counter // 3 + counter // 5 - counter // 15
    counter += newmoos - oldmoos
    if newmoos - oldmoos == 0:
        break

    oldmoos = newmoos

with open("moobuzz.out", "w") as f:
    f.write(str(counter))
