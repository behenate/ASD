"""
Dana jest struktura Node opisująca listę jednokierunkową:
struct Node { Node * next; int value; };
Proszę zaimplementować funkcję Node* fixSortedList( Node* L ), która otrzymuje na
wejściu listę jednokierunkową bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że
powstała z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową
wartość. Funkcja powinna przepiąć elementy listy tak, by lista stała się posortowana i zwrócić
wskaźnik do głowy tej listy. Można założyć, że wszystkie liczby na liście są różne i że lista ma co
najmniej dwa elementy. Funkcja powinna działać w czasie liniowym względem długości listy
wejściowej.
"""


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def arr_to_list(arr):
    list_head = None
    list_tail = None
    for value in arr:
        if list_head is None:
            list_head = Node(value)
            list_tail = list_head
            continue
        list_tail.next = Node(value)
        list_tail = list_tail.next

    return list_head


def print_list(list):
    tmp = list
    while tmp is not None:
        print(tmp.value, end=" ", sep=" ")
        tmp = tmp.next
    print("")


def fix_sorted_list(lst):
    lst_head = lst
    p = lst
    q = p.next
    r = q.next
    if p.value > q.value:
        lst_head = lst_head.next
        lst = lst.next
        while lst.next is not None and p.value > lst.next.value:
            lst = lst.next
        if lst.next is None:
            print_list(lst_head)
            lst.next = p
            p.next = None
            return lst_head
        else:
            p.next = lst.next
            lst.next = p
            return lst_head
    else:
        while r is not None and q.value <= r.value:
            p = p.next
            q = q.next
            r = r.next
    if r is None:
        return lst
    if r.next is not None and r.next.value > q.value:
        p = p.next
        q = q.next
        r = r.next
        p.next = r
    elif r.next is not None and r.next.value <= q.value:
        p.next = r
    elif r.next is None and r.value < q.value:
        q.next = None
        q = r
    if lst.value > q.value:
        q.next = lst
        return q
    while lst.next is not None and q.value > lst.next.value:
        lst = lst.next
    q.next = lst.next
    lst.next = q
    return lst_head


arr = [1, 2, 3, 3, 5, 6, 7, 10, 8, 9, 11, 13]
lst = arr_to_list(arr)
lst = fix_sorted_list(lst)
print_list(lst)