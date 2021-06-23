from queue import PriorityQueue

S = ["a", "b", "c", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]



def huffman(S, F):
    n = len(S)
    queue = PriorityQueue()
    transformations = ["" for _ in range(n)]
    cnt = 0
    for i in range(n):
        queue.put((F[i], [i]))
    while cnt != n-1:
        a = queue.get()
        b = queue.get()
        for elem in a[1]:
            transformations[elem] = "1" + transformations[elem]
        for elem in b[1]:
            transformations[elem] = "0" + transformations[elem]
        cnt += 1
        queue.put((a[0]+b[0], a[1]+b[1]))

    print(queue.queue)
    print(S)

    print(transformations)
    sum = 0
    for i in range(n):
        sum += len(transformations[i]) * F[i]
    print(sum)
    return transformations
    pass


huffman(S, F)
