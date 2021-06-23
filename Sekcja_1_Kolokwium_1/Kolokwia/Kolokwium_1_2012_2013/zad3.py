from random import choice
from time import time


def possible(u, v, w):
    required = [0] * 26
    required_int = 0
    for letter in w:
        if required[ord(letter) - 97] == 0:
            required_int += 1
        required[ord(letter) - 97] += 1
    for letter in u:
        required[ord(letter) - 97] -= 1
        if required[ord(letter) - 97] == 0:
            required_int -= 1
            if required_int == 0:
                break
    if required_int > 0:
        for letter in v:
            required[ord(letter) - 97] -= 1
            if required[ord(letter) - 97] == 0:
                required_int -= 1
                if required_int == 0:
                    break
    return required_int == 0


def slowo(u, v, w):
    litery = [0] * 26
    for i in range(len(u)):
        litery[ord(u[i]) - 97] += 1
    for i in range(len(v)):
        litery[ord(v[i]) - 97] += 1
    for i in range(len(w)):
        litery[ord(w[i]) - 97] -= 1
        if litery[ord(w[i]) - 97] < 0:
            return False
    return True


u = [choice(
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "y",
     "z"]) for _ in range(15000)]

v = [choice(
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "y",
     "z"]) for _ in range(15000)]
w = [choice(
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "y",
     "z"]) for _ in range(10000)]


print("Wojtek:")
start = time()
print(possible(u, v, w))
print(time() - start)
print("Basia:")
start = time()
print(slowo(u, v, w))
print(time() - start)
