from math import inf


def stringi(S, t):
    n = len(t)
    F =[[inf for _ in range(n)] for _ in range(n)]
    print(ciasne_stringi(t,S,F,0,n-1))
    for line in F:
        print(line)


def ciasne_stringi(t,S, F, i, j):
    if F[i][j] != inf:
        return F[i][j]
    if t[i:j+1] in S:
        F[i][j] = 1
        return 1
    small = inf
    for k in range(i,j-1):
        small = min(small, ciasne_stringi(t,S,F,i,k) + ciasne_stringi(t,S,F,k+1,j))
    F[i][j] = small
    return small




S = ["ab","abab", "ba", "bab", "b"]
t = "ababbab"
stringi(S,t)