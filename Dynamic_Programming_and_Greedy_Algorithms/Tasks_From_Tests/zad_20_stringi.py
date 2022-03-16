"""
Znajdź najczęściej powtarzający się podzbiór stringów
"""

def find_rep(words, t):
    def find_rep_recur(i, j):
        if F[i][j] != -1:
            return F[i][j]
        if t[i:j + 1] in words:
            F[i][j] = j - i + 1
            return F[i][j]
        for k in range(i, j - 1):
            F[i][j] = max(F[i][j], min(find_rep_recur(i, k), find_rep_recur(k + 1, j)))
        return F[i][j]

    n = len(t)
    F = [[-1 for _ in range(n)] for _ in range(n)]
    best = find_rep_recur(0, n - 1)
    print(best)


_words = ["ab", "abab", "ba", "bab", "b"]
_t = "ababbab"
find_rep(_words, _t)
_words = ["a", "aaa", "aaaa", "aaaaa", "aaaaaa"]
_t = "aaaaaaa"

find_rep(_words, _t)
