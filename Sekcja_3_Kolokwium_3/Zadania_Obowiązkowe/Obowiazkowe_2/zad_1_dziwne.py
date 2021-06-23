from queue import PriorityQueue
from cmath import inf

def Path(parent, ind, path):
    if parent[ind] == -1:
        return [ind] + path
    return Path(parent, parent[ind], [ind] + path)


def Dijkstra(G, s, t):
    kol = PriorityQueue()
    odl = [inf] * len(G)
    parents = [-1] * len(G)

    def Relax(u, v):
        if odl[v] > odl[u] + G[u][v]:
            odl[v] = odl[u] + G[u][v]
            parents[v] = u
            kol.put((odl[v], v))

    odl[s] = 0
    kol.put((odl[s], s))
    while kol.qsize() > 0:  # jeśli kolejka nie jest pusta
        u = kol.get()  # z kolejki wyciągamy najmn wartosc
        for i in range(len(G)):  # iterujemy po wierszu macierzy
            # jeśli jest połaczenie krawędziowe i krawędz poprzednia ma większą wartosc
            # lub to jest wierzch końcowy to relaksujemy
            if 0 < G[u[1]][i] < G[u[1]][parents[u[1]]] or (u[1] == s and G[u[1]][i] != 0):
                Relax(u[1], i)  # take it eeeeeeeaaaaaassyyyyyyy

    path = Path(parents, t, [])

    return odl[t], path


if __name__ == '__main__':
    i = inf
    G = [[0, 2, 0, 3, 2],
         [2, 0, 1, 0, 0],
         [0, 1, 0, 1, 0],
         [3, 0, 1, 0, 1],
         [2, 0, 0, 1, 0]]
    # G = [[0, 8, 30, 20],
    #    [8, 0, 7, 2],
    #    [30, 7, 0, 1],
    #    [20, 2, 1, 0]]
    # _G = [
    #     [0, 2, 5, 0, 0, 0],
    #     [2, 0, 0, 3, 7, 0],
    #     [5, 0, 0, 4, 0, 0],
    #     [0, 3, 4, 0, 2, 2],
    #     [0, 7, 0, 2, 0, 1],
    #     [0, 0, 0, 2, 1, 0],
    # ]
    _G = [
        [0, 7, 8, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 6, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 6, 7, 0, 6, 5, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 5, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    ]

    print(Dijkstra(_G, 0, 9))
