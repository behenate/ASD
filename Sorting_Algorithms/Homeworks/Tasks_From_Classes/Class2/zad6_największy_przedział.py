"""
Zadanie 6 (największy przedział). Dany jest ciąg przedziałów domkniętych [a1, b1], . . . ,[an, bn]. Proszę
zapropnować algorytm, który znajduje taki przedział [at, bt], w którym w całości zawiera się jak najwięcej
innych przedziałów
"""


def fits(s1, s2):
    if s1[0] <= s2[0] and s1[1] >= s2[1]:
        return True
    return False


def find_max_section(tab):
    n = len(tab)

    max_chad_cap = 1
    potential_chads = [-1 for _ in range(n)]
    potential_chads[0] = 0

    for elem in potential_chads:
        if elem == -1:
            continue

        chad_index = elem
        chad_section = tab[chad_index]
        curr_chad_cap = 0
        for i in range(elem, n):
            if fits(chad_section, tab[i]):
                print(chad_section, tab[i])
                potential_chads[i] = -1
                curr_chad_cap += 1
                print(curr_chad_cap)
            elif fits(tab[i], chad_section):
                chad_section = tab[i]
                potential_chads[chad_index] = -1
                chad_index = i
                curr_chad_cap += 1
            else:
                potential_chads[i] = i

        if curr_chad_cap > max_chad_cap:
            max_chad_cap = curr_chad_cap
    return chad_section


print(fits((5, 6), (1, 3)))
sections = [(1, 3), (7, 7), (7, 7), (1, 4), (2, 3), (3, 4), (5, 6), (7, 10), (7, 7), (7, 7), (7, 7), (7, 7), (7, 7),
            (7, 7)]

find_max_section(sections)
