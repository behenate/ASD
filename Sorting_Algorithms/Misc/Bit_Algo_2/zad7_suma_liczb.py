from random import randint, seed
"""
Sprawdź czy z liczb z tablic A i B (po jednej z każdej) da się utworzyć jakąkolwiek wartośc z tablicy C 
"""

def partition(tab, p, r):
    last = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= last:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    if p < r:
        i = partition(tab, p, r)
        quicksort(tab, p, i - 1)
        quicksort(tab, i + 1, r)


def a_plus_b(arr_a, arr_b, arr_c):
    quicksort(arr_a, 0, len(arr_a) - 1)
    quicksort(arr_b, 0, len(arr_b) - 1)
    is_there = False
    for c in arr_c:
        a = 0
        b = len(arr_b)-1
        sum = arr_a[a] + arr_b[b]
        while sum != c:
            sum = arr_a[a] + arr_b[b]
            if sum < c:
                if a == len(arr_a)-1:
                    break
                a += 1
            elif sum > c:
                if b == 0:
                    break
                b -= 1
            else:
                break
        if sum == c:
            print(sum)
            return True
    return False


n = 5

arr_a = [randint(1, 10) for _ in range(n)]
arr_b = [randint(1, 10) for _ in range(n)]
arr_c = [randint(1, 123) for _ in range(n)]
print(arr_a, arr_b, arr_c)
print(a_plus_bi(arr_a, arr_b, arr_c))
