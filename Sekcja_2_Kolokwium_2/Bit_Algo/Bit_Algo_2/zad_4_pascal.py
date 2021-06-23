def pick_plates(plates_arr, guests):
    n = len(plates_arr)
    k = len(plates_arr[0])

    for i in range(n):
        for j in range(1, k):
            plates_arr[i][j] += plates_arr[i][j-1]

    F = [[-1 for _ in range(n)] for _ in range(guests)]
    for i in range(guests):
        if i < k:
            F[i][0] = plates_arr[0][i]
        else:
            F[i][0] = plates_arr[0][-1]
    for i in range(1, n):
        F[0][i] = max(F[0][i-1], plates_arr[i][0])

    for i in range(1, guests):
        for j in range(1, n):
            best = 0
            for m in range(k+1):
                print("i:{} j:{}, k:{}".format(i, j, k))
                if m == 0:
                    best = max(best, F[i][j-1])
                elif i-m >=0:
                    best = max(best, F[i-m][j-1] + plates_arr[j][m-1])
            F[i][j] = best
    for line in F:
        print(line)
plates = [[1,10,5], [5,1,3], [1,6,10]]
pick_plates(plates, 9)