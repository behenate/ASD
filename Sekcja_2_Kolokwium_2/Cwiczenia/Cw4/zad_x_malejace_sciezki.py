_G = [
    [0, 1, 5], [0, 2, 7], [1, 3, 4], [2, 0, 7], [2, 3, 6], [2, 4, 2], [3, 1, 4], [3, 5, 5], [3, 2, 6], [4, 2, 2],
    [4, 5, 3], [5, 4, 3], [5, 3, 5]
]


def find_path(G, s, t):
    n = len(G)
    G = sorted(G, key=lambda x: x[2])
    trying_to_connect = [t]
    for i in range(n):
        for j in range(len(trying_to_connect)):
            if G[i][1] == trying_to_connect[j]:
                trying_to_connect.append(G[i][0])
                if G[i][0] == s:
                    return True





print(find_path(_G, 0, 5))
