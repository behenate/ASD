from zad7 import huffman
from random import seed, randint
from geeks4geeks import huffman_geeks

# Tester nie sprawdza czy podany kod huffmana jest optymalny, a jedynie czy nie ma w nim
# kodów które nie są prefiksowe/są powtórkami

S = "abcdefghijklmnoprstuqyxyz"
n = len(S)
fails = 0
for i in range(10000):
    F = [randint(1, 1000) for _ in range(len(S))]
    cost, res_tab = huffman(S,F)
    cost_geeks = huffman_geeks(S,F)
    if cost != cost_geeks:
        fails += 1
        continue
    for i in range(n):
        code_a = res_tab[i]
        for j in range(n):
            code_b = res_tab[j]
            f = False
            if j != i and len(code_a) <= len(code_b) and code_a[:] == code_b[:len(code_a)]:
                fails += 1
                f = True
                break
        if f:
            break

print("Test finished with: {} fails". format(fails))