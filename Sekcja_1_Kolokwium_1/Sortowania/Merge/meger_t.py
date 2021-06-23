def merge(tab, p, q, r):
    left = tab[p:q]
    right = tab[q:r]
    if len(left) == 1:
        print(left)
    if len(right) == 1:
        print(right)
    left.append(9999999)
    right.append(9999999)
    i = 0
    j = 0
    for k in range(p, r):
        if left[i] <= right[j]:
            tab[k] = left[i]
            i += 1
        else:
            tab[k] = right[j]
            j += 1

arr = [3,5,7,9,1,2,4,6,8,9]
merge(arr, 0, 4, len(arr))
print(arr)