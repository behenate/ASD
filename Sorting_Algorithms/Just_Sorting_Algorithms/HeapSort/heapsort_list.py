class Node:
    def __init__(self, value=None, l_child=None, r_child=None):
        self.l_child = l_child
        self.r_child = r_child
        self.value = value


# Jakim cudem to zadziałało od strzała to nie wiem
def arr_to_tree(arr, elem, i, n):
    left = 2 * i + 1
    right = left + 1
    elem.value = arr[i]
    if left < n:
        elem.l_child = arr_to_tree(arr, Node(), left, n)
    if right < n:
        elem.r_child = arr_to_tree(arr, Node(), right, n)
    return elem


def heapify(elem):
    biggest = elem
    if elem.l_child is not None and elem.l_child.value > biggest.value:
        biggest = elem.l_child
    if elem.r_child is not None and elem.r_child.value > biggest.value:
        biggest = elem.r_child

    if biggest != elem:
        print(elem.value, biggest.value)
        elem.value, biggest.value = biggest.value, elem.value
        print(elem.value, biggest.value)
        heapify(biggest)


def build_max_heap(elem,i,n, init=True):
    left = 2 * i + 1
    right = left + 1
    if left < n//2:
        build_max_heap(elem.l_child, left, n, False)
        heapify(elem.l_child)
    if right < n//2:
        build_max_heap(elem.r_child, right, n, False)
        heapify(elem.r_child)
    if init:
        heapify(elem)


def heapsort(elem,i,n, init=True):
    if init:
        build_max_heap(elem,i,n)
    left = 2 * i + 1
    right = left + 1


    heapify(elem)

tab = [0,3,2,5,6,1,4]
bruh = arr_to_tree(tab, Node(), 0, len(tab))
heapsort(bruh,0,len(tab))
print(bruh)
