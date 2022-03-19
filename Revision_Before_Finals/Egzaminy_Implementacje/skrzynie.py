from math import inf


class Box:
    def __init__(self, weight, strength):
        self.w = weight
        self.s = strength

    def __gt__(self, other):
        return self.w + self.s > other.w + other.s

    def __lt__(self, other):
        return self.w + self.s < other.w + other.s


def tallest_tower(B):
    n = len(B)
    for i in range(n):
        B[i] = Box(B[i][0], B[i][1])
    B = sorted(B, reverse=True)
    F = [[inf for _ in range(n)] for _ in range(n)]
    W = [[inf for _ in range(n)] for _ in range(n)]
    F[0][0] = B[0].w
    W[0][0] = B[0].s
    for i in range(1, n):
        if F[i-1][0] > B[i].w:
            F[i][0] = B[i].w
            W[i][0] = B[i].s
        else:
            F[i][0] = F[i-1][0]
            W[i][0] = W[i-1][0]
    for i in range(1,n):
        for j in range(1,n):
            F[i][j] = F[i-1][j]
            W[i][j] = W[i-1][j]
            if B[i].w <= W[i-1][j-1] and F[i][j] > F[i-1][j-1] + B[i].w:
                F[i][j] = F[i-1][j-1] + B[i].w
                W[i][j] = min(W[i-1][j-1]-B[i].w, B[i].s)
    for line in F:
        print(line)


boxes = [(10, 20), (5, 10), (6, 7), (1, 30)]
tallest_tower(boxes)
