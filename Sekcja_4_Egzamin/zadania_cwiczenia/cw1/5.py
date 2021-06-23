class Node:
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next

def print_list(list):
    while list is not None:
        print(list.val, "->", end="")
        list = list.next
    print()

def reverse_list(list):
    prev = list
    list = list.next
    prev.next = None
    while list.next is not None:
        n = list.next
        list.next = prev
        prev = list
        list = n
    list.next = None
    list.next = prev
    return list

e = Node(5)
d = Node(4, e)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)
print_list(a)
reverse_list(a)
print_list(e)