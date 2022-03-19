
def find_sum(A, sum):
    n = len(A)
    F = [[0 for _ in range(sum+1)] for _ in range(n)]
    for i in range(n):
        F[i][0] = 1
    if A[0] < sum:
        F[0][A[0]] = 1
    for i in range(1, n):
        for j in range(1, sum+1):
            F[i][j] = F[i-1][j]
            if j-A[i] >= 0:
                F[i][j] = F[i][j] or F[i-1][j-A[i]]
    for line in F:
        print(line)
    print(F[-1][sum])
    return F[-1][sum]


A = [1000,6,5,8,3]

find_sum(A, 8)