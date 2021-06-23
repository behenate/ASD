G = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 0]
]
G = [
    [0,1,1,1],
    [1,0,1,1],
    [1,1,0,1],
    [1,1,1,0]
]


def znajdz(G):
    n = len(G)
    for i in range(n):
        for j in range(i + 1, n):
            f_c_t = []
            for k in range(n):
                if G[i][k] == 1 and G[j][k] == 1:
                    f_c_t.append(k)
                    if len(f_c_t) == 2:
                        print("znaleziono: ", i, f_c_t[0], j, f_c_t[1])
                        return
znajdz(G)
