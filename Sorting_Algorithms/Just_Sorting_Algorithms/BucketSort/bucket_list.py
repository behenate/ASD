from random import randint, seed
from math import floor
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


def insertion_list(lst):
    lst = Node(-9999, lst)
    prev = lst
    curr = lst.next
    while curr is not None:
        if curr.value >= prev.value:
            curr = curr.next
            prev = prev.next
        else:
            prev.next = curr.next
            insert_pointer = lst
            while curr.value > insert_pointer.next.value:
                insert_pointer = insert_pointer.next

            curr.next = insert_pointer.next
            insert_pointer.next = curr
            curr = prev.next

    return lst.next, prev


def bucket_list(list, n):
    buckets_heads = [0]*n
    buckets_tails = [0]*n
    for i in range(n):
        buckets_heads[i] = Node(-1)
        buckets_tails[i] = buckets_heads[i]
    p = list
    while p is not None:
        i = floor(p.value * n)
        buckets_tails[i].next = p
        buckets_tails[i] = buckets_tails[i].next
        p = p.next
    bucket_sorted = None
    last_tail = None
    for i in range(n):
        buckets_tails[i].next = None
        buckets_heads[i] = buckets_heads[i].next
        res, last = insertion_list(buckets_heads[i])
        if last.value != -9999:
            if bucket_sorted is None:
                bucket_sorted = res
            else:
                last_tail.next = res
            last_tail = last

    return bucket_sorted


seed(42)
n = 10
test_tab = [randint(1, 999)/1000 for _ in range(n)]
print(test_tab)
t_l = arr_to_list(test_tab)
res = bucket_list(t_l, n)
print_list(res)