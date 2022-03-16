"""
Dany jest zbiór przedziałów otwartych A = {(a1, b1), ...,(an, bn)}. Proszę zaproponować algorytm
(bez implementacji), który znajduje taki zbiór X, X ⊆ {1, ..., n} że (a) |X| = k (gdzie k ∈ N to
dany parametr wejściowy), (b) dla każdych i, j ∈ X, przedziały (ai
, bi) oraz (aj
, bj ) nie nachodzą
na siebie, oraz (c) wartość maxj∈Xbj − mini∈Xai
jest minimalna. Jeśli podzbioru spełniającego
warunki (a) i (b) nie ma, to algorytm powinien to stwierdzić. Algorytm powinien być możliwie
jak najszybszy (ale przede wszystkim poprawny)."""

przedzialy = [
    (1, 3),
    (1.5, 2.5),
    (3, 5),
    (3, 8),
    (6, 7),
    (7, 8),
    (8, 9),
    (10, 11),
    (11, 12),
    (9, 13,),
    (9, 12)
]
def find_k(rngs, k=4):
    rngs = sorted(rngs, key=lambda x:x[1])
    n = len(przedzialy)
    res = [() for _ in range(n)]
    best = (-1, 1000000000000)
    for i in range(n):
        c_l = rngs[i][1] - rngs[i][0]
        a_i = i
        c_c = 1
        c_i = i
        while c_c < k:
            while a_i < n and rngs[a_i][0] < rngs[c_i][1]:
                a_i += 1
            if a_i == n:
                break
            c_l += (rngs[a_i][0] - rngs[c_i][1] + (rngs[a_i][1] - rngs[a_i][0]))
            c_c += 1
            c_i = a_i
            a_i += 1
        if c_c == k and c_l < best[1]:
            best = (c_c, c_l)
        res[i] = (c_c, c_l)
    print(res)
    print(best)
    if best[0] == -1:
        print("NIE ISTNIEJE!!!")
find_k(przedzialy)
