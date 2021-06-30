from queue import Queue
def BFS(G,s):
    Q = Queue()
    n = len(G) #ilosc wierzcholkow
    #przyszlam 1/2 lub 1L, przyszlam 2L
    visited = [[False,False] for _ in range(n)]
    d = [[-1,-1] for _ in range(n)]
    visited[s][0] = True
    visited[s][1] = True
    d[s][0] = 0
    d[s][1] = 0
    Q.put((s,1))
    while not Q.empty():
        u,last = Q.get()
        for j in range(n):
            if G[u][j] != 0:
                neigh = j
                if last == 1 or last == 2:
                    if G[u][j] == 1 or G[u][j] == 2:
                        if visited[neigh][0] == False:
                            visited[neigh][0] = True
                            d[neigh][0] = d[u][0]+ 1
                            Q.put((neigh, G[u][neigh]))
                    if G[u][j] == 3:
                        if visited[neigh][1] == False:
                            visited[neigh][1] = True
                            d[neigh][1] = d[u][1]+ 1
                            Q.put((neigh, G[u][neigh]))
                if last == 3 and G[u][j] == 1:
                    if visited[neigh][1] == False:
                        visited[neigh][1] = True
                        d[neigh][1] = d[u][1]+ 1
                        Q.put((neigh, G[u][neigh]))
    print(d)
from math import sqrt
def odleglosc(x1,y1,x2,y2):
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
#1 to 1/2L, 2 to L, 3 to 2L
def zabcia(T,L):
    n = len(T)
    G = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                weight = odleglosc(T[i][0],T[i][1],T[j][0],T[j][1])
                if weight <= L/2:
                    G[i][j] = 1
                elif weight <= L:
                    G[i][j] = 2
                elif weight <= 2*L:
                    G[i][j] = 3
    BFS(G,0)

points = [
    [0, 0],
    [1, 1],
    [2, 1],
    [3, 1],
    [4, 1],
    [6, 1],
    [6, 2],
    [3, 3],
    [3, 4],
    [3, 5],
    [5, 5],
    [7, 5],
    [8, 6],
]
zabcia(points,2)