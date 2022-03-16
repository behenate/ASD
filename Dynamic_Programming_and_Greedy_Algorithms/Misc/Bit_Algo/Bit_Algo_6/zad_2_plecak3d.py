ceny = [1, 2, 3]
wagi = [1, 2, 1]

def plecaki_sposoby(ceny, wagi, w, min_cena):
    n = len(ceny)
    m = w + 1
    l = sum(ceny) + 1
    F = [[[0 for _ in range(l)] for _ in range(m)] for _ in range(n)]
    F[0][wagi[0]][ceny[0]] = 1
    for i in range(1, n):
        for j in range(m):
            for k in range(l):
                # j = 1 k = 3
                F[i][j][k] = F[i-1][j][k]
                if j == wagi[i] and k == ceny[i]:
                    F[i][j][k] += 1
                if j-wagi[i] >= 0 and k-ceny[i] >= 0:
                    F[i][j][k] += F[i-1][j-wagi[i]][k-ceny[i]]

    for cell in F:
        print("")
        for line in cell:
            print(line)
    cnt = 0
    for i in range(min_cena, l):
        for j in range(m):
            cnt += F[n-1][j][i]
    print(cnt)

plecaki_sposoby(ceny, wagi, 1, 0)
