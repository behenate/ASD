"""

Dany jest ciąg klocków (k1, ..., kn). Klocek ki zaczyna się na pozycji ai
i ciągnie się do pozycji bi
(wszystkie pozycje to liczby naturalne) oraz ma wysokość 1. Klocki układane są po kolei. Jeśli
klocek nachodzi na któryś z poprzednich, to jest przymocowywany na szczycie poprzedzającego
klocka. Na przykład dla klocków o pozycjach (1,3), (2,5), (0,3), (8,9), (4,6) powstaje konstrukcja
o wysokości trzech klocków (vide rysunek). Proszę podać możliwie jak najszybszy algorytm,
który oblicza wysokość powstałej konstrukcji (bez implementacji) oraz oszacować jego złożoność
obliczeniową

"""
def klocki(arr):
    n = len(arr)
    m = 0
    for i in range(n):
        m = max(m, arr[i][1])
    h_arr = [0 for _ in range(m+1)]
    for block in arr:
        a = block[0]
        b = block[1]
        m_loc = 0
        for k in range(a, b):
            m_loc = max(m_loc, h_arr[k])
        for k in range(a, b):
            h_arr[k] = m_loc+1
    print(max(h_arr))
_klocki = [(1,3), (2,5), (0,3), (4,6), (8,9)]
klocki(_klocki)
