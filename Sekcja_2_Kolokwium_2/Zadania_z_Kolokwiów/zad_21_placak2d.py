def backpack(v, w, h, m_w, m_h):
    n = len(v)
    F = [[[0 for _ in range(m_h+1)] for _ in range(m_w + 1)] for _ in range(n)]
    F[0][w[0]][h[0]] = v[0]

    for i in range(n):
        for j in range(m_w+1):
            for k in range(m_h+1):
                if j == w[i] and k == h[i]:
                    F[i][j][k] = v[i]
                F[i][j][k] = max(F[i-1][j][k], F[i][j][k])
                if j - w[i] >= 0 and k - h[i] >= 0:
                    F[i][j][k] = max(F[i-1][j][k], F[i-1][j-w[i]][k-h[i]] + v[i], F[i][j][k])
    for i in range(m_w+1):
        for j in range(m_h+1):
            print(F[n-1][i][j], end=" ")
        print()
_v = [1, 2, 2, 3]
_h = [1, 2, 3, 2]
_w = [1, 2, 1, 2]
m_w = 10
m_h = 10
backpack(_v, _w, _h, m_w, m_h)