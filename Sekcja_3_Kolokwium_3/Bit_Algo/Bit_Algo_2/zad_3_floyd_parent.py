from math import inf

_G = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, -2, 0, 0],
    [0, 0, 0, 2, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, -2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def floyd_warshall(G, s, e):
    n = len(G)
    S = [[G[i][j] if G[i][j] != 0 else inf for j in range(n)] for i in range(n)]
    P = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            P[i][j] = i
    for t in range(n):
        for i in range(n):
            for j in range(n):
                tmp = S[i][j]
                S[i][j] = min(S[i][j], S[i][t] + S[t][j])
                if S[i][j] != tmp:
                    P[i][j] = P[t][j]
    path = []
    p = e
    while p != s:
        path.append(p)
        if P[s][p] != -1:
            p = P[s][p]
        else:
            p = s
    path.append(p)
    path.reverse()
    print(path)
    for line in S:
        print(line)

floyd_warshall(_G, 0 ,8)