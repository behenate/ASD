from math import inf

"""Zadanie 3. Dany jest zbiór klocków K = {K1, . . . , Kn}. Każdy klocek Ki opisany
jest jako jednostronnie domknięty przedział (ai
, bi], gdzie ai
, bi ∈ N, i ma wysokość 1 (należy
założyć, że żadne dwa klocki nie zaczynają się w tym samym punkcie, czyli wartości ai są
parami różne). Klocki są zrzucane na oś liczbową w pewnej kolejności. Gdy tylko spadający
klocek dotyka innego klocka (powierzchnią poziomą), to jest do niego trwale doczepiany i
przestaje spadać. Kolejność spadania klocków jest poprawna jeśli każdy klocek albo w całości
ląduje na osi liczbowej, albo w całości ląduje na innych klockach. Rozważmy przykładowy
zbiór klocków K = {K1, K2, K3, K4}, gdzie:
K1 = (2, 4], K2 = (5, 7], K3 = (3, 6], K4 = (4, 5].
Kolejność K1, K4, K2, K3 jest poprawna (choć są też inne poprawne kolejności) podczas gdy
kolejność K1, K2, K3, K4 poprawna nie jest (K3 nie leży w całości na innych klockach):
1 2 3 4 5 6 7 8
K1 K4 K2
K3
(a) Klocki po tym, jak spadały w poprawnej kolejności K1, K4, K2, K3.
1 2 3 4 5 6 7 8
K1
K4
K2
K3
(b) Klocki po tym, jak spadały w niepoprawnej kolejności K1, K2, K3, K4.
Proszę podać algorytm (bez implementacji), który sprawdza czy dla danego zbioru klocków
istnieje poprawna kolejność spadania. Proszę uzasadnić poprawność algorytmu oraz oszacować jego złożoność. Proszę także odpowiedzieć na następujące pytanie:
Czy jeśli początki klocków nie muszą być parami różne to algorytm dalej działa poprawnie? Jeśli tak, proszę to uzasadnić. Jeśli nie, to proszę podać kontrprzykład."""
def tower(A):
    n = len(A)
    F = [1 for _ in range(n)]
    for i in range(1, n):
        for k in range(i):
            if A[k][0] <= A[i][0] and A[k][1] >= A[i][1]:
                F[i] = max(F[i], F[k] + 1)
    print(F)


_A = [
    (1, 4),
    (0, 5),
    (1, 5),
    (2, 6),
    (2, 4)
]
tower(_A)
_A = [
    [10, 15],
    [8, 14],
    [1, 6],
    [3, 10],
    [8, 11],
    [6, 15]
]
tower(_A)
