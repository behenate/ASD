"""

Zadanie 2. (sortowanie listy jednokierunkowej) Proszę zaimplementować algorytm sortowania listy
jednokierunkowej. W szczególności należy:
1. Zdefiniować klasę w Pythonie realizującą listę jednokierunkową.
2. Zaimplementować wstawianie do posortowanej listy.
3. Zaimplementować usuwanie maksimum z listy.
4. Zaimplementować sortowanie przez wstawianie lub sortowanie przez wybieranie na podstawie powyższych funkcji


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
        print(tmp.value, end=None)
        tmp = tmp.next
    print("")



def insert_into_list(lst, value):
    head = Node(-9999, lst)
    tail = head
    q = tail
    while tail is not None:
        if tail.value > value:
            q.next = Node(value, q.next)
            head = head.next
            return head
        else:
            if tail.next is None:
                tail.next = Node(value)
                head = head.next
                return head
            q = tail
            tail = tail.next


def remove_largest(list):
    head = Node(0, list)
    previous_to_max_node = head
    current = previous_to_max_node

    while current.next is not None:
        if current.next.value > previous_to_max_node.next.value:
            previous_to_max_node = current
        current = current.next
    max_node = previous_to_max_node.next
    if previous_to_max_node.next.next is not None:
        previous_to_max_node.next = previous_to_max_node.next.next
    else:
        previous_to_max_node.next = None
    head = head.next
    return head, max_node


def select_sort(list):
    sorted = None
    head = list
    while head is not None:
        head, m = remove_largest(head)
        sorted = Node(m.value, sorted)
    return sorted


arr = [1, 3, 5, 7, 9, 2]
test = arr_to_list(arr)
t1 = select_sort(test)
print_list(t1)
