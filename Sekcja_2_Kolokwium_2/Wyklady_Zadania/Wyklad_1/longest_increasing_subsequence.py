def lis(arr):
    n = len(arr)
    lew = [1] * n
    sub_tab = [-1]*n
    for i in range(1, n):
        longest_continues = 1
        for j in range(i-1, -1, -1):
            if lew[j] + 1 > longest_continues and arr[j] < arr[i]:
                longest_continues = lew[j] + 1
                sub_tab[i] = j
        lew[i] = longest_continues

    max_len_index = -1
    for i in range(n):
        if lew[max_len_index] < lew[i]:
            max_len_index = i
    i = max_len_index
    print_solution(arr, sub_tab, i)

def print_solution(arr, sub_tab, index):
    if index == -1:
        return
    print_solution(arr,sub_tab, sub_tab[index])
    print(arr[index])



arr = [3, 1, 5, 7, 2, 4, 9, 17, 3]
lis(arr)
