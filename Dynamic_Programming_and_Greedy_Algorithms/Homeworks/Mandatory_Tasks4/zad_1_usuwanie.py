"""Zadanie 1. (Pause) Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w
Polsce. Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które
tworza spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu
działajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Proszę zaproponować algorytm
podający kolejność wyłączania stacji."""
_G = [
    [1, 4],
    [0, 2],
    [1, 4, 3],
    [2, 6, 5],
    [0, 2, 7],
    [6, 3],
    [5, 3],
    [4]
]

def low(lows, parent, i):
    print(lows, lows[i])
    while lows[parent[i]] > lows[i] and parent[i] != -1:
        print("Doing for: ", parent[i], "from: ", lows[parent[i]], "to: ", lows[i])
        lows[parent[i]] = lows[i]
        i = parent[i]


def DFS(G):
    def DFS_visit(G, i):
        nonlocal time
        time += 1
        visited[i] = True
        times[i] = time
        lows[i] = time
        for neigh in G[i]:
            if visited[neigh] and parent[i] != neigh and parent[i] != -1:
                lows[i] = lows[neigh]
                low(lows, parent, i)
            elif not visited[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh)

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    times = [0 for _ in range(n)]
    lows = [0 for _ in range(n)]
    time = 0

    DFS_visit(G, 0)
    safe_list = []
    for i in range(n):
        if lows[i] == times[i] and parent[i] != -1:
            safe_list.append(i)
            safe_list.append(parent[i])
    # safe_list = sorted(safe_list, reverse=True)
    

    _N_G = []
    for elem in safe_list:
        _N_G.append([])
        for neigh in G[elem]:
            if neigh in safe_list:
                _N_G[-1].append(neigh)
    # print(times, lows)
    # print(parent)
    return visited, parent, time


DFS(_G)
