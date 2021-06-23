def find_path(arr):
    n = len(arr[0])
    m = len(arr)
    costs = [[99999999 for _ in range(n)] for _ in range(m)]
    costs[0][0] = 3
    # Wypełnij pierwszą kolumnę i wiersz kosztami. Dla nich wartości są znane
    for i in range(1, n):
        costs[0][i] = costs[0][i - 1] + arr[0][i]
    for i in range(1, m):
        costs[i][0] = costs[i - 1][0] + arr[i][0]

    # Dla wszystkich do tej pory nie wypełnionych wybierz minimalny koszt i przypisz go do tablicy
    for i in range(1, n):
        for j in range(1, m):
            costs[i][j] = min(costs[i - 1][j], costs[i][j - 1]) + arr[i][j]

    print(find_path_res_recur(arr, costs, m-1, n-1))


def find_path_res_recur(arr, costs, m, n):
    if m == 0 and n == 0:
        return [[m, n]]
    # Jako że zaczynamy od końca to sprawdź z którego pola udało się dojść do tego momentu, dodaj jego współrzędne
    #I wywołaj rekurencję
    if m > 0 and costs[m][n] == costs[m - 1][n] + arr[m][n]:
        return find_path_res_recur(arr, costs, m - 1, n) + [[m, n]]
    if n > 0 and costs[m][n] == costs[m][n - 1] + arr[m][n]:
        return find_path_res_recur(arr, costs, m, n - 1) + [[m, n]]


_arr = [
    [3, 1, 1, 1, 1, 1, 1],
    [2, 4, 5, 2, 1, 4, 1],
    [3, 1, 5, 4, 2, 3, 1],
    [4, 1, 7, 3, 4, 1, 1],
    [1, 2, 3, 7, 3, 4, 1],
    [1, 2, 4, 2, 2, 7, 1],
    [3, 4, 1, 3, 1, 4, 1]
]

find_path(_arr)

"""
def find_path_res(arr, costs):
    n = len(arr[0]) - 1
    m = len(arr) - 1
    path = []
    while n != 0 or m != 0:
        path.append(arr[n][m])
        if n == 0:
            m -= 1
            continue
        if m == 0:
            n -= 1
            continue
        if costs[n - 1][m] < costs[n][m - 1] and n > 0:
            n -= 1
        else:
            m -= 1
    path.append(arr[0][0])
    path.reverse()

    return path
"""
