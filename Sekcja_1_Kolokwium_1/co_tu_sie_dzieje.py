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
    while tail.next is not None:
        tail = tail.next

    return result, tail


def find_sorted(l):
    left_head = Node(0)
    series_end = left_head

    series_end.next = l.next
    series_end = series_end.next
    l.next = l.next.next

    while l.next is not None:
        if l.next.value >= series_end.value:
            series_end.next = l.next
            series_end = series_end.next
            l.next = l.next.next
        else:
            break
    series_end.next = None
    return left_head, l


def merge_sort(l):
    while True:
        new_l = None
        new_l_tail = None
        while l.next is not None:
            left, l = find_sorted(l)
            if l.next is None and new_l is None:
                return l
            elif l.next is None:
                new_l, right = merge_lists(new_l, left)
            else:
                right, l = find_sorted(l)
                merged, tail = merge_lists(left, right)

                if new_l is None:
                    new_l = merged
                    new_l_tail = tail
                else:
                    new_l_tail.next = merged
                    new_l_tail = tail

            l = new_l


a = [5, 3, 1, 11, 9, 7]

l_a = Node(0)

for x in a:
    tmp = Node(x, l_a.next)
    l_a.next = tmp

print_list(l_a, "la:")
print("")
l_head, r_head = find_sorted(l_a)
print_list(l_head, "Left head")
print_list(r_head, "Right head")
sorted_arr = merge_sort(l_a)
print_list(sorted_arr, "Sorted")




