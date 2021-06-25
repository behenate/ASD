arr = [1, 2, 3, 4, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None]


def find_n(arr):
    n = 1
    while arr[n] != None:
        n *= 2
    print("co")
    return n


def find_x(arr, x):
    n = find_n(arr)
    l = 0
    r = n
    while l <= r:
        q = (l + r) // 2
        if arr[q] == x:
            return q
        if arr[q] is None or arr[q] > x :
            r = q - 1
        else:
            l = q + 1
    return -1


print("test")
print(find_x(arr, 5))
# testestetsetset