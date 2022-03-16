G = [
    [1],
    [0, 2],
    [1, 3],
    [2, 4],
    [3, 10, 5],
    [4, 6],
    [5, 7],
    [6, 8],
    [7, 9],
    [8],
    [4, 11, 12],
    [10, 13, 14],
    [10, 15, 16],
    [11],
    [11],
    [12],
    [12]
]
cities = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]


def DFS_mark_unnecessary(G, cities):
    def DFS_visit(G, i):
        visited[i] = True
        r = cities[i]
        for neigh in G[i]:
            if not visited[neigh]:
                r = DFS_visit(G, neigh) or r
        if not r:
            to_remove[i] = 1
        return r

    n = len(G)
    visited = [False for _ in range(n)]
    to_remove = [0 for _ in range(n)]
    for i in range(n):
        if cities[i]:
            to_remove[i] = 0
            DFS_visit(G, i)
            break
    return to_remove

def find_diameter(G, blocked):
    def DFS_visit(G, i, dist):
        dist += 1
        nonlocal max_dist_i
        nonlocal max_dist
        if dist > max_dist:
            max_dist = dist
            max_dist_i = i
        visited[i] = True
        for neigh in G[i]:
            if not visited[neigh] and not blocked[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh, dist)
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    time = 0
    max_dist = -1
    max_dist_i = -1
    for i in range(n):
        if not blocked[i]:
            DFS_visit(G,i, 0)
            break
    max_dist = -1
    s_i = max_dist_i
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    DFS_visit(G, s_i, 0)
    e_i = max_dist_i
    main_path = [0 for _ in range(n)]
    while e_i != s_i:
        main_path[e_i] = 1
        e_i = parent[e_i]
    main_path[e_i] = 1
    return main_path


def sum_subtrees(G, blocked, main_path):
    def DFS_visit(G, i):
        nonlocal main_sum
        main_sum += 2
        visited[i] = True
        for neigh in G[i]:
            if not visited[neigh] and not blocked[neigh]:
                DFS_visit(G, neigh)
    n = len(G)
    main_sum = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if main_path[i]:
            main_sum += 1
        if main_path[i] and len(G[i]) > 2:
            visited[i] = True
            for neigh in G[i]:
                if not main_path[neigh]:
                    DFS_visit(G, neigh)
    main_sum -= 1
    print(main_sum)

blocked = DFS_mark_unnecessary(G, cities)
main_path = find_diameter(G, blocked)
sum_subtrees(G, blocked, main_path)
print(blocked)
