from copy import copy
from time import time


def reverse_arr(arr):
    i = 0
    j = len(arr) - 1
    while j - i > 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


# Longest decreasing subsequence
def lds(arr):
    n = len(arr)
    lengths = [1] * n
    extends = [[] for _ in range(n)]
    max_length = 0
    for i in range(1, n):
        local_max_length = 1
        for j in range(i, -1, -1):
            # Jeśli długość jest większa wyczyść extends na j i wstaw nowe, prawidłowe przedłużenie
            if arr[j] > arr[i] and lengths[j] + 1 > local_max_length:
                local_max_length = lengths[j] + 1
                # Jeżeli ta maksymalna lokalna długość jest większa od tej głównej to ją zastąp
                max_length = max(max_length, local_max_length)
                extends[i] = [j]
            # Jeśli długość  jest równa aktualnej maksymalnej to jest kilka potencjalnie najdłuższych podciągów
            elif arr[j] > arr[i] and lengths[j] + 1 == local_max_length:
                extends[i].append(j)
            lengths[i] = local_max_length

    total = 0
    print(extends)
    for i in range(n - 1, -1, -1):
        if lengths[i] == max_length:
            total += print_solution(arr, extends, i, [0]*max_length)
    return total


def print_solution(arr, extends, current_index, append_tab, insert_i=0, tab_index=0):
    if len(extends[current_index]) == 0:
        append_tab[tab_index] = arr[current_index]
        for elem in append_tab:
            print(elem, end=" ")
        print("")
        return 1

    cnt = 0
    for i in range(len(extends[current_index])):
        append_tab[tab_index] = arr[current_index]
        cnt += print_solution(arr, extends, extends[current_index][i], append_tab, insert_i+1, tab_index+1)
    return cnt


def printAllLIS(A):
    reverse_arr(A)
    return lds(A)


start = time()
# _arr = [3, 1, 5, 7, 2, 4, 3]
_arr = [10 * k + i for k in range(8) for i in range(6, 0, -1)]
print(printAllLIS(_arr))
print(time() - start)
