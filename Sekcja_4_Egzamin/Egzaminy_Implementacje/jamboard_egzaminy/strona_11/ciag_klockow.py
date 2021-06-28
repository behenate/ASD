A = [(1, 4), (0, 5), (1, 5), (2, 6), (2, 4)]
B = [(10, 15), (8, 14), (1, 6), (3, 10), (8, 11), (6, 15)]
def klocki(A):
    n = len(A)
    F = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
                F[i] = max(F[i], F[j]+1)
    print(F)
klocki(A)
klocki(B)