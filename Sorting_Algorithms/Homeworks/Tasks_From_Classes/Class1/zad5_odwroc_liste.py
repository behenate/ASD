"""
Zadanie 5. (odwracanie listy) Proszę zaimplementować funkcję odwracającą listę jednokierunkową
"""


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


def invert(list):
    head = list
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current =next

    return prev


arr = [1, 2, 3, 4, 5, 6, 7]
lst = arr_to_list(arr)
lst = invert(lst)
print_list(lst)