from random import randint, seed
from time import time


def count_sort(tab, digit, digits_num):
    n = len(tab)
    b = [0] * n
    c = [0] * digits_num

    def get_digit(num, digit):
        db = 10 ** digit
        bd = 10 ** (digit - 1)
        ret = int((num % db) // bd)
        return ret

    for elem in tab:
        c[get_digit(elem, digit)] = c[get_digit(elem, digit)] + 1

    for i in range(1, digits_num):
        c[i] = c[i] + c[i - 1]

    for k in range(n - 1, -1, -1):
        c[get_digit(tab[k], digit)] -= 1
        b[c[get_digit(tab[k], digit)]] = tab[k]
    return b


def radix_sort(tab, k):
    for i in range(k):
        tab = count_sort(tab, i + 1, 10)
    return tab


seed(420)

n = 100

test_tab = [randint(0, 100) for _ in range(n)]
start = time()
test_tab = radix_sort(test_tab, 3)
print(time() - start)
print(test_tab)
