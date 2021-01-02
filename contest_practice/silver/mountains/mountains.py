# def insort(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0

#     while low < high:

#         mid = (high + low) // 2

#         if arr[mid][0] < x[0]:
#             low = mid + 1
#         elif arr[mid][0] > x[0]:
#             high = mid - 1
#         elif arr[mid][1] < x[1]:
#             high = mid - 1
#         elif arr[mid][1] > x[1]:
#             low = mid + 1

#     arr.insert(low, x)
import bisect

class Line:
    def __init__(self, s, e):
        self.start = s
        self.end = e

    def __lt__(self, other):
        if self.start < other.start:
            return True
        if self.start > other.start:
            return False
        if self.end < other.end:
            return False
        if self.end > other.end:
            return True

    def __repr__(self):
        return str(self.start) + " " + str(self.end)

with open("mountains.in", "r") as f:
    n = int(f.readline().strip())
    mountains = []
    for i in range(n):
        x, y = [int(j) for j in f.readline().strip().split()]
        bisect.insort_left(mountains, Line(x-y, x+y))

result = 0
max_end = 0
# print(mountains)
for l in mountains:
    s = l.start
    e = l.end
    # print(s, e)
    if e > max_end:
        result += 1
        max_end = e
        # print("+")

with open("mountains.out", "w") as f:
    f.write(str(result))
