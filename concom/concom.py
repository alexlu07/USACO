"""
ID: alexlu.1
LANG: PYTHON3
TASK: concom
"""
import pprint

class Cell:
    def __init__(self, direct):
        self.direct = direct
        self.children = 0

with open("concom.in", "r") as f:
    n = int(f.readline().strip())
    triples = [[int(x) for x in f.readline().strip().split()] for line in range(n)]
    owns = [[0 for j in range(101)] for i in range(101)]
    controls = [[0 for j in range(101)] for i in range(101)]

def addcontroller(i, j):
    if controls[i][j]:
        return

    controls[i][j] = 1
    for k in range(101):
        owns[i][k] += owns[j][k]

    for k in range(101):
        if owns[i][k] > 50:
            addcontroller(i, k)

def addowner(i, j, p):
    for k in range(101):
        if controls[k][i]:
            owns[k][j] += p

    for k in range(101):
        if owns[k][j] > 50:
            addcontroller(k, j)

for i in range(101):
    controls[i][i] = 1

for i, j, p in triples:
    addowner(i, j, p)




    # companies = {index+1: name for index, name in enumerate(set([company for triple in triples for company in triple[:2]]))}
    # rev_companies = dict([reversed(i) for i in companies.items()])
    # table = [[Cell(0) for j in range(len(companies)+1)] for i in range(len(companies)+1)]
    # for i, j, p in triples:
    #     table[rev_companies[j]][rev_companies[i]].direct = p
    # print(companies)

# original_table = table.copy()
# def print_table(table, children, height=len(companies)+1, width=len(companies)+1):
#     for i in range(height):
#         print(i, " " * (5-len(str(i))), end="")
#     print()
#     print("=" * (height) * 6)
#     for i in range(1, height):
#         print(" ", i, " " * (2-len(str(i))), end="|")
#         for j in range(1, width):
#             if children:
#                 print(f"{table[j][i].children}{' ' * (6-len(str(table[j][i].children))) if j < width-1 else ''}", end="")
#             else:
#                 print(f"{table[j][i].direct}{' ' * (6-len(str(table[j][i].direct))) if j < width-1 else ''}", end="")
#         print()

# # print_table(table, False, 50, 50)
# size = len(companies)+1

# for i, x in enumerate(table):
#     print(i, " " * (2-len(str(i))), x[34].children, " " * (2-len(str(x[34].children))), x[79].children)

# def backtrack(owned, original_owned, amount, depth):

#     for owner, p in enumerate(table[owned]):
#         # print(owner, owned, p, amount)
#         if p.direct and owner != owned and (owned, owner) not in visited:
#              if p.direct > 50:
#                 table[original_owned][owner].children += amount
#                 if owner == 34 or owner == 79:
#                     print(depth, owned, owner, table[owned][owner].children, amount)
#                 if table[original_owned][owner].children > 50:
#                     table[original_owned][owner].direct = 500
#                 # print(f"========== {owner} =========")
#                 visited.append((owned, owner))
#                 backtrack(owner, original_owned, amount, depth+1)

# # for owned, owners in enumerate(table):
# #     for owner, p in enumerate(owners):

# for owned in range(size):
#     for owner in range(size):
#         cell = table[owned][owner]
#         if cell.direct > 0:
#             visited = []
#             # print(f"============ {owner} {owned} ==================")
#             backtrack(owner, owned, cell.direct, 0)

# print("==========")
# # print_table(table, False, 50, 50)
# for i, x in enumerate(table):
#     print(i, " " * (2-len(str(i))), x[34].children, " " * (2-len(str(x[34].children))), x[79].children)


with open("concom.out", "w") as f:
    for i in range(101):
        for j in range(101):
            if i != j and controls[i][j]:
                f.write(f"{i} {j}\n")

