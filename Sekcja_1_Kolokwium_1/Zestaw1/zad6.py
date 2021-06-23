"""
Zadanie 6. (wyszukiwanie binarne) Proszę zaimplementować funkcję, która otrzymuje na wejściu posortowaną niemalejąco
tablicę A o rozmiarze n oraz liczbę x i sprawdza, czy x występuje w A. Jeśli tak, to zwraca najmniejszy indeks,
pod którym x występuje.
"""
def find_num(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return False
arr = [1,2,3,4,6,8,9]
print(find_num(arr, 7))