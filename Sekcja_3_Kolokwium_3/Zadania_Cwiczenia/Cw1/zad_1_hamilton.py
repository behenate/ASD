def top_sort(G):
    def DFS_visit(G, i):
        visited[i] = True
        for neigh in G[i]:
            if not visited[neigh]:
                parent[neigh] = i
                DFS_visit(G, neigh)
        top_order.append(i)
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    top_order = []

    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i)
    top_order.reverse()
    return visited, parent, top_order

def check_hamilton(G):
    sorted = top_sort(G)[2]
    for i in range(len(sorted)-1):
        f = False
        for neigh in G[sorted[i]]:
            if neigh == sorted[i+1]:
                f = True
        if not f:
            print("false")
            return False
    print("True")
    return True
_G = [
    [1],
    [2],
    [3,4],
    [4,],
    [5, 6],
    [],
    [7],
    [5]
]
check_hamilton(_G);
