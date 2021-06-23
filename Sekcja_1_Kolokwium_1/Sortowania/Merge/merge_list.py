from math import ceil, floor


class Node:
    def __init__(self, value, next=None):
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


def merge(l1, l2):
    merged = Node(-9999)
    m_h = merged
    while l1 is not None and l2 is not None:
        if l1.value < l2.value:
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
        print_list(p)
        print_list(q)
        l1 = merge_lists(p, floor(n / 2))
        l2 = merge_lists(q, ceil(n / 2))
        return merge(l1, l2)
    return lst

arr = [7, 8, 4, 5, 9, 2]
m1 = [4]
m2 = [2]
m1l = arr_to_list(m1)
m2l = arr_to_list(m2)
print_list(merge(m1l, m2l))
lst = arr_to_list(arr)
res = merge_lists(lst, 6)
print_list(res)
