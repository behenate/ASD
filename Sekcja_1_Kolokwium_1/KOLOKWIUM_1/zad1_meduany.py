from zad1testy import runtests

def partition(tab, p, r):
    last = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= last:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def select(tab, p, r, k):
    if p==r:
        return tab[p]
    q = partition(tab, p, r)
    if q == k:
        return tab[q]
    elif k < q:
        return select(tab, p, q - 1, k)
    else:
        return select(tab, q + 1, r, k)


def quicksort(tab, p, r):
    if p < r:
        i = partition(tab, p, r)
        quicksort(tab, p, i - 1)
        quicksort(tab, i + 1, r)

def Median(T):
    n = len(T)
    num_elems = n**2
    in_data = [0]*num_elems
    c = 0
    for sub in T:
        for elem in sub:
            in_data[c] = elem
            c+=1
    quicksort(in_data, 0, num_elems-1)
    print(in_data)
    medians = [0]*n
    m_p = ((num_elems-n) // 2) -1
    m_q = m_p+n-1
    for i in range(n):
        medians[i] = select(in_data,0,num_elems-1, m_p+i)
    print(medians, "<<Medians")
    for i in range(n):
        T[i][i] = medians[n - i - 1]
    for line in T:
        print(line)
    c = len(in_data)-1

    for i in range(n):
        for j in range(i + 1, n):
            T[i][j] = in_data[c]
            c -= 1
            if c == m_q:
                c = m_p-1
    c = 0
    for i in range(n-1,-1,-1):
        for j in range(i):
            T[i][j] = in_data[c]
            c += 1
    print("res:")
    for line in T:
        print(line)
    # tu prosze wpisac wlasna implementacje
    return

# T2 = [ [2,3,5], [11,7,13], [17,19,23] ]
T4 = [ [43, 74, 53, 97], [80, 61, 61, 19], [61, 73, 89, 93], [42, 17, 89, 80] ]
Median(T4)


# runtests( Median )
