slowa = ["a", "la", "ala", "lama", "kot", "kota", "ma", "mak", "ta"]

def slice(p,q,string):
    return string[p:q+1]

def fill(word="alamakotamak"):
    n = len(word)
    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            print(i,j, word[i:j+1])
            F[i][j] = word[i:j+1] in slowa
            for k in range(i + 1, j - 1):
                F[i][j] = F[i][j] or (F[i][k] and F[k+1][j])
    for line in F:
        print(line)
    return F[0][n-1]


print(fill())
