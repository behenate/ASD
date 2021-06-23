def klocki(arr):
    n = len(arr)
    m = 0
    for i in range(n):
        m = max(m, arr[i][1])
    h_arr = [0 for _ in range(m+1)]
    for block in arr:
        a = block[0]
        b = block[1]
        m_loc = 0
        for k in range(a, b):
            m_loc = max(m_loc, h_arr[k])
        for k in range(a, b):
            h_arr[k] = m_loc+1
    print(max(h_arr))
_klocki = [(1,3), (2,5), (0,3), (4,6), (8,9)]
klocki(_klocki)