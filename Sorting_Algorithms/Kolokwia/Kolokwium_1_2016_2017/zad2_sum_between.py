"""
    Proszę zaimplementować funkcję:
    int SumBetween(int T[], int from, int to, int n);
    Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
    tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
    liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
    Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
    czasową (oraz bardzo krótko uzasadnić to oszacowanie)
"""


def partition(tab, p, r):
    pivot = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= pivot:
            i += 1
            tab[j], tab[i] = tab[i], tab[j]
    tab[r], tab[i + 1] = tab[i + 1], tab[r]
    return i + 1


def select(tab, p, r, k):
    if p == r:
        return tab[p]
    q = partition(tab, p, r)
    if q == k:
        return tab[k]
    elif k < q:
        return select(tab, p, q - 1, k)
    else:
        return select(tab, q + 1, r, k)


tab = [2, 5, 7, 8, 4, 2, 4, 6, 87, 5, 34, 3, 6, 7, 8, 5, 43, 2, 345, 56, 57, 6, 45]
i1 = 5
i2 = 10
min = select(tab, 0, len(tab)-1, i1)
max = select(tab, 0, len(tab)-1, i2)
sum = min+max
for i in range(len(tab)):
    if min < tab[i] < max:
        sum += tab[i]
print(sum)
# print(select(tab, 0, len(tab)-1, 12))
print(sorted(tab))
# złożoność: Wyszukiaiwanie select: 2*O(n) + wyszukiawnia liczb mniejszych i większych: O(n) : złożoność O(3n) = O(n)