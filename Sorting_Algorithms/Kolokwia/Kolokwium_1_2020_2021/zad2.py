"""Treść
Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:
class Node:
def __init__(self):
self.val = None # przechowywana liczba rzeczywista
self.next = None # odsyłacz do nastepnego elementu
Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste a1, a2, . . . , an (lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każdego elementu zachodzi, że po posortowaniu listy znalazłby się na pozycji różniącej się od bieżącej
o najwyżej k. Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest
1, 0, 3, 2, 4, 6, 5, a (n − 1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności.
Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p.
Funkcja powinna zwrócić wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy
oraz używać jak najmniej pamięci (w sensie asymptotycznym, mierzonym względem długości n
listy oraz parametru k). Proszę oszacować jego złożoność czasową dla k = Θ(1), k = Θ(log n) oraz
k = Θ(n).
"""
class Node():
    def __init__(self, val=None, next = None):
        self.val = val
        self.next = next

    def __gt__(self, other):
        if other is None:
            return True
        return self.val > other.val


    def __lt__(self, other):
        if other is None:
            return True
        return self.val < other.val

class MinHeap:
    def __init__(self, arr):
        self.arr = arr
        self.len = len(arr)
        self.create_heap()

    def heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        m = i
        if l < self.len and self.arr[l] < self.arr[m]:
            m = l
        if r < self.len and self.arr[r] < self.arr[m]:
            m = r
        if m != i:
            self.arr[i], self.arr[m] = self.arr[m], self.arr[i]
            self.heapify(m)

    def create_heap(self):
        n = self.len
        p = n // 2
        for i in range(p, -1, -1):
            self.heapify(i)

    def remove_min(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        ret = self.arr.pop()
        self.len -= 1
        if self.len > 0:
            self.heapify(0)
        return ret

    def insert(self, val):
        self.arr.append(val)
        self.len += 1
        i = self.len - 1
        parent = (i - 1) // 2
        while self.arr[parent] > self.arr[i] and i > 0:
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent
            parent = (i - 1) // 2

    def get_min(self):
        return self.arr[0]


def arr_to_list(arr):
    list_head = None
    list_tail = None
    for i in range(len(arr)):
        value = arr[i]
        if list_head is None:
            list_head = Node(value)
            list_tail = list_head
            continue
        list_tail.next = Node(value)
        list_tail = list_tail.next

    return list_head


def print_list(list, label=None):
    n = 0
    tmp = list
    if label:
        print(label, " ", end=" ")
    while tmp is not None:
        n+=1
        print(tmp.val, end=" ", sep=" ")
        tmp = tmp.next
    print("length: {}".format(n), end="")
    print("")

def SortH(p, k):
    head = p
    heap = MinHeap([])
    new = Node(-1000)
    new_head = new
    n=0
    _p = head
    while _p is not None:
        _p = _p.next
        n +=1
    for i in range(2*k+1):
        heap.insert(p)
        p = p.next
        if p is None: break

    while p is not None:
        min = heap.remove_min()
        heap.insert(p)
        p = p.next
        new.next = min
        new = new.next

    for i in range(2*k +1):
        if len(heap.arr) > 0:
            min = heap.remove_min()
            new.next = min
            new = new.next
    new.next = None
    return new_head.next

from zad2testy import runtests
runtests(SortH)
# to_cvt = [1, 0, 3, 2, 4, 6, 5]
# _p = arr_to_list(to_cvt)
# print_list(SortH(_p, 1))
