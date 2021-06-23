def count_sort(tab, k, letter):
    n = len(tab)
    b = [0]*n
    c = [0]*k

    for elem in tab:
        if letter < len(elem):
            c[ord(elem[letter])-96] = c[ord(elem[letter])-96]+1
        else:
            c[0] += 1
    for i in range(1, k):
        c[i] = c[i] + c[i-1]

    for k in range(n-1, -1, -1):
        if letter < len(tab[k]):
            b[c[ord(tab[k][letter])-96]-1] = tab[k]
            c[ord(tab[k][letter])-96] -= 1
        else:
            b[c[0]-1] = tab[k]
            c[0] -= 1
    return b


def radix_string(tab, max_len):
    for i in range(max_len-1, -1, -1):
        tab = count_sort(tab, 27, i)
    return tab


sexy_stringi_jak_glos_kamila = ["asd", "asdfas", "ksdfasdf", "asdf", "fsdfasdf", "asdfd", "dsdfsadf", "asdfs", "sad"]
max_len = 8
radix_string(sexy_stringi_jak_glos_kamila, 8)
print(radix_string(sexy_stringi_jak_glos_kamila, max_len))

