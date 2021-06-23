def palindrom(word):
    n = len(word)
    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i] = True
    for i in range(n-1):
        F[i][i+1] = word[i] == word[i+1]
    max_len = 1
    for i in range(2,n):
        for j in range(n-i):
            if i-max_len > 3:
                break
            F[j][i+j] = F[j+1][i+j-1] and (word[j] == word[i+j])
            if F[j][i+j]:
                max_len = i+1
    for line in F:
        print(line)
    print(max_len)

palindrom("acaclasdjfl;abababababababa")