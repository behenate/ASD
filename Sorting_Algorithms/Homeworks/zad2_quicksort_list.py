from random import randint, seed


class Node:
    def __init__(self, value=None, next=None):
        self.next = next
        self.value = value


def partition(pivot):
    pivot_head = pivot
    left = Node(0)
    right = Node(0)
    left_head = left
    right_head = right
    curr = pivot.next
    while curr is not None:
        if curr.value < pivot.value:
            left.next = curr
            left = left.next
        elif curr.value > pivot.value:
            right.next = curr
            right = right.next
        else:
            pivot.next = curr
            pivot = pivot.next
        curr = curr.next
    left.next = right.next = pivot.next = None
    left_head = left_head.next
    right_head = right_head.next
    return left_head, pivot_head, pivot, right_head


def qsort_wrapped(L):
    l1, p1, p2, r1 = partition(L)
    grp = p1
    grq = p2
    if l1 is not None:
        grp, grq = qsort_wrapped(l1)
        grq.next = p1
        grq = p2
    if r1 is not None:
        p2.next, grq = qsort_wrapped(r1)
    return grp, grq

# Funkcja pomocnicza aby zwracać jedną wartość zamiast dwóch bez stosowania ifow w każdej rekurencji qsort
def qsort(L):
    return qsort_wrapped(L)[0]

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
