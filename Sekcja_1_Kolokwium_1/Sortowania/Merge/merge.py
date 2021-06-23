class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_list(l, label=''):
    tmp = l
    print(label)
    while tmp is not None:
        print(tmp.value)
        tmp = tmp.next


def merge_lists(list_1, list_2):
    result = Node(0)
    tail = result

    while list_1.next is not None and list_2.next is not None:
        print(list_1.next.value)
        if list_1.next.value <= list_2.next.value:
            tail.next = list_1.next
            list_1.next = list_1.next.next
        else:
            tail.next = list_2.next
            list_2.next = list_2.next.next
        tail = tail.next

    if list_1.next is not None:
        tail.next = list_1.next
    else:
        tail.next = list_2.next

    return result


a = [7, 6, 3, 1]
b = [8, 6, 4, 2]

l_a = Node(0)
l_b = Node(0)

for x in a:
    tmp = Node(x, l_a.next)
    l_a.next = tmp
for x in b:
    tmp = Node(x, l_b.next)
    l_b.next = tmp

print_list(l_a, 'a')
print('\n')
print_list(l_b, 'b')

a_plus_b = merge_lists(l_a, l_b)
print('\n')
print_list(a_plus_b, 'a+b')



