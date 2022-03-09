def find_fun_index(arr):
    p = 0
    r = len(arr) - 1
    while p <= r:
        q = (p + r) // 2
        print(p, r)
        if arr[q] == q:
            return q
        elif arr[q] < q:
            p = q+1
        else:
            r = q-1



arr = [-10, -9, -8, -5, -4, -2, 0, 1, 3, 8, 10, 23, 34, 56]
print(find_fun_index(arr))