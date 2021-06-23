def least_refueling_path(l, s):
    p_i = 0
    n = len(s)
    refuel_cnt = 0
    for i in range(-1, n - 1, 1):
        if s[i + 1] - p_i > l:
            print("refueling at: ", s[i])
            if i != -1:
                p_i = s[i]
            else:
                p_i = s[0]
            refuel_cnt += 1
    return refuel_cnt


S = [4, 6, 9, 14, 16]
print(least_refueling_path(5, S))
