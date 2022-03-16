def find_start(i, j, T):
    m = len(T[0])
    n = len(T)
    F = [[-1 for _ in range(m)] for _ in range(n)]
    print(F)
    max_len = 1
    max_len = find_path(i, j, None, None, T, F)
    for line in F:
        print(line)
    return max_len


def find_path(i, j, p_i, p_j, T, F):
    max_len = 1
    m = len(T[0])
    n = len(T)
    if F[i][j] != -1:
        return F[i][j]
    if i - 1 >= 0 and T[i - 1][j] > T[i][j] and (p_i is None or p_i != i-1):
        max_len = max(max_len, find_path(i - 1, j, i, j, T, F) + 1)
    if i + 1 < n and T[i + 1][j] > T[i][j] and (p_i is None or p_i != i+1):
        max_len = max(max_len, find_path(i + 1, j, i, j, T, F) + 1)
    if j - 1 >= 0 and T[i][j - 1] > T[i][j] and (p_j is None or p_j != j-1):
        max_len = max(max_len, find_path(i, j - 1, i, j, T, F) + 1)
    if j + 1 < m and T[i][j + 1] > T[i][j] and (p_j is None or p_j != j+1):
        max_len = max(max_len, find_path(i, j + 1, i, j, T, F) + 1)

    F[i][j] = max_len
    return max_len

# T = [
#     [1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]
# ]
T = [
    [1, 2, 3],
    [2, 9, 33],
    [7, 11, 5]
]
print(find_start(1,0,T))