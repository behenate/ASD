from math import inf

_G = [
    [0,1,0,0,0,0],
    [0,0,1,0,0,0],
    [0,0,0,0,1,0],
    [0,1,0,0,0,0],
    [0,0,0,1,0,1],
    [0,0,0,0,0,0],
]


def floyd_warshall(G):
    n = len(G)
    S = [[G[i][j] if G[i][j] != 0 else inf for j in range(n)] for i in range(n)]
    for t in range(n):
        for i in range(n):
            for j in range(n):
                S[i][j] = min(S[i][j], S[i][t] + S[t][j])
    for line in S:
        print(line)
    return S


floyd_warshall(_G)
