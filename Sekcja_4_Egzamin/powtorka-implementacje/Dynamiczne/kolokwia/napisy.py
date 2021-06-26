from math import inf

S = ["ab", "abab", "ba", "bab", "b"]
t = "ababbab"


def word_func(S, t):
    n = len(t)
    F = [[0 for _ in range(n)] for _ in range(n)]
    for word in S:
        for start in range(n - len(word)+1):
            s = 1
            for j in range(len(word)):
                if word[j] != t[start + j]:
                    s = 0
            if s == 1:
                F[start][start + len(word)-1] = len(word)


    for j1 in range(1, n):
        for i in range(n):
            j = i+j1
            if i+j > n:
                break
            for k in range(i, j):
                print(i,j, "   ", i,k,"  ",k+1,j)
                F[i][j] = max(F[i][j], min(F[i][k], F[k+1][j]))
    for line in F:
        print(line)

word_func(S, t)




