def find_subset(arr, sum):
    n = len(arr)
    break_i = -1
    exists = [[0 for _ in range(sum+1)] for _ in range(n)]
    for i in range(n):
        exists[i][0] = 1
    for i in range(n):
        if i == arr[0]:
            exists[0][i] = 1
            break
    for i in range(1,n):
        for j in range(sum+1):
            if exists[i-1][j]:
                exists[i][j] = 1
                if j==sum:
                    break_i = i
                    break
                if j+arr[i] <= sum:
                    exists[i][j+arr[i]] = 1
                    if j+arr[i] == sum:
                        break_i = i
                        break
    for line in exists:
        print(line)
    print(break_i, sum)
    print(find_elements(arr, exists, break_i, sum))


def find_elements(arr, exists, index, sum):
    if index == 0:
        if sum == 0:
            return []
        return [sum]
    if exists[index-1][sum] == 1:
        return find_elements(arr,exists,index-1,sum)
    return find_elements(arr, exists, index-1, sum-arr[index]) + [arr[index]]



nums = [2,8,1,3,7,9]
find_subset(nums, 7)