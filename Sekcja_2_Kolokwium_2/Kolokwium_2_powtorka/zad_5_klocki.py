from math import inf


def remove_min(blocks):
    blocks = sorted(blocks, key =lambda x: x[1])
    print(blocks)
    n = len(blocks)
    F = [inf for _ in range(n)]
    F[0] = 0
    for i in range(1, n):
        F[i] = i
        for k in range(i-1):
            if blocks[k][1] <= blocks[i][0]:
                F[i] = min(F[i], F[k] + i-k-1)
    print(F)



_blocks = [[0, 3], [2, 5], [4, 6], [5, 7], [6, 10], [9, 12], [12, 15], [11, 17], [14, 18], [17, 19]]
remove_min(_blocks)
