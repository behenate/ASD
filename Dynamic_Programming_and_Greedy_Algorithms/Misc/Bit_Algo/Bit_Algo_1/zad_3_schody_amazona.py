def amanzonka(arr):
    n = len(arr)
    jumps = [0] * n
    jumps[0] = 1
    for i in range(1, n):
        for j in range(i):
            if j + arr[j] >= i:
                jumps[i] += jumps[j]
    print(jumps)


arr = [1, 3, 2, 2, 1, 0]
amanzonka(arr)
