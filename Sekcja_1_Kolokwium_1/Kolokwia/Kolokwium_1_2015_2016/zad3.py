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


def fix_list(lst):
    lst = Node(-999, lst)
    prev = lst
    p = lst.next
    while

arr = [1, 2, 2, 1, 3 , 7]
print(arr)
lst = arr_to_list(arr)
lst = fix_list(lst)
print_list(lst)
