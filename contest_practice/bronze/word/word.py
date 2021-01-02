with open("word.in", "r") as f:
    n, k = [int(x) for x in f.readline().strip().split()]
    words = f.readline().strip().split()

essay = ""
counter = 0
for word in words:
    if counter + len(word) > k:
        essay += "\n"
        counter = 0
    else:
        essay += " "
    essay += word
    counter += len(word)

essay = essay[1:]

print(essay)
with open("word.out", "w") as f:
    f.write(essay)
