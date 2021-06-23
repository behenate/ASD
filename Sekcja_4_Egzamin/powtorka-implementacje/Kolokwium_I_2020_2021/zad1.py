from zad1testy import runtests


def partition(tab, p, r, n):
    last = ct(tab, r, n)
    i = p - 1
    for j in range(p, r):
        if ct(tab, j, n) <= last:
            i = i + 1
            i_i = c(i, n)
            j_i = c(j, n)
            tab[i_i[0]][i_i[1]], tab[j_i[0]][j_i[1]] = tab[j_i[0]][j_i[1]], tab[i_i[0]][i_i[1]]
    i_i = c(i + 1, n)
    r_i = c(r, n)
    tab[i_i[0]][i_i[1]], tab[r_i[0]][r_i[1]] = tab[r_i[0]][r_i[1]], tab[i_i[0]][i_i[1]]
    # tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def select(tab, p, r, k, n):
    if p == r:
        return tab[c(p, n)[0]][c(p, n)[1]]
    q = partition(tab, p, r, n)
    if q == k:
        return tab[c(q, n)[0]][c(q, n)[1]]
    elif k < q:
        return select(tab, p, q - 1, k, n)
    else:
        return select(tab, q + 1, r, k, n)


def c(i, n):
    return i // n, i % n


def ct(tab, i, n):
    return tab[i // n][i % n]


def Median(T):
    n = len(T)
    m = n * n
    s_i = n * (n // 2)
    e_i = s_i + (n - 1)
    low = ct(T, s_i, n)
    high = ct(T, e_i, n)
    diag_cnt = 0
    for i in range(m):
        y = c(i, n)[0]
        x = c(i, n)[1]
        if low <= T[y][x] <= high and x != y:
            print("swapping", diag_cnt, y, x, T[y][x], T[diag_cnt][diag_cnt])
            T[diag_cnt][diag_cnt], T[y][x] = T[y][x], T[diag_cnt][diag_cnt]
            diag_cnt += 1
        elif low <= T[y][x] <= high and diag_cnt == x:
            diag_cnt += 1
    for line in T:
        print(line)
    i1 = 1
    j1 = 0
    i2 = 0
    j2 = 1
    while i1 < n and j1 < n - 1 and i2 < n - 1 and j2 < n:
        s_x, s_y, b_x, b_y = -1, -1, -1, -1
        # dolna przekatna
        while i1 < n and s_x == -1 and s_y ==-1:
            while j1 < i1:
                if T[i1][j1] < low:
                    s_y, s_x =i1, j1
                    break
                j1 += 1
            j1 = 0
            i1 += 1
        while j2 < n and b_x == -1 and b_y == -1:
            while i2 < j2:
                if T[i2][j2] > high:
                    b_y, b_x = i2, j2
                    break
                i2 += 1
            i2 = 0
            j2 += 1
        if s_x != -1:
            print("swap: ",T[s_y][s_x], T[b_y][b_x] )
            T[s_y][s_x], T[b_y][b_x] = T[b_y][b_x], T[s_y][s_x]
    for line in T:
        print(line)
    return


runtests(Median)

T = [
    [2, 3, 5],
    [7, 11, 13],
    [17, 19, 23]
]
Median(T)
