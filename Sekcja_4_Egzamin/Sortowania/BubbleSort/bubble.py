def bubble_sort(tab):
    n = len(tab)
    for i in range(n):
        for j in range(i+1, n):
            if tab[i] > tab[j]:
                tab[i], tab[j] = tab[j], tab[i]

arr = [3,2,1,2,3,2,34,5,7,4,3,6,7]
bubble_sort(arr)
print(arr)
