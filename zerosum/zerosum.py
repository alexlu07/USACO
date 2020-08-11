"""
ID: alexlu.1
LANG: PYTHON3
TASK: zerosum
"""
with open("zerosum.in", "r") as f:
    n = int(f.readline().strip())
    # numbers = list(" ".join([str(x) for x in range(1, n+1)]))
    numbers = list(range(1, n+1))
    print(numbers)

symbols = ["+", "-", " "]
def find_expressions(depth):
    if depth < n-1:
        for symbol in symbols:
            operations = find_expressions(depth+1)
            for operation in operations:
                yield operation + symbol
    else:
        yield ""

results = []
for operation in find_expressions(0):
    expression = [None] * (n * 2 - 1)
    expression[::2] = numbers
    expression[1::2] = operation
    expression = "".join([str(c) for c in expression])
    if not eval(expression.replace(" ", "")):
        results.append(expression)

# for i in range(1, 2 * n - 3, 2):
#     for symbol in symbols:
#         numbers_copy = numbers.copy()
#         numbers_copy[i] = symbol
#         numbers_copy = "".join(numbers_copy)
#         numbers_copy = numbers_copy.replace(" ", "")
#         print(numbers_copy)
#         if not eval(numbers_copy):
#             results += 1

with open("zerosum.out", "w") as f:
    for expression in sorted(results):
        f.write(f"{expression}\n")
