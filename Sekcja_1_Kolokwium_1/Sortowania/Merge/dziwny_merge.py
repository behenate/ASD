from random import randint, seed
from time import time

def divide(T, b, e):
    if b < e:
        mid = (b + e) // 2
        left = divide(T, b, mid)
        right = divide(T, mid + 1, e)
        return merge(T, b, mid, mid + 1, e)


def merge(T, bl, el, br, er):
    temp = []
    pom_start_index = bl

    for i in range(er - bl + 1):
        if bl <= el and br <= er and T[bl] > T[br]:
            temp.append(T[br])
            br += 1
        elif bl <= el and br <= er:
            temp.append(T[bl])
            bl += 1
        if bl > el:
            temp.append(T[br])
            br += 1
        if br > er:
            temp.append(T[bl])
            bl += 1
        if bl > el and br > er: break
    j = 0
    for i in range(pom_start_index, er + 1):
        T[i] = temp[j]
        j += 1
    return T


def mergesort(T):
    T = divide(T, 0, len(T) - 1)
    print("Tu proszę napisać swoją funckję")
    return T


seed(42)

n = 10
T = [randint(1, 100) for i in range(1000000)]

# print("przed sortowaniem: T =", T)
start = time()
T = mergesort(T)
print(time()-start)
# print("po sortowaniu    : T =", T)

for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK")
