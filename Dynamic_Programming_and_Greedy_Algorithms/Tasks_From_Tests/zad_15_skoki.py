"""2. struct field {
int value;
int long j;
int short j;
};
Z każdego pola można skakać tylko o ilość pól zapisaną w long j lub short j. Napisać program
który zwróci maksymalną wartość jaką możemy osiągnąć pop"""
def skoki(fields, jumps):
    n = len(fields)
    jumps_from = [[] for _ in range(n)]
    for i in range(n):
        t1 = i + jumps[i][0]
        t2 = i + jumps[i][1]
        if t1 < n:
            jumps_from[t1].append(i)

        if n > t2 != t1:
            jumps_from[t2].append(i)

    F = [0 for _ in range(n)]
    F[0] = fields[0]
    parent = [-1 for _ in range(n)]
    for i in range(1, n):
        if len(jumps_from[i]) == 0:
            F[i] = -10000
        for elem in jumps_from[i]:
            s = F[i]
            F[i] = max(F[elem] + fields[i], F[i])
            if F[i] != s:
                parent[i] = elem
    print(F)
    print(parent)
    p = n-1
    while p != -1:
        print(p, end=" ")
        p = parent[p]

    return F[-1]


fields = [2, 1, 1, 3, 2, 2]
jumps = [(1, 4), (2, 3), (2, 3), (1, 2), (1, 3), (2, 5)]
skoki(fields, jumps)
