from random import randint, seed
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
def left(i):
    return 2*i +1
def right(i):
    return 2*i+2


def k_th_greater(heap, k, x):
    def greater_recur(heap, i):
        nonlocal cnt
        if cnt+1 > k:
            return
        if left(i) < n and heap[left(i)] < x:
            cnt += 1
            greater_recur(heap, left(i))
        if right(i) < n and heap[right(i)] < x:
            cnt += 1
            greater_recur(heap, right(i))
    n = len(heap)
    if heap[0] > x:
        return
    cnt = 0
    if heap[0] < x:
        cnt = 1
    greater_recur(heap, 0)
    return cnt+1 <= k

seed(0)
heap_arr = [randint(1, 10) for  i in range(10)]
print(heap_arr)
print(heap_arr)
heap = MinHeap(heap_arr)
print(heap_arr)
print(k_th_greater(heap_arr,4, 7))
print(sorted(heap_arr))

# no napraw ze sei