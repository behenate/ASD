"""Na wykładzie podaliśmy algorytm działający w czasie O(n
2
). Proszę podać algorytm o złożoności
O(nlog n)""
def longest_common_subsequence(a, b):
    n = len(a)
    F = [[1 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        if a[0] < b[i]:
            for j in range(i, n):
                F[0][j] = 2
            break
    for i in range(1, n):
        if a[i] > b[0]:
            for j in range(i, n):
                F[j][0] = 2
            break
    for i in range(1, n):
        for j in range(1, n):
            F[i][j] = F[i][j - 1]
            F[i][j] = max(F[i][j], F[i - 1][j])
            if a[i] < b[j]:
                F[i][j] = max(F[i][j], F[i - 1][j - 1] + 1)

    for line in F:
        print(line)


a = [7, 8, 2, 3, 4]
b = [7, 8, 2, 3, 4]

longest_common_subsequence(a, b)
