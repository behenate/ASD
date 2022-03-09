from random import randint
from time import time


class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value


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


def print_list(list, label=None):
    n = 0
    tmp = list
    if label:
        print(label, " ", end=" ")
    while tmp is not None:
        n+=1
        print(tmp.value, end=" ", sep=" ")
        tmp = tmp.next
    print("length: {}".format(n), end="")
    print("")


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


def quicksort(l):
    l1, p1, p2, r1 = partition(l)
    grp = p1
    grq = p2
    if l1 is not None:
        grp, grq = quicksort(l1)
        grq.next = p1
        grq = p2
    if r1 is not None:
        p2.next, grq = quicksort(r1)
    return grp, grq


arr = [randint(1, 100) for _ in range(1000000)]
# print(arr)
l = arr_to_list(arr)
start = time()
eksde, lul = quicksort(l)
print(time()-start)
# print_list(eksde)