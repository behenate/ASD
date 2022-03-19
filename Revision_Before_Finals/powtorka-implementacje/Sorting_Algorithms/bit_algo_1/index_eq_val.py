arr = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def find(arr):
    n = len(arr)
    p = 0
    r = n-1
    while p<=r:
        q = (p+r) // 2
        if arr[q] == q:
            return q
        elif arr[q] < q:
            p = q+1
        else:
            r = q-1
    return -1
print(find(arr))
