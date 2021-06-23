from random import randint, shuffle, seed
'''Proszę zaimplementować algorytm “magiczne piątki”, który dostaje na wejściu
tablicę liczb naturalnych A oraz liczbę k i zwraca liczbę, która po posortowaniu
tablicy A byłaby pod indeksem k. Można założyć, że wszystkie liczby w tablicy
A są parami różne. Stworzona funkcja powinna się nazywać.'''


def InsertSort(T, left, right):
    for i in range(left, right + 1):
        key = T[i]
        j = i - 1
        while key < T[j] and j >= left:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key


def median(A, left, right):
    if (right-left) <= 5:
        InsertSort(A, left, right)
        return left + (right-left)//2
    index = 0

    for i in range(left, right + 1, 5):
        if i + 4 < right + 1:
            InsertSort(A, i, i + 4)
            A[i + 2], A[index+left] = A[index+left], A[i + 2]
        else:
            InsertSort(A, i, right)
            middle = (right - i) // 2
            A[i + middle], A[index+left] = A[index+left], A[i + middle]
        index += 1
    return median(A, left, left+index-1)


def partition(T, left, right):
    x = median(T, left, right)
    T[x], T[right] = T[right], T[x]
    pivot = T[right]
    border = left - 1
    for i in range(left, right):
        if T[i] < pivot:
            border += 1
            T[i], T[border] = T[border], T[i]
    border += 1
    T[border], T[right] = T[right], T[border]
    return border



def select(A,left,right,k):
    if left == right:
        return A[left]
    q = partition(A,left,right)
    if q == k:
        return A[q]
    elif k < q:
        return select(A,left,q-1,k)
    else:
        return select(A,q+1,right,k)


def linearselect(A, k):
    x = select(A,0,len(A)-1,k)
    print(x)
    return x




A = [4,6,5,1,3,8,6,7,7,7,8,8,8,8,8]

seed(42)
print(A)
# print(median(A,5,11))
print(A)
n = 11
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")
