def lis(arr):
    n = len(arr)
    lew = [1] * n
    sub_tab = [[] for _ in range(n)]
    for i in range(1, n):
        longest_continues = 1
        for j in range(i - 1, -1, -1):
            if lew[j] + 1 >= longest_continues and arr[j] < arr[i]:
                longest_continues = lew[j] + 1
                sub_tab[i].append(j)
        lew[i] = longest_continues

    max_len_index = -1
    for i in range(n):
        if lew[max_len_index] < lew[i]:
            max_len_index = i
    i = max_len_index
    print(sub_tab)
    # for line in sub_tab:
    #     print(line)
    print(sub_tab)
    print(lew)
    max_val = max(lew)
    to_print_arr = []
    for i in range(n):
        if lew[i] == max_val:
            to_print_arr.append(i)
    print("")
    print(arr)
    print(lew)
    print(sub_tab)
    print(to_print_arr)
    print("RESULT: ")
    for i in range(len(to_print_arr)):
        print_solution(arr, sub_tab, to_print_arr[i], [])


def print_solution(arr, sub_tab, c_i, append_tab):

    if len(sub_tab[c_i]) == 0:
        append_tab.append(arr[c_i])
        append_tab.reverse()
        print(append_tab)
        return

    clones = []
    append_tab.append(arr[c_i])
    for j in range(len(sub_tab[c_i]) - 1):
        clones.append([])
        for elem in append_tab:
            clones[j].append(elem)

    for i in range(len(sub_tab[c_i])):
        if i == 0:
            print_solution(arr, sub_tab, sub_tab[c_i][i], append_tab)
        else:
            print_solution(arr, sub_tab, sub_tab[c_i][i], clones[i-1])


# def print_solution(arr, sub_tab, index, index_ret2d=0):
#     if len(sub_tab[index]) == 0:
#         ret2d[index_ret2d].append(arr[index])
#         return [arr[index]]
#     to_ret = []
#     for i in range(len(sub_tab[index])):
#         while index_ret2d + i >= len(to_ret):
#             ret2d.append([])
#         ret2d[index_ret2d].append(print_solution(arr, sub_tab, sub_tab[index][i], index_ret2d+i) + [arr[index]])
#     return to_ret


arr = [3, 1, 5, 7, 2, 4, 3]
lis(arr)


