arr = [1, 2, 3, 4, 4, 7, 8, 12, 13, 14, 16, 16]


def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        m = (left + right) // 2
        if num < arr[m]:
            right = m - 1
        elif num > arr[m]:
            left = m + 1
        else:
            return m
    return -1


print(binary_search(arr, 2))
# test co to halo test halo