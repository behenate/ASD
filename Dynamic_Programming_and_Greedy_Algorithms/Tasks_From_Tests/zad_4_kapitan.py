"""
Kapitan pewnego statku zastanawia się, czy może wpłynąć do portu mimo tego, że nastąpił
odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy:
int n = ...
int m = ...
int A[m][n];
gdzie wartość A[y][x] to głębokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna
wartość int T to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port
znajduje się na pozycji (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio
jedynie na pozycję bezpośrednio obok (to znaczy, na pozycję, której dokładnie jedna ze
współrzędnych różni się o jeden). Proszę napisać funkcję rozwiązującą problem kapitana.
"""


from queue import Queue


def BFS(G, s, depth):
    queue = Queue()
    n = len(G)
    queue.put(s)
    while not queue.empty():
        elem = queue.get()
        x = elem[0]
        y = elem[1]
        G[x][y] = depth - 1
        if x - 1 >= 0 and G[x - 1][y] > depth:
            queue.put((x - 1, y))
        if x + 1 < n and G[x + 1][y] > depth:
            queue.put((x + 1, y))
        if y - 1 >= 0 and G[x][y - 1] > depth:
            queue.put((x, y - 1))
        if y + 1 < n and G[x][y + 1] > depth:
            queue.put((x, y + 1))
    return G[n-1][n-1] < depth

map = [
    [10, 1, 1, 1, 9, 9],
    [9, 8, 1, 1, 9, 1],
    [1, 5, 9, 9, 9, 1],
    [1, 1, 6, 7, 9, 1],
    [1, 1, 1, 3, 8, 10],
    [1, 1, 1, 1, 1, 10]
]
print(BFS(map, (0,0), 4))
