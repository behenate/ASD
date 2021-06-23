

def insert_into_heap(tree, value):
    n = len(tree)
    insertion_index = n
    tree.append(value)
    parent = (n-1)//2

    while tree[parent] < tree[insertion_index]:
        tree[parent], tree[insertion_index] = tree[insertion_index], tree[parent]
        insertion_index = parent
        parent = (abs(insertion_index-1))//2
    return tree


heap = [8, 7, 6, 6, 4, 6, 5, 2, 1, 4, 3, 2, 3]
heap = insert_into_heap(heap, 9)
print(heap)
