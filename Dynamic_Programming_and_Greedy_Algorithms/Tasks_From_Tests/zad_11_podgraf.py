from time import time

n = 1000
_G = [[0 for i in range(n-1)] for _ in range(n)]
n = len(_G)
m = len(_G[0])
for i in range(n):
    offset = 0
    for j in range(m):
        if j == i:
            offset += 1
        _G[i][j] = j + offset
# for line in _G:
#     print(line)
def find_subgraph(G, k):
    n = len(G)
    degrees = [len(G[i]) for i in range(n)]
    stack = [i for i in range(n)]
    while len(stack) > 0:
        elem = stack.pop()
        if degrees[elem] < k and degrees[elem] != -1:
            for neigh in G[elem]:
                if degrees[neigh] != -1 and degrees[neigh] < k:
                    degrees[neigh] -= 1
                    stack.append(neigh)
            degrees[elem] = -1
    print(degrees)

start = time()
find_subgraph(_G, 50000)
end= time()-start
print(end)

start = time()
find_subgraph(_G, 50000)
end = time()-start
print(end)