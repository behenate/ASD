provinces = [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1]
print(len(provinces))
k = 3
current = 0
last_placed = -k
while last_placed + k < len(provinces):
    c = min(current + k, len(provinces)-1)
    while c >= 0 and provinces[c] == 0 and c != last_placed:
        c -= 1
    print(c)
    if c == last_placed or provinces[c] == 0 and c == 0:
        print("Nie da się!")
        exit()
    last_placed = c
    print("Placing on: {}".format(c))
    current = c + k

