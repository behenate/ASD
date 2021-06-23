from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def partition(p):
    smaller = Node()
    first_smaller = smaller
    equal = Node()
    first_equal = equal
    bigger = Node()
    first_bigger = bigger
    pivot = p.value
    while p != None:
        q = p.next
        p.next = None
        if p.value < pivot:
            smaller.next = p
            smaller = p
        if p.value == pivot:
            equal.next = p
            equal = p
        if p.value > pivot:
            bigger.next = p
            bigger = p
        p = q
    return first_smaller.next, first_equal.next, first_bigger.next, smaller, equal, bigger


def sort(p):
    small, equal, big, last_small, last_equal, last_big = partition(p)
    first_b = None
    last_b = None
    last_s = None
    first_s = None
    if small is not None:
        first_s, last_s = sort(small)

    if big is not None:
        first_b, last_b = sort(big)

    if small is None:
        if big is not None:
            last_equal.next = first_b
            return equal, last_b
        else:
            return equal, last_equal
    else:  # small != None
        if big is not None:
            last_s.next = equal
            last_equal.next = first_b
            return first_s, last_b
        else:  # big == None
            last_s.next = equal
            return first_s, last_equal


def qsort(L):
    return sort(L)[0]


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
