# Python program for implementation of Quicksort  

def partition(tab, p, r):
    last = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= last:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1

def quicksort_iterative(tab):
    p = 0
    r = len(tab)-1
    stack = [0]*len(tab)
    index = -1

    index += 1
    stack[index] = p
    index += 1
    stack[index] = r

    while index >= 0:
        r = stack[index]
        index -= 1
        p = stack[index]
        index -= 1

        q = partition(tab, p, r)

        if p < q-1:
            index += 1
            stack[index] = p
            index += 1
            stack[index] = q - 1

        if r > q+1:
            index += 1
            stack[index] = q+1
            index += 1
            stack[index] = r

arr = [2,4,6,7,4,2,3,5,6,8,5,4]
quicksort_iterative(arr)
print(arr)