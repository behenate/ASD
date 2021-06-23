from random import randint, seed

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

def split(lst):
    even_head = Node(0)
    even = even_head
    p = lst
    prev = None
    if p.value % 2 == 0:
        even.next = p
        lst = lst.next
        even = even.next

    while p.next is not None:
        if p.next.value % 2 == 0:
            even.next = p.next
            even = even.next
            p.next = p.next.next
        prev = p
        p = p.next

    if p.value % 2 == 0:
        even.next = p
        prev.next = None

    print_list(lst)
    print_list(even_head.next)

seed(42)
arr=[randint(1,10) for i in range(10)]
print(arr)
lt = arr_to_list(arr)
split(lt)