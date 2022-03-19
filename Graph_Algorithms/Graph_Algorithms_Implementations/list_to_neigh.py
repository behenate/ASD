def list_to_neigh(edges, directional=False):
    n = len(edges)
    max_e = edges[0][1]
    for i in range(n):
        max_e = max(max_e, edges[i][1])
    neigh = [[] for _ in range(max_e+1)]
    for i in range(n):
        neigh[edges[i][0]].append(edges[i][1])
        if not directional:
            neigh[edges[i][1]].append(edges[i][0])
    return neigh

