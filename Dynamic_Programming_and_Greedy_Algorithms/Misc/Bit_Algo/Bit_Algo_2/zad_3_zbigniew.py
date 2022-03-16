"""Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
(wartość przekąki dodaje się do aktualnej energii Zbigniewa).
Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie. Funkcja powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do
n-1 lub −1 jeśli nie jest to możliwe."""

from math import inf
def zbigniew(A):
    n = len(A)
    m = 0
    for i in range(n):
        m += A[i]
    F = [[inf for _ in range(m)] for _ in range(n)]
    F[0][A[0]] = 0
    for i in range(1, n):
        for j in range(m):
            for k in range(1, i+1):
                if 0 <= j+k-A[i] < m:
                    F[i][j] = min(F[i][j], F[i-k][j+k-A[i]] + 1)
    for line in F:
        print(line)
    print(min(F[n-1]))


A = [4,1,1,1,1]
zbigniew(A)
