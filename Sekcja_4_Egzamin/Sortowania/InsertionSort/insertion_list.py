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
    print(prev.value)
    return lst.next, prev


arr = [1, 2, 5, 7, 8, 1123]
lt = arr_to_list(arr)
lt, last = insertion_list(lt)
print_list(lt)