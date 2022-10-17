from io import TextIOWrapper

def same_path(entry1, entry2, entry2set):
    if entry1[0] != entry2[0]: return False

    entry1set = set(entry1[1])

    order1 = [i for i in entry1[1] if i in entry2set]
    order2 = [i for i in entry2[1] if i in entry1set]

    return order1 == order2

def solve(f):
    n, m = [int(i) for i in f.readline().strip().split()]

    ongoing_bracelets = set()
    killed_bracelets = set()
    columns = [] # [ a column: { 4: [[stack: 1, 2], [order: 3]], 
                 #               5: [[stack: 1, 2], [order: 3, 4]],
                 #             } 
                 # ]
    return_false = False
    for c in range(m):
        if return_false:
            f.readline()
            continue
        column = {}
        stack = [[-1, []]] # [[stack=4, contents=5, 6]]
        seen = set()
        skipped = False
        for i in f.readline().strip().split():
            if not skipped:
                skipped = True
                continue
            x = int(i)
            if x in killed_bracelets:
                return False
            if x not in seen:
                stack.append([x, []])
                seen.add(x)
            else:
                x_container = stack.pop()
                if x_container[0] == x:
                    entry = [[s[0] for s in stack], stack[-1][1].copy()]
                    if columns and x in columns[-1]:
                        if not same_path(entry, columns[-1][x], columns[-1]): 
                            return_false = True
                            break
                    column[x] = entry
                    stack[-1][1].append(x)
                else:
                    return_false = True
                    break
        if len(stack) > 1:
            return_false = True
        
        if return_false:
            continue

        columns.append(column)
        killed_bracelets = ongoing_bracelets - seen
        ongoing_bracelets = seen

    return False if return_false else True
            


with open("bracelet.in", "r") as f:
    t = int(f.readline().strip())

    for i in range(t):
        f.readline()
        print("YES") if solve(f) else print("NO")

# t = int(input().strip())
# for i in range(t):
#     input()
#     print("YES") if solve() else print("NO") 