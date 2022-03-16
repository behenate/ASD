from queue import Queue




def BFS(s, pin):
    queue = Queue()
    nums = [733]
    visited = [False for _ in range(10000)]
    visited[s] = True
    queue.put(s)

    while not queue.empty():
        elem = queue.get()
        for num in nums:
            e = (elem+num)%10000
            print(e)
            if not visited[e]:
                visited[e] = True
                queue.put(e)
    print(visited)
    return visited[pin]
n = 9001
while True:

    n = (n + 733) % 10000
    print(n)
    if n == 800:
        break
# print(BFS(9001, 2000))