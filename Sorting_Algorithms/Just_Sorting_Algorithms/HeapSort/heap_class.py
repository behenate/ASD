class Heap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    @staticmethod
    def left(index):
        return (index * 2) + 1

    @staticmethod
    def right(index):
        return index * 2 + 2

    def heapify(self, index):
        n = len(self.heap)
        m = index
        l = self.left(index)
        r = self.right(index)
        if l < n and self.heap[m] < self.heap[l]:
            m = l
        if r < n and self.heap[m] < self.heap[r]:
            m = r

        if m != index:
            print("co")
            self.heap[m], self.heap[index] = self.heap[index], self.heap[m]
            self.heapify(m)

    def insert(self, value):
        self.heap.append(value)
        c_i = len(self.heap)-1
        p = self.parent(c_i)
        while p >= 0 and self.heap[p] < self.heap[c_i]:
            self.heap[p], self.heap[c_i] = self.heap[c_i], self.heap[p]
            c_i = p
            p = self.parent(c_i)

    def remove(self, index):
        self.heap[-1], self.heap[index] = self.heap[index], self.heap[-1]
        self.heap.pop()
        self.heapify(index)

    def print(self):
        print(self.heap)


heap = Heap()
for i in range(10):
    heap.insert(i)
heap.print()
heap.remove(3)
heap.print()

