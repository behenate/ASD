def partition(tab, p, r):
    last = tab[r][0]
    i = p - 1
    for j in range(p, r):
        if tab[j][0] <= last:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    if p < r:
        i = partition(tab, p, r)
        quicksort(tab, p, i - 1)
        quicksort(tab, i + 1, r)


def ranges(T):
    ln = 0
    l = r = 0
    max_l = max_r = 0
    max_ln = 0
    c_c_x = 0
    i=0
    while i < len(T):
        if T[i][0] == l:
            ln += 1
            if T[i][1] > r:
                r = T[i][1]
        else:
            if i > 0 and T[i-1][0] != T[i][0]:
                c_c_x = i
            if T[i][1] <= r:
                ln += 1
            else:
                if ln > max_ln:
                    max_ln = ln
                    max_l = l
                    max_r = r
                ln = 0
                l = T[c_c_x][0]
                r = T[c_c_x][1]
                i = c_c_x
                print("i", c_c_x, i)
        i += 1
    if ln > max_ln:
        max_ln = ln
        ln = 0
        max_l = l
        max_r = r

    return max_l, max_r


lalala = [[1, 3], [5, 8], [6, 7], [6, 8], [2,5], [2, 3], [1, 4], [7, 8], [1,2]]
quicksort(lalala, 0, len(lalala) - 1)
print(lalala)
print(ranges(lalala))
