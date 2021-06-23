def find_subsets(nums, t):
    n = len(nums)
    F = [[-1 for _ in range(t + 1)] for _ in range(n)]
    G = [[-1 for _ in range(t + 1)] for _ in range(n)]

    for i in range(n):
        F[i][0] = 0
    for i in range(n):
        F[i][1] = sum(nums[:i + 1])

    for j in range(2, t+1):
        for i in range(j-1, n):
            for k in range(1, i-j+3):
                tmp = F[i][j]
                F[i][j] = max(F[i][j], min(F[i-k][j-1], sum(_nums[i-k+1: i+1])))
                if F[i][j] != tmp:
                    G[i][j] = k


    cnt = t
    e = n-1
    p = G[e][cnt]
    while p != -1:
        cnt -= 1
        new_p = G[e-p][cnt]
        print(nums[e-p+1: e+1])
        e = e - p
        p = new_p
    print(nums[:e+1])
    for line in G:
        print(line)
    for line in F:
        print(line)

_nums = [2, 5, 4, 3, 4, 6, 8, 4, 2, 1]
find_subsets(_nums, 4)