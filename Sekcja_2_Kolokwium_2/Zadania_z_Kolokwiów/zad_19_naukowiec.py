from math import inf

def pick_sum(nums):
    n = len(nums)
    F = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i] = 0
    for i in range(n-1):
        F[i][i+1] = abs(nums[i] + nums[i+1])

    for a in range(2, n):
        for b in range(n-a):
            # i - początek przedziału - włącznie
            # j - koniec przedziału - włącznie
            i = b
            j = a+b
            s = abs(sum(nums[i:j+1]))
            for k in range(i, j):
                print(i,j," " , k, " ", i ,i+k, "  ", i+k+1, j )
                F[i][j] = min(F[i][j], max(F[i][k], F[k+1][j]))
            F[i][j] = max(F[i][j], s)

    for line in F:
        print(line)
    print(F[0][n-1])
_nums = [-1, 3, -3, 1, 2]
pick_sum(_nums)

