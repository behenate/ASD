def find(n):
    n_2 = 2
    n_1 = 3
    for i in range(2, n):
        tmp = n_2+n_1
        n_2 = n_1
        n_1 = tmp
    print(n_1)

find(10)