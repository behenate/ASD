A = [1, 5, 4, 1, 3, 100, 2]


def play(A):
    def play_recur (i, j):
        if i >= n or j < 0 or i>j:
            return 0
        print(i,j)
        if F[i][j] != 0:
            return F[i][j]
        F[i][j] = max(A[i] + min(play_recur(i+1, j-1), play_recur(i+2, j)),
                      A[j] + min(play_recur(i+1, j-1), play_recur(i, j-2)))
        return F[i][j]
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i] = A[i]
    play_recur(0, n-2)
    for line in F:
        print(line)
    print(F[0][n-2])
play(A)