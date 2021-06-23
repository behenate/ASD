class e:
    def __init__(self, p, c, source_index=None):
        self.p = p
        self.c = c
        self.i = source_index

    def __lt__(self, other):
        return self.p < other.p

    def __gt__(self, other):
        return self.p > other.p


class MaxHeap:
    def __init__(self, arr):
        self.arr = arr
        self.len = len(arr)
        self.create_heap()

    def heapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        m = i
        if l < self.len and self.arr[l] > self.arr[m]:
            m = l
        if r < self.len and self.arr[r] > self.arr[m]:
            m = r
        if m != i:
            self.arr[i], self.arr[m] = self.arr[m], self.arr[i]
            self.heapify(m)

    def create_heap(self):
        n = self.len
        p = n // 2
        for i in range(p, -1, -1):
            self.heapify(i)

    def remove_max(self):
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
        while self.arr[parent] < self.arr[i] and i > 0:
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent
            parent = (i - 1) // 2

    def get_max(self):
        return self.arr[-1]


def calculate_order(k, W, P, C):
    n = len(C)
    # Jakaś tablica tupli, dużo lepiej po prostu zmodyfikować quicksort, ale mi mi się nie chce
    t_l = [e(P[i], C[i], i) for i in range(n)]
    t_l.sort()
    # Don't do that on kolos, bruh

    heaps = []
    tasks = []
    heaps.append([t_l[0]])
    for i in range(1, n):
        if t_l[i-1].c == t_l[i].c:
            heaps[-1].append(t_l[i])
        else:
            heaps.append([t_l[i]])

    m = len(heaps)
    for i in range(m):
        heaps[i] = MaxHeap(heaps[i])

    master_heap = MaxHeap([])

    for i in range(k):
        max_profit = 0
        l_j = 0
        for j in range(l_j, m):
            if heaps[j].len == 0:
                continue
            if heaps[j].get_max().c > W:
                print("no zarucz no")
                l_j = j
                break
            a = heaps[j].get_max()
            master_heap.insert(e(a.p, a.c, j))

        elem = master_heap.remove_max()
        removed = heaps[elem.i].remove_max()
        if heaps[elem.i].len > 0:
            a = heaps[elem.i].get_max()
            master_heap.insert(e(a.p, a.c, elem.i))
        tasks.append(removed.i)
        W += removed.p
    for task in tasks:
        a = t_l[task]
    print(W)

_k = 3
_w = 0
_P = [1, 2, 3, 1000]
_C = [0, 1, 1, 4]
calculate_order(_k, _w, _P, _C)
