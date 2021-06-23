_G = [[[1, 3], [2, 4]], [[0, 3], [3, 5]], [[0, 4], [3, 5], [4, 3]], [[1, 5], [2, 5], [4, 5], [5, 6]],
      [[2, 3], [3, 5], [5, 7]], [[4, 7], [3, 6]]]


def contains(a, b):
    if a[0] <= b[0] and a[1] >= b[1]:
        return True
    return False


def sep(a, b):
    if a[0] > b[1] or b[0] > a[1]:
        return True
    return False


def reduce(a, b):
    r = [max(a[0], b[0]), min(a[1], b[1])]
    return r


def przelot(G, s, e, t):
    def DFS_visit(G, i, r):
        print(r)
        res = False
        visited[i].append(r)
        if i == e:
            print("no co")
            return True
        for neigh in G[i]:
            alt = reduce(r, [neigh[1] - t, neigh[1] + t])
            for rng in visited[neigh[0]]:
                if contains(rng, alt):
                    alt = []
                    break
                if not sep(alt, rng):
                    alt = reduce(alt, rng)
            if alt == []:
                continue
            res = DFS_visit(G, neigh[0], alt) or res
        return res
    n = len(G)
    visited = [[] for _ in range(n)]

    print(DFS_visit(G, 0,[-100, 100]))
    print(visited)

przelot(_G, 0, 5, 2)
