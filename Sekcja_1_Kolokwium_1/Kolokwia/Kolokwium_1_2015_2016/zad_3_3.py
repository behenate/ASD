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


def fix_sorted_list(list):
    lst = Node(-999, list)
    b_p = None
    p = lst
    q = lst.next
    while q is not None and p.value <= q.value:
        b_p = p
        p = p.next
        q = q.next
    if q is None:
        return lst.next
    if q.next is None:
        if q.value < p.value:
            p.next = None
            b_p = lst
            p = lst.next
            while q.value > p.value:
                b_p = p
                p = p.next
            b_p.next = q
            q.next = p
        return lst.next
    if p.value >= q.next.value:
        b_p.next = q
        b_q = None
        while q is not None and p.value > q.value:
            b_q = q
            q = q.next
        b_q.next = p
        p.next = q
    else:
        print(p.value)
        p.next = q.next
        p_b = lst
        p = lst.next
        while p is not None and p.value < q.value:
            p_b = p
            p = p.next
        p_b.next = q
        q.next = p
    return lst.next


arr = [1, 2, 3, 3, 5, 6, 7, 7, 9, 11]
lst = arr_to_list(arr)
lst = fix_sorted_list(lst)
print_list(lst)
