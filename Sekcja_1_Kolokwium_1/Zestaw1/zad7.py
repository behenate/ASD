"""
Zadanie 7. (szukanie sumy) Dana jest posortowana tablica A[1...n] oraz liczba x. Proszę napisać program,
który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x
"""
def find_sum(arr, target):
    i=0
    while i<len(arr) and arr[i] < target:
        j = 0
        i += 1
        while j < len(arr) and (arr[i] + arr[j]) < target:
            j += 1
        if arr[i] + arr[j] == target:
            return i, j




arr = [1, 2, 3, 4, 6, 8, 9]
print(find_sum(arr, 7))