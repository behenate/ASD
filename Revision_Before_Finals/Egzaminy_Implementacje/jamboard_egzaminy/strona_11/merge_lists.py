from math import inf
from queue import PriorityQueue

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val



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


def print_list(l, label=''):
    tmp = l
    print(label)
    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next


def merge_lists(A):
    n = len(A)
    new = Node(-inf)
    new_head = new
    nones = 0
    queue = PriorityQueue()
    for i in range(n):
        queue.put(A[i])
    while nones != n:
        to_add = queue.get()
        new.next = to_add
        new = new.next
        if to_add.next is None:
            nones += 1
        else:
            queue.put(to_add.next)

    new.next = None
    print_list(new_head.next)


A = [[0, 1, 2, 4, 5], [0, 10, 20], [5, 15, 25]]
for i in range(len(A)):
    A[i] = arr_to_list(A[i])
merge_lists(A)
