def place_spaces(t, d):
    def dict(word):
        return word in d
    n = len(t)
    F = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(i, n):
            if dict(t[i:j+1]):
                F[i][j] = True
            for k in range(i, j+1):
                F[i][j] = F[i][j] or (F[i][k] and F[k+1][j])
    for i in range(n):
        for j in range(n):
            F[i][j] = int(F[i][j])
    for line in F:
        print(line)
    print(F[0][-1])
dict = ["ala","ma","kota","i","nie","ma","psa","a","o","lama","kot"]

place_spaces("alamakotainiemapsa", dict)

