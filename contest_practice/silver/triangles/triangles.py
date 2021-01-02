import bisect
with open("triangles.in", "r") as f:
    n = int(f.readline().strip())
    x_axis = []
    y_axis = []
    for i in range(n):
        coords = [int(x) for x in f.readline().strip().split()]
        bisect.insort_left(x_axis, coords)
        bisect.insort_left(y_axis, [coords[1], coords])

        
