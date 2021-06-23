from zad3testy import runtests


def insertion_sort(tab):
    for j in range(1, len(tab)):
        key = tab[j]
        i = j - 1
        while i >= 0 and tab[i] > key:
            tab[i + 1] = tab[i]
            i -= 1
        tab[i + 1] = key


def SortTab(T, P):
    n = len(T)
    amounts = [0]*(n)
    total = 0
    for elem in P:
        for i in range(elem[0], elem[1]+1):
            amounts[i-1] += 1
            total += 1
    print(amounts)
    range_counter = 0
    new_P = []
    for i in range(len(amounts)-1):
        if T[i] == T[i+1]:
            print("no jest przecies")
        if T[i] == T[i+1] and T[i] != 0 and T[i+1] != 0:
            if range_counter >= len(new_P):
                new_P.append([i,i,0])
            else:
                new_P[range_counter][1] += 1
        else:
            if range_counter < len(new_P):
                range_counter += 1
    print(new_P)

    # tu prosze wpisac wlasna implementacje
    return


T1 = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
P1 = [(1, 5, 0.75), (4, 8, 0.25)]
SortTab(T1, P1)
