class Node:
    def __init__(self, value, next=None):
        self.val = value
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
        print(tmp.val, end=" ", sep=" ")
        tmp = tmp.next
    print("")


def merge_list(a_list, b_list):
    if a_list.val > b_list.val:
        a_list, b_list = b_list, a_list
    head = a_list
    to_add = b_list
    while to_add is not None:
        while a_list.next is not None and to_add.val > a_list.next.val:
            a_list = a_list.next
        tmp = to_add
        to_add = to_add.next
        if a_list.next is not None:
            tmp.next = a_list.next
        else:
            tmp.next = None
        a_list.next = tmp
    return head


a_list = arr_to_list([1, 3, 5, 7, 9, 100])
b_list = arr_to_list([0, 2, 4, 6, 9, 9, 9])

r = merge_list(a_list, b_list)
print_list(r)
