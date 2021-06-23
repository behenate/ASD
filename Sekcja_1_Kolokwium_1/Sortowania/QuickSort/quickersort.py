from random import randint


def quicker_partition(arr, p, rg):
    pivot = arr[rg]
    l = p
    r = p
    u = rg
    while r <= u:
        if arr[r] < pivot:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r += 1
        elif arr[r] > pivot:
            arr[r], arr[u] = arr[u], arr[r]
            u -= 1
        else:
            r += 1
    return l, r


def quicker_sort(arr, p, r):
    while p <= r:
        l, rg = quicker_partition(arr, p, r)
        if l-p-1 < r-rg:
            quicker_sort(arr,p, l-1)
            p = rg
        else:
            quicker_sort(arr, rg, r)
            r = l-1


test = [randint(0, 10) for i in range(1000000)]
quicker_sort(test,0, len(test)-1)
print(test)
for i in range(1, len(test)):
    if test[i-1] > test[i]:
        print("Błąd")