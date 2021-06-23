def find_recur_in_heap(heap, value, index, k, found):
    l_child = 2 * index + 1
    r_child = l_child + 1
    c = 0
    if heap[index] <= value and found < k:
        c += 1
        if l_child < len(heap):
            c += find_recur_in_heap(heap, value, l_child, k, found + c)
        if r_child < len(heap):
            c += find_recur_in_heap(heap, value, r_child, k, found + c)
    return c

def how_many(heap, value, k):
    res = find_recur_in_heap(heap, value, 0, k, 0)
    return res==k

min_heap_arr = [3, 4, 6, 9, 11, 14, 13, 15, 10, 17, 16, 20, 21, 15, 16, 19]
print(len(min_heap_arr))
print(find_recur_in_heap(min_heap_arr, 20, 0, 5, 0))
