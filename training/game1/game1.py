"""
ID: alexlu.1
LANG: PYTHON3
TASK: game1
"""

with open("game1.in", "r") as f:
    n = int(f.readline().strip())

    board = []
    for line in f.readlines():
        board += [int(i) for i in line.strip().split()]

scores = [[None for j in range(n)] for i in range(n)] # ij = numbers taken from each side

def minimax(l, r, player): # player: 1 = player1, -1 = player2
    if l + r == n-1:
        score = [0, 0]
        score[player] = board[l]
        scores[l][r] = [score, score]

        # print(l, r)
        # for s in scores:
        #     print("tail", s)
        return score.copy()

    saved_scores = scores[l][r]
    if saved_scores is not None:
        left = saved_scores[0]
        right = saved_scores[1]
    else:
        left = minimax(l+1, r, 1-player)
        right = minimax(l, r+1, 1-player)
        left[player] += board[l]
        right[player] += board[-1-r]

        scores[l][r] = [left, right]

    # print(l, r)
    # for s in scores:
    #     print(s)

    return max(left, right, key=lambda x: (x[player] - x[1-player])).copy()

minimax(0, 0, 0)

left = scores[0][0][0]
right = scores[0][0][1]
result = max(left, right, key=lambda x: (x[0] - x[1]))

with open("game1.out", "w") as f:
    f.write(f"{result[0]} {result[1]}\n")