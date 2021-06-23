def matrioszki(A):
    A = sorted(A)
    n = len(A)
    F = [1 for _ in range(n)]
    for i in range(1, n):
        print("A", A[i])
        for j in range(i):
            print(A[j])
            if A[j][1] < A[i][1] and A[j][0] < A[i][0]:
                F[i] = max(F[i], F[j]+1)
    print(A)
    print(F)
    print(max(F))

_A = [[2, 4], [1, 3], [2, 3], [4, 10]]
matrioszki(_A)