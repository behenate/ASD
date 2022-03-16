"""4. (mnożenie macierzy) Dany jest cięg macierzy A1, A2, . . . , An. Ktoś chce policzyć iloczyn
A1A2⋯An. Macierze nie sa koniecznie kwadratowe (ale oczywiście znamy ich rozmiary). Zależnie w jakiej
kolejnosci wykonujemy mnożenia, koszt obliczeniowy moze byc różny—należy podać algorytm znajdujący
koszt mnożenia przy optymalnym doborze kolejnośc"""

from math import inf


def calc_mult_cost(matrix_l):
    n = len(matrix_l)
    F = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i] = 0
    for i in range(n - 1):
        F[i][i + 1] = matrix_l[i][0] * matrix_l[i][1] * matrix_l[i + 1][1]
    recur_matrix(F, 0, n - 1, matrix_l)
    for line in F:
        print(line)
    return F[0][n-1]

def recur_matrix(F, i, j, matrix_l):
    if F[i][j] != inf:
        return F[i][j]
    for k in range(i, j):
        F[i][j] = min(F[i][j], recur_matrix(F, i, k, matrix_l) + recur_matrix(F, k + 1, j, matrix_l)\
                      + matrix_l[i][0] * matrix_l[k][1] * matrix_l[j][1])
    return F[i][j]


matrix_l = [[30, 35], [35, 15], [15, 5], [5, 10], [10, 20], [20, 25]]
calc_mult_cost(matrix_l)
arr1 = [(10, 20), (20, 30), (30, 40), (40, 30)]  # ma być 30000
print(arr1, calc_mult_cost(arr1))
arr2 = [(40, 20), (20, 30), (30, 10), (10, 30)]  # ma być 26000
print(arr2, calc_mult_cost(arr2))
