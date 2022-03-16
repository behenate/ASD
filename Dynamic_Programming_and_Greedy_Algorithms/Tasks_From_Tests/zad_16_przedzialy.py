_ranges = [
    [0, 0.2],
    [0, 0.1],
    [0, 0.3],
    [0.2, 0.3],
    [0.3, 0.6],
    [0.5, 0.6],
    [0.4, 0.6],
    [0.5, 0.55],
    [0.7, 1],
    [0.5, 0.8],

]

def find_range(ranges):
    ranges = sorted(ranges)

    n = len(ranges)
    c_r = 0
    picked = [-1]
    c_m_i = c_r
    for i in range(n):
        if ranges[i][0] > ranges[c_r][1] and ranges[c_m_i][1] != 1:
            c_r = c_m_i
            picked.append(-1)
        if ranges[i][1] > ranges[c_m_i][1]:
            picked[-1] = i
            c_m_i = i
    print(ranges)
    print(picked)
    return ranges[picked[-1]][1]==1

print(find_range(_ranges))
