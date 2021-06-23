
from random import randint, getrandbits, seed

def linear_ujscie(G):
    n = len(G)
    might_be = [1 for _ in range(n)]
    next_that_works = 1
    i = 0
    checks = 0
    while i < n - 1:
        for j in range(i + 1, n):
            checks += 1
            if G[i][j] == 1:
                might_be[i] = 0
                i = j
                break
            else:
                next_that_works += 1
                might_be[j] = 0
                if j == n - 1:
                    return check(G, i)
    for i in range(n):
        if might_be[i]:
            if check(G, i):
                return True
    print("Ni ma :(")
    return False
    # print("Checks: {}, n:{}, złozonosc: {}n".format(checks, n, checks / n))

def check(G, i):
    n = len(G)
    for j in range(n):
        if (not G[j][i] or G[i][j]) and j != i:
            return False
    for line in G:
        print(line)
    return True
# linear_ujscie(_G)
_G = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

_G1 = [
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1],
]
print(linear_ujscie(_G1))
n = 5
seed(2)
# for i in range(1000):
#
#     _G = [[getrandbits(1) for _ in range(n)] for _ in range(n)]
#     linear_ujscie(_G)