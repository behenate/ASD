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
        return self.arr[-1]
