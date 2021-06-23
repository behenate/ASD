from math import inf
_T = [
    [0, 3, 4, 0, 0, 0],
    [3, 0, 0, 5, 2, 0],
    [4, 0, 0, 0, 3, 0],
    [0, 5, 0, 0, 2, 2],
    [0, 2, 3, 2, 0, 1],
    [0, 0, 0, 2, 1, 0],
]

_D = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 2, 2, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 2, 0, 0, 2, 2],
    [0, 2, 1, 2, 0, 1],
    [0, 0, 0, 2, 1, 0],
]
def floyd_warshall(T, D):
    n = len(T)
    times = [[T[i][j] if T[i][j] != 0 else inf for j in range(n)] for i in range(n)]
    distances = [[D[i][j] if D[i][j] != 0 else inf for j in range(n)] for i in range(n)]
    for t in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    times[i][j] = 0
                    distances[i][j] = 0
                    continue
                if times[i][j] > times[i][t] + times[t][j] or times[i][j] == times[i][t] + times[t][j] and \
                        distances[i][j] < distances[i][t] + distances[t][j]:
                    times[i][j] = times[i][t] + times[t][j]
                    distances[i][j] = distances[i][t] + distances[t][j]
    for line in times:
        print(line)
    print()
    for line in distances:
        print(line)


floyd_warshall(_T, _D)


