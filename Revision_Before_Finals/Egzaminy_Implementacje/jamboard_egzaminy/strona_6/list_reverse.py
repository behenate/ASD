class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next =next

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


lst = arr_to_list([1,2,3,4,5,6,7,8])
print_list(lst)

def reverse_list(l):
    prev = l
    curr = l.next
    prev.next = None
    while curr is not None:
        nxt = curr.next
        curr.next = prev

        prev = curr
        curr = nxt
    print_list(prev)
reverse_list(lst)