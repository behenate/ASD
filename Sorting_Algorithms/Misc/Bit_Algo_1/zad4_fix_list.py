"""
5. Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k]. Zamieniono 10 liczb z tej tablicy na
 losowe liczby spoza tego zakresu (np. dużo większe lub ujemne). Napisz algorytm, który posortuje tablicę w czasie O(n).
"""
from random import randint, seed
from math import floor, log10


def count_sort(tab, digit, digits_num):
    n = len(tab)
    b = [0] * n
    c = [0] * digits_num

    def get_digit(num, digit):
        db = 10 ** digit
        bd = 10 ** (digit - 1)
        ret = int((num % db) // bd)
        return ret

    for i in range(5, n - 5):
        elem = tab[i]
        c[get_digit(elem, digit)] += 1
    print(c)
    for i in range(1, digits_num):
        c[i] = c[i] + c[i - 1]
    for k in range(n - 6, 4, -1):
        c[get_digit(tab[k], digit)] -= 1
        b[c[get_digit(tab[k], digit)] + 5] = tab[k]
    for i in range(5):
        b[i] = arr[i]
    for i in range(n - 5, n):
        b[i] = arr[i]
    return b


def radix_sort(tab, k):
    for i in range(k):
        tab = count_sort(tab, i + 1, 10)
    return tab


def insertion_sort(tab, p, q):
    for j in range(p + 1, q):
        key = tab[j]
        i = j - 1
        while i >= p and tab[i] > key:
            tab[i + 1] = tab[i]
            i -= 1
        tab[i + 1] = key


def sort_broken_list(arr, k):
    n = len(arr)
    s_i = 0
    b_i = n - 1
    i = 0
    while i < n - 5:
        if arr[i] < 0:
            arr[s_i], arr[i] = arr[i], arr[s_i]
            s_i += 1
        elif arr[i] > k:
            arr[b_i], arr[i] = arr[i], arr[b_i]
            b_i -= 1
            i -= 1
        i += 1
    arr = radix_sort(arr, floor(log10(k) + 1))
    insertion_sort(arr, 0, 5)
    insertion_sort(arr, n - 5, n)


k = 20
n = 20
seed("Dasia Boncer")
arr = [randint(0, k) for _ in range(n)]
for i in range(0, 5):
    arr[floor(i * n / 10)] = randint(-30, -1)
for i in range(5, 10):
    arr[floor(i * n / 10)] = randint(k + 1, k + 100)
sort_broken_list(arr, k)
