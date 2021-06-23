"""
Zadanie 5. (Lider ciągu) Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.
"""


def find_leader(tab):
    leader = tab[0]
    c = 1
    for i in range(1, len(tab)):
        if c == 0:
            leader = tab[i]
            c = 1
        else:
            if tab[i] == leader:
                c += 1
            else:
                c -= 1
    return leader

tab = [1,2,1,2,1,3,1,2,1,3,1,2,3,1]
leader = find_leader(tab)
l_c = 0
for elem in tab:
    if elem == leader:
        l_c += 1
if l_c > len(tab) /2:
    print("Liczba:{} jest liderem".format(leader))
else:
    print("Ni ma lidera")

