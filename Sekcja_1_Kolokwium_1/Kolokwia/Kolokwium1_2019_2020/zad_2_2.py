def countsort(tab, k, p, q):
    n = len(tab)
    b = [0] * len(tab)
    c = [0] * k

    for elem in tab:
        c[149 - (elem - 150)] += 1

    for i in range(1, k):
        c[i] += c[i - 1]

    for i in range(n - 1, -1, -1):
        c[149 - (tab[i] - k)] -= 1
        b[c[149 - (tab[i] - k)]] = tab[i]
    return b[p:q]


t = [150, 169, 179, 189, 189, 210, 222, 205, 193, 188]
t = countsort(t, 150, 0, 10)
print(t)
