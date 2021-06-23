def find_who_goes(friends_map, r_z, r_n):
    n = len(friends_map)
    F = [[0 for _ in range(n)] for _ in range(n)]
    # Nikt nie zna sam siebie
    for i in range(n):
        F[i][i] = None
    Z = [0] * n
    N = [0] * n
    for i in range(n):
        for knows in friends_map[i]:
            F[i][knows] = 1
            Z[i] += 1
        N[i] = n - Z[i] - 1  # Odejmuję żeby nie było że jest w relacji znajomości sama z sobą
    for line in F:
        print(line)
    print(Z)
    print(N)
    remove_queue = []
    for i in range(n):
        if Z[i] < r_z or N[i] < r_n:
            remove_queue.append(i)
    remove_recur(F, Z, N, remove_queue, r_n, r_z)
    for line in F:
        print(line)


def remove_recur(F, Z, N, remove_queue, r_n, r_z):
    n = len(F)
    if len(remove_queue) == 0:
        return
    i = remove_queue[-1]
    for j in range(n):
        if F[i][j] == None:
            continue
        v = F[i][j]
        if v == 1:
            Z[j] -= 1
            if Z[j] < r_z:
                remove_queue.append(j)
        else:
            N[j] -= 1
            if N[j] < r_n:
                remove_queue.append(j)
        # Udawaj że osoba nigdy nie istniała
        F[i][j] = None
        F[j][i] = None
    res = remove_queue.pop()
    print("removed:", res)
    print("Knows tab:", Z)
    print("Doesnt know:", N)
    remove_recur(F, Z, N, remove_queue, r_n, r_z)


_f = [[1, 2, 3],
      [0, 5, 4],
      [0, 3, 5],
      [0, 2],
      [1],
      [1, 2]
      ]
find_who_goes(_f, 2, 1)
