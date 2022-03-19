from collections import deque


def binary_add(queue, val):
    n = len(queue)
    if len(queue) == 0:
        queue.append([val, 1])
        return
    l = 0
    r = len(queue) - 1
    while l <= r:
        q = (l + r) // 2
        print(q)
        if queue[q][0] == val:
            return
        if queue[q][0] < val:
            l = q + 1
        else:
            r = q - 1
    print()
    print(queue, val)
    if l == 0:
        queue.appendleft([val, 1])
    if l >= n:
        queue.append([val, queue[n - 1][1] + 1])
    if queue[l][0] > val:
        queue[l][0] = val
    print(queue, val)


def lis_n_log_n(A):
    queue = deque([])
    for i in range(len(A)):
        binary_add(queue, A[i])
    print(queue[-1][1])


A = [2, 5, 2, 8, 5, 3, 6, 7, 8,6, 100,1]
lis_n_log_n(A)
