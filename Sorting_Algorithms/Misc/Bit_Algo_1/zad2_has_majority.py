"""
Sprawdź czy tablica posiada wartość występującą w niej najwięcej razy
"""

def has_majority(arr):
    leader = None
    counter = 1
    for i in range(len(arr)):
        if arr[i] != leader:
            counter -= 1
            if counter == 0:
                leader = arr[i]
                counter = 1
        else:
            counter += 1
    r_c = 0
    for elem in arr:
        if elem == leader:
            r_c += 1

    return len(arr)/r_c > 0.5

arr = [1,2,3,4,5,6,7,8,9,10,5,5,5]
print(has_majority(arr))
