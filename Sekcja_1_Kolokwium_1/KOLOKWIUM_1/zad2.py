"""
Wojciech Dróżdż
Rozwiązanie wykorzystuje implementację merge sorta na listach.
Jego szybkosć jest niezależna od k i wynosi
O(nlog(n))
złożoność pamięciowa to O(n) - w czasie mergowania wymagane jest O(n) dodatkowej pamieci

"""

from zad2testy import runtests
from math import ceil, floor


# Wprowadziłem delikatną zmianę w Node dla "ułatwienia życia"
class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None


def merge(l1, l2):
    # Zakladam ze wartosci sa wieksze od -999999999999999
    merged = Node(-999999999999999)
    m_h = merged
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            merged.next = l1
            l1 = l1.next
        else:
            merged.next = l2
            l2 = l2.next
        merged = merged.next
    while l1 is not None:
        merged.next = l1
        l1 = l1.next
        merged = merged.next
    while l2 is not None:
        merged.next = l2
        l2 = l2.next
        merged = merged.next
    return m_h.next


def merge_lists(lst, n):
    p = lst
    q = None
    if n > 1:
        for i in range((n // 2) - 1):
            lst = lst.next
        q = lst.next
        lst.next = None
        l1 = merge_lists(p, floor(n / 2))
        l2 = merge_lists(q, ceil(n / 2))
        return merge(l1, l2)
    return lst


def SortH(p, k):
    tmp = p
    n = 0
    while tmp is not None:
        tmp = tmp.next
        n += 1
    res = merge_lists(p, n)
    return res


runtests( SortH )
