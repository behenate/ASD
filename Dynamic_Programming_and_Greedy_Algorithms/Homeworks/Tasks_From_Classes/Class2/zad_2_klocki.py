"""
Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
[a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
algorytm, który oblicza ile klocków należy usunąć z listy tak, żeby każdy kolejny spadajacy klocek mieścił
się w całości w tam, który spadł tuż przed nim.
"""
from math import inf


def blocks(A):
    n = len(A)
    F = [-1] * n
    F[0] = 0
    maxi = 0
    for i in range(1, n):
        for j in range(i):
            if A[i][0] >= A[i][0] and A[i][1] <= A[j][1]:
                F[i] = max(F[i], F[j]+1)
        maxi = max(maxi, F[i])
    print(n-maxi)

A = [[4, 8], [2, 3], [5, 7], [6, 7], [1, 2]]
blocks(A)