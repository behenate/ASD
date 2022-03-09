from copy import  copy
class FastMinMaxInsert:
    def __init__(self):
        self.min_to_max = []
        self.max_to_min = []
        self.min_heap = []
        self.max_heap = []

    def swap(self, arr, i, j, mtx, xtm):
        arr[i], arr[j] = arr[j], arr[i]
        xtm[mtx[i]], xtm[mtx[j]] = xtm[mtx[j]], xtm[mtx[i]]
        mtx[i], mtx[j] = mtx[j], mtx[i]

    def insert_min(self, arr, mtx, xtm):
        idx = len(arr)-1
        p_idx = abs(idx-1)//2
        while arr[idx] < arr[p_idx]:
            self.swap(arr, idx, p_idx, mtx, xtm)
            idx = p_idx
            p_idx = idx//2

    def insert_max(self, arr, xtm, mtx):
        idx = len(arr)-1
        p_idx = abs(idx-1)//2
        while arr[idx] > arr[p_idx]:
            self.swap(arr, idx, p_idx, xtm, mtx)
            idx = p_idx
            p_idx = idx//2

    def insert(self, value):
        mtx = self.min_to_max
        xtm = self.max_to_min
        n = len(self.min_to_max)
        self.min_heap.append(value)
        self.max_heap.append(value)
        mtx.append(n)
        xtm.append(n)
        self.insert_min(self.min_heap, mtx, xtm)
        self.insert_max(self.max_heap, xtm, mtx)
        print(self.min_heap, self.max_heap, mtx, xtm)

    def max_heapify(self, arr, idx, mtx, xtm):
        left = idx * 2 + 1
        right = left + 1
        max = idx
        if left < len(arr) and arr[max] < arr[left]:
            max = left
        if right < len(arr) and arr[max] < arr[right]:
            max = right
        if max != idx:
            self.swap(arr, idx, max, xtm, mtx)
            self.max_heapify(arr, max, mtx, xtm)

    def min_heapify(self, arr, idx, mtx, xtm):
        left = idx * 2 + 1
        right = left + 1
        min = idx
        if left < len(arr) and arr[min] > arr[left]:
            min = left
        if right < len(arr) and arr[min] > arr[right]:
            min = right
        if min != idx:
            self.swap(arr, idx, min, mtx, xtm)
            self.min_heapify(arr, min, mtx, xtm)

    def remove_max(self):
        mtx = self.min_to_max
        xtm = self.max_to_min
        # Remove elem from max
        self.swap(self.max_heap, 0, len(self.max_heap)-1, xtm, mtx)
        self.max_heap.pop()
        # xtm.pop()
        self.max_heapify(self.max_heap, 0, mtx, xtm)
        # Remove elem from min
        self.swap(self.min_heap, xtm[-1], len(self.min_heap)-1, mtx, xtm)
        self.min_heap.pop()
        self.min_heapify(self.min_heap, xtm[-1], mtx, xtm)
        xtm.pop()
        mtx.pop()
        print(self.min_heap, self.max_heap, mtx, xtm)

    def remove_min(self):
        mtx = self.min_to_max
        xtm = self.max_to_min
        # Remove elem from max
        self.swap(self.min_heap, 0, len(self.min_heap)-1, mtx, xtm)
        self.min_heap.pop()
        self.min_heapify(self.min_heap, 0, mtx, xtm)
        # Remove elem from min
        self.swap(self.max_heap, mtx[-1], len(self.max_heap)-1, xtm, mtx)
        self.max_heap.pop()
        self.max_heapify(self.max_heap, mtx[-1], mtx, xtm)
        xtm.pop()
        mtx.pop()
        print(self.min_heap, self.max_heap, mtx, xtm)


structure = FastMinMaxInsert()

structure.insert(5)
structure.insert(4)
structure.insert(3)
structure.insert(2)
structure.insert(1)
structure.insert(6)
structure.insert(7)

structure.remove_max()
structure.remove_min()