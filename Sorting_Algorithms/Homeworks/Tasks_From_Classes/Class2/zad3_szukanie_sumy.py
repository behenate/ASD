"""
Zadanie 3. (szukanie sumy) Dana jest posortowana tablica A[1...n] oraz liczba x.
Proszę napisać program, który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x
"""
def find_sum(tab, num):
    n = len(tab)
    for i in range(n):
        if tab[i] > num:
            break
        for j in range(i+1, n):
            if tab[j] + tab[i] > num:
                break
            if tab[j] + tab[i] == num:
                return True
    return False

tab = [1,2,3,4]
print(find_sum(tab, 2))