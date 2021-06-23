

def find_longest(intervals, l):
    n = len(intervals)
    intervals = sorted(intervals)
    discovered = [None for _ in range(n)]
    parent = [None for _ in range(n)]
    for i in range(n):
        print("i: ", i)
        print()
        s = i
        i_t = []
        t = l-1
        if discovered[i] is not None:
            t -= discovered[i][2] - 1
            s = discovered[i][1]
            p = discovered[i][1]
            while p != i:
                i_t.append(p)
                p = parent[p]
        i_t.append(i)
        i_t.reverse()
        print(i_t, t)
        for j in range(t):
            c_m = 0
            c_m_i = -1
            for k in range(s+1, n):
                if intervals[k][0] < intervals[s][1]:
                    if intervals[k][1] > c_m:
                        c_m_i = k
                        c_m = intervals[k][1]
                else:
                    i_t.append(c_m_i)
                    s = c_m_i
                    break
            else:
                if c_m_i != -1:
                    i_t.append(c_m_i)
                    s = c_m_i
        print(i_t)
        u = len(i_t)
        for h in range(1, u):
            parent[i_t[h]] = i_t[h-1]
        for h in range(u):
            discovered[i_t[h]] = (intervals[i_t[u-1]][1] - intervals[i_t[h]][0], i_t[u-1], l-h)
        print("i:", i,  discovered)
        print()

_intervals = [[1, 8], [4, 14], [7, 11], [10, 14], [13, 19], [18, 22], [21, 24], [23, 26]]
find_longest(_intervals, 4)







