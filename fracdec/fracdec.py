"""
ID: alexlu.1
LANG: PYTHON3
TASK: fracdec
"""
with open("fracdec.in", "r") as f:
    n, d = [int(x) for x in f.readline().strip().split()]

# decimal = str(n/d)
# print(decimal)

# integers, decimal = decimal.split(".")

# digit_chain = [None for i in range(10)]
# last_digit = None
# repeating_digits = None
# for digit in decimal:
#     print(digit)
#     if digit_chain[int(digit)]:
#         last_digit = digit
#         repeating_digits = digit_chain[int(digit)]
#         break


#     digit_chain[int(digit)] = digit
#     for old_digit in digit_chain:
#         if old_digit:
#             old_digit += digit

# print(integers + "." + decimal[:decimal.index(last_digit)] + repeating_digits)

def infinity():
    index = 0
    while True:
        yield index
        index += 1

decimals = ""
rem = [None for i in range(100000)]
result = str(n//d) + "."
remainder = n % d
for i in infinity():
    if remainder == 0: 
        if i == 0:
            result += "0"
            break
        else:
            result += decimals
            break

    if rem[remainder] != None:
        k = rem[remainder]
        non_repeat = decimals[:k]
        repeat = decimals[k:]
        if repeat:
            repeat = f"({repeat})"
        result += non_repeat
        result += repeat
        print(f"k: {k} {decimals}")
        break
    rem[remainder] = i
    n = remainder * 10
    decimals += str(n//d)
    remainder = n % d

print(result)
    # print(numerator, result, remainder, rem[remainder], i)


# if repeat:
#     result = str(int(non_repeat[:len(n)-1])) + "." + non_repeat[len(n)-1:] + "(" + str(repeat) + ")"
# else:
#     result = str(int(non_repeat[:len(n)-1])) + "." + non_repeat[len(n)-1:]
# print(result)
# print()
result = [result[i:i+76] for i in range(0, len(result), 76)]
with open("fracdec.out", "w") as f:
    for line in result:
        f.write(f"{line}\n")

