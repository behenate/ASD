arr = [5, 2, 4, 6, 1, 3]
"""
    Wybiera się elementy po kolei od drugiego do końca i porównuje z wcześniejszymi elementami.
    Przesuwa się ten element w lewo tablicy tak długo jak długo wartość  elementu jest mniejsza od wartości elementu
    po lewej. W ten sposób zawsze na lewo od wybranego elementu tablica jest posortowana.
"""

def insertion_sort(tab):
    for j in range(1, len(tab)):
        key = tab[j]
        i = j-1
        while i >= 0 and tab[i] > key:
            print(tab)
            tab[i+1] = tab[i]
            i -= 1
        tab[i+1] = key


insertion_sort(arr)
print(arr)
