"""
1. Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
struct Node{ Node* next; double value; }
Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
zaimplementowanej funkcji.
"""


from random import randint, seed
from math import floor


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


def count_lst(lst):
    tmp = lst
    c = 0
    while tmp is not None:
        c += 1
        tmp = tmp.next
    return c


def remove_max(lst):
    lst_head = Node(-999, lst)
    p = lst_head.next
    pp = lst_head
    p_to_max = lst_head
    while p is not None:
        if p.value > p_to_max.next.value:
            p_to_max = pp
        pp = p
        p = p.next

    max = p_to_max.next
    p_to_max.next = p_to_max.next.next
    return lst_head.next, max


def min_sort(lst):
    lst_head = lst
    sort_tail = lst
    sorted = None
    last =None
    while sort_tail is not None:
        sort_tail, max = remove_max(sort_tail)
        max.next = sorted
        if sorted is None:
            last = max
        sorted = max

    return sorted, last


def bucket_sort_adj(lst):
    lst_head = lst
    lst = lst.next  # Usuniecie wartownika z listy
    n = count_lst(lst)
    buckets = [0]*n
    buckets_heads = [0]*n
    for i in range(n):
        buckets[i] = Node(-1)
        buckets_heads[i] = buckets[i]

    while lst is not None:
        idx = floor((lst.value/10) * n)

        # init = buckets[idx].value
        buckets[idx].next = lst
        buckets[idx] = buckets[idx].next
        lst = lst.next

    sorted = None
    last_bucket_last = None
    for i in range(n):
        buckets[i].next = None

        buckets_heads[i] = buckets_heads[i].next
        buckets_heads[i], last = min_sort(buckets_heads[i])
        print_list(buckets_heads[i])
        if last_bucket_last:
            last_bucket_last.next = buckets_heads[i]
        else:
            if last is not None:
                print_list(buckets_heads[i])
                sorted = buckets_heads[i]
        if last is not None:
            print_list(sorted)
            last_bucket_last = last

    print(sorted.next.value)

    lst_head.next = None
    lst_head.value = sorted.value
    print(count_lst(sorted))
    print_list(sorted)
    return sorted


seed(68)
arr = [randint(0, 99)/10 for _ in range(1000)]
# print(sorted(arr))
print(arr)
lt = arr_to_list(arr)

lt = Node(-1, lt)
bucket_sort_adj(lt)
# lt = list_insertion_sort(lt)
min_sort(lt)
print_list(lt)
print(count_lst(lt))
